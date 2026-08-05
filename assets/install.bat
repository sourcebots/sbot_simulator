:: sbot_simulator install script
:: This script has been generated for sbot_simulator version __RELEASE__.

wget https://github.com/sourcebots/sbot_simulator/releases/download/__RELEASE__/sbot-simulator-__RELEASE__.zip
unzip -d sbot-simulator-__RELEASE__/ sbot-simulator-__RELEASE__.zip
cd sbot-simulator-__RELEASE__/
C:\Apps\Python315\python.exe scripts/setup.py
