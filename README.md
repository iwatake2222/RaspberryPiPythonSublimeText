# Raspberry Pi Setup Guide for Python Development from Host PC with Sublime Text

## Prerequisite
* Sublime Text 3 installed (PackageControl, CodeIntel)
* I assume the IP address of Raspberry Pi is 192.168.0.144
* Install PEP
```
pip install pep8
pip install pep257

```

## Install Sublime Text packages related to python
* PackageControl -> InstallPackage
	* Python Breakpoints
	* Python Flake8 Lint

* Python break points
	* This is only for local debugging
	* Ctrl + Shift + B is to set break point
	* If you use tab indent, you need to adjust indent for inserted break point
* Flake8Lint.sublime-settings
```
{
	"pep8_max_line_length": 99,
	"ignore": ["W191","N802","I201"],
}
```

## Setup: Raspberry Pi side
* Create workspace in Raspberry Pi
	* $PI$ > mkdir ~/dev/PythonProject01

## Setup: Host PC side
* Create workspace in Host PC
	* $PC$ > mkdir ~/dev/PythonProject01
		* maybe, it is not necessary the same name
* Install SFTP package in Sublime Text
	* PackageControl -> InstallPackage -> SFTP
* Setup SFTP
	* Open the directory you created
	* Right click on the project name -> SFTP/FTP -> Map to Remote
	* modify config file
	* Note: avoid sharing this file in public if you write password
```
    "type"SublimeLinter: "sftp",

    "save_before_upload": true,
    "upload_on_save": false,
    "sync_down_on_open": false,
    "sync_skip_deletes": false,
    "sync_same_age": true,
    "confirm_downloads": false,
    "confirm_sync": true,
    "confirm_overwrite_newer": false,
    
    "host": "192.168.0.144",
    "user": "pi",
    "password": "raspberry",
    "port": "22",
    
    "remote_path": "/home/pi/dev/PythonProject01",
```

* Upload
	* Right click on the project name -> SFTP/FTP -> Upload Folder

* Sample code
```
#!/bin/env python
# coding: utf-8
import time
import RPi.GPIO as GPIO

GPIO_LED = 23
GPIO_SW = 17


def initGPIO():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(GPIO_LED, GPIO.OUT)
	GPIO.setup(GPIO_SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def setGPIO(gpio, out):
	if(out == 0):
		GPIO.output(gpio, GPIO.LOW)
	else:
		GPIO.output(gpio, GPIO.HIGH)


if __name__ == "__main__":
	print "Hello World"
	initGPIO()
	while True:
		setGPIO(GPIO_LED, 1)
		time.sleep(0.2)
		setGPIO(GPIO_LED, 0)
		time.sleep(0.2)
		if GPIO.input(GPIO_SW) == 0:
			break
	GPIO.cleanup()
	print "bye"
```