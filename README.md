# Simple Raspberry Pi Video Recorder

## Installation:
To use this simple code for recording video with Raspberry Pi, you just need to install two libraries: `opencv` and `picamera`:
```
pip install picamera2
pip install opencv-python
```

If you encounter the following error while installing either of these libraries on Raspberry Pi:
```
$ pip install Picamera2
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    For more information visit http://rptl.io/venv

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```
There are several solutions provided in [this link](https://askubuntu.com/questions/1465218/pip-error-on-ubuntu-externally-managed-environment-%C3%97-this-environment-is-extern). But in summary, you can use `pipx`. For example to install pipx, run:
```
sudo apt install pipx
```
and to install picamera2 using pipx:
```
pipx install picamera2
```
Or append `--break-system-packages` at the end of the regular `pip` command:
```
pip install picamera2 --break-system-packages
```

## Usage:
After running the program by `python cam.py` or `python3 cam.py`, press `s` to start recording. Press `e` to end the recording and save the video, and press `q` to exit the program.
