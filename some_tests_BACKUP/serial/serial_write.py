#!/usr/bin/env python3
import time
import serial

ser = serial.Serial(
        port='/dev/ttyUSB0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
#        baudrate = 1000000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=3
)
counter=0
while 1:
        ser.write(b'Write counter: %d \n'%(counter))
#        time.sleep(3)
        counter += 1
