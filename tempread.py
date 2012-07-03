# -*- coding:utf-8 -*-

#That code uses the Temperature_Sense_Demo original project

try:
    import serial
except ImportError:
    raise ImportError, 'This program recquires the pyserial module. See http://pyserial.sourceforge.net/pyserial.html'


port=raw_input("Which port ? ")

ser = serial.Serial(port,2400)

while(1):
	fahrenheit = ord(ser.read())
	celsius = (fahrenheit-32)*5./9.
	print "temperature : ",fahrenheit,"°F = ",celsius," °C"
