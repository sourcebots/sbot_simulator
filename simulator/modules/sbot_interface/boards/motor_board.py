"""
A simulator for the SRv4 Motor Board.

Provides a message parser that simulates the behavior of a motor board.

Based on the Motor Board v4.4.1 firmware.
"""
from __future__ import annotations

import logging

from sbot_interface.devices.motor import MAX_POWER, MIN_POWER, BaseMotor

LOGGER = logging.getLogger(__name__)


class MotorBoard:
    """
    A simulator for the SRv4 Motor Board.

    :param motors: A list of simulated motors connected to the motor board.
                     The list is indexed by the motor number.
    :param asset_tag: The asset tag to report for the motor board.
    :param software_version: The software version to report for the motor board.
    """

    def __init__(
        self,
        motors: list[BaseMotor],
        asset_tag: str,
        software_version: str = '4.4.1'
    ):
        self.motors = motors
        self.asset_tag = asset_tag
        self.software_version = software_version

    def handle_command(self, command: str) -> str:
        """
        Process a command string and return the response.

        Executes the appropriate action on any specified motors automatically.

        :param command: The command string to process.
        :return: The response to the command.
        """
        args = command.split(':')
        if args[0] == '*IDN?':
            return f'Student Robotics:MCv4B:{self.asset_tag}:{self.software_version}'
        elif args[0] == '*STATUS?':
            # Output faults are unsupported
            return "0,0:12000"
        elif args[0] == '*RESET':
            LOGGER.info(f'Resetting motor board {self.asset_tag}')
            for motor in self.motors:
                motor.disable()
            return 'ACK'
        elif args[0] == 'MOT':
            if len(args) < 2:
                return 'NACK:Missing motor number'

            try:
                motor_number = int(args[1])
            except ValueError:
                return 'NACK:Invalid motor number'
            if not (0 <= motor_number < len(self.motors)):
                return 'NACK:Invalid motor number'

            if len(args) < 3:
                return 'NACK:Missing motor command'
            if args[2] == 'SET':
                if len(args) < 4:
                    return 'NACK:Missing motor power'
                try:
                    power = int(args[3])
                except ValueError:
                    return 'NACK:Invalid motor power'
                if not (MIN_POWER <= power <= MAX_POWER):
                    return 'NACK:Invalid motor power'
                LOGGER.info(
                    f'Setting motor {motor_number} on board {self.asset_tag} to {power}'
                )
                self.motors[motor_number].set_power(power)
                return 'ACK'
            elif args[2] == 'GET?':
                return ':'.join([
                    f'{int(self.motors[motor_number].enabled())}',
                    f'{self.motors[motor_number].get_power()}',
                ])
            elif args[2] == 'DISABLE':
                LOGGER.info(f'Disabling motor {motor_number} on board {self.asset_tag}')
                self.motors[motor_number].disable()
                return 'ACK'
            elif args[2] == 'I?':
                return str(self.current())
            else:
                return 'NACK:Unknown motor command'
        else:
            return f'NACK:Unknown command {command.strip()}'
        return 'NACK:Command failed'

    def current(self) -> int:
        """
        Get the total current draw of all motors.

        :return: The total current draw of all motors in mA.
        """
        return sum(motor.get_current() for motor in self.motors)
