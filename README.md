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
    . requirements.sh
    . setup.sh
    python3 main.py
    ```