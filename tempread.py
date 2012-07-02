# -*- coding:utf-8 -*-

#That code use the Temperature_Sense_Demo original project

import serial #pyserial module

port=raw_input("Which port ? ")

ser = serial.Serial(port,2400)

while(1):
	fahrenheit = ord(ser.read())
	celsius = (fahrenheit-32)*5./9.
	print "temperature : ",fahrenheit,"°F = ",celsius," °C"
