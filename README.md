# Equalsafe GUI

The Equalsafe GUI provides a simple way to interact with the device without the need of an external device/phone. It includes an interface to interact with the functionalities of the device locally.

## Documentation
* Qt: [documentation](https://doc.qt.io/qtforpython-6/)

## Emulation
* Setup
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install pyqt5
    ```

* Running
    ```
    python3 main.py
    ```

## Running on device

1. Make sure that all of the daemons are running...
2. All of display drivers are installed correctly...
3. run
    ```
    . /scripts/requirements.sh
    . /scripts/setup.sh
    python3 main.py
    ```

## Install and run on boot

* inside of the directory run:
    ```
    sudo make install
    ```

* reboot the device
    ```
    sudo reboot
    ```


# REALLY IMPORTANT:

### Configure the rotation of the screen:

This has been tested on a headless ubuntu distro:
`Linux equalsafe 6.1.54-v8+ #1685 SMP PREEMPT Fri Sep 29 11:04:07 BST 2023 aarch64 GNU/Linux`

* In `boot/config.txt`
    ```
    # For 0 degree rotation:
    # (no additional entries - default setting)

    # For 90 degree rotation (top to right):
    #display_lcd_rotate=1
    #dtoverlay=rpi-ft5406,touchscreen-swapped-x-y=1,touchscreen-inverted-x=1

    # For 180 degree rotation (upside down)
    #display_lcd_rotate=2
    #dtoverlay=rpi-ft5406,touchscreen-inverted-x=1,touchscreen-inverted-y=1

    ### WE ARE USING THIS CURRENTLY
    # For 270 degree rotation (top to left)
    #display_lcd_rotate=3
    #dtoverlay=rpi-ft5406,touchscreen-swapped-x-y=1,touchscreen-inverted-y=1
    ```

### to disable raspberry's own bootup sequence:

1. Add the following lines to `/boot/config.txt`
    ```
    disable_splash=1
    ```

2. Change the `boot/cmdline.txt` to:
    * remove:
        ```
        console=tty1
        ```

    * add
        ```
        vt.global_cursor_default=0 logo.nologo quiet
        ```
