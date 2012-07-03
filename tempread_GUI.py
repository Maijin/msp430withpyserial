# -*- coding:utf-8 -*- 

#That code uses the Temperature_Sense_Demo original project

from Tkinter import *
import tkSimpleDialog
import time

try:
    import serial
except ImportError:
    raise ImportError, 'This program recquires the pyserial module. See http://pyserial.sourceforge.net/pyserial.html'


class App (object):
    def __init__(self):
        self.root=Tk()
        self.variable=StringVar()
        self.temperature=0
        self.your_label=Label(self.root,textvariable=self.variable)
        self.port=tkSimpleDialog.askstring(title="Port",prompt="Which Port ?")
        self.ser=0
    def grid(self):
        self.your_label.pack()
    def update_label(self):
        self.ser=serial.Serial(self.port,2400)
        self.temperature=(ord(self.ser.read())-32)*5./9.
        self.variable.set("Température : " + str(self.temperature) + " °C")
        self.root.after(20,self.update_label)
    def run(self):
        self.grid()
        self.root.after(20,self.update_label)
        self.root.mainloop()

if __name__=='__main__':
    App().run()