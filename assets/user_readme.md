The sbot Simulator
---

The robotics simulator for sbot used by the SRO society, powered by Webots.

In order to use the simulator a few set-up steps need to be done.
First you need to install Python 3.9+ and Webots R2023b.

To install Python, you can download the latest version from the [Python website](https://www.python.org/downloads/). If you have already installed Python from a package manager, such as homebrew on MacOS, apt on Ubuntu, or the Windows store on Windows, you can skip this step.
![python download site](images/python_download.png)

To install Webots, you can download the latest version from the [Webots website](https://cyberbotics.com/#download). Use the default settings when installing Webots.
![webots download site](images/webots_download.png)

Once you have installed these, you can download the latest release from the releases page and extract the contents to a folder.

- setup
    - release download
        - download the latest release from the releases page
        - extract the contents to a folder
    - release contents
        - ![release contents](images/release_contents.png)
    - config script
        - right click, open with python
        - ![open with python](images/open_with_python.png)
- where the code goes
    - zone_0 folder
    - must be called robot.py
    - other zones are available
    - use the sbot library
- how to run the simulator
    - startup script
    - UI elements
        - ![webots UI](images/webots_overview.png)
        - 3d world
        - logs in console
        - play/pause buttons
- where the logs are
    - location
        - ![logs location](images/zone_folder.png)
    - naming
- improving performance
    - ![preferences menu](images/windows_preferences.png)
    - ![reduce graphics](images/reduced_settings.png)
    - disable shadows
    - disable anti-aliasing
- common issues
    - remember to sleep
    - reopening the camera overlay
    - ![camera overlay menu](images/camera-overlays.png)
