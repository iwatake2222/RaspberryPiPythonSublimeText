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
