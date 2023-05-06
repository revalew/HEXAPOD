#!/usr/bin/env python3
import time
import serial

ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 9600,
#        baudrate = 1000000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=3
)
while 1:
        x=ser.readline()
#        time.sleep(1)
        print(x)
