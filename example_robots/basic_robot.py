from sbot import arduino, motors, utils

# robot = Robot()

motors.set_power(0, 1)
motors.set_power(1, 1)

# measure the distance of the right ultrasound sensor
# pin 6 is the trigger pin, pin 7 is the echo pin
distance = arduino.measure_ultrasound_distance(6, 7)
print(f"Right ultrasound distance: {distance / 1000} meters")

# motor board, channel 0 to half power forward
motors.set_power(0, 0.5)

# motor board, channel 1 to half power forward,
motors.set_power(1, 0.5)
# minimal time has passed at this point,
# so the robot will appear to move forward instead of turning

# sleep for 2 second
utils.sleep(2)

# stop both motors
motors.set_power(0, 0)
motors.set_power(1, 0)
