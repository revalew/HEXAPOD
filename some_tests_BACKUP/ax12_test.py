import serial
import time
# import RPi.GPIO as GPIO

# GPIO.setwarnings(False)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)


# port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=3.0)
port = serial.Serial("/dev/ttyUSB0", baudrate=1000000)

while True:
        # GPIO.output(18, GPIO.HIGH)
        port.write(bytearray.fromhex("FF FF 0C 05 03 1E 32 03 A3"))
        time.sleep(0.1)
        # GPIO.output(18, GPIO.LOW)
        time.sleep(3)

        # GPIO.output(18,GPIO.HIGH)
        port.write(bytearray.fromhex("FF FF 0C 05 03 1E CD 00 0b"))
        time.sleep(0.1)
        # GPIO.output(18,GPIO.LOW)
        time.sleep(3)

# import serial
# import time
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)
# GPIO.setwarnings(False)

# port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=3.0)

# while True:
#     GPIO.output(18, GPIO.HIGH)
#     port.write(bytearray.fromhex("FF FF 0E 05 03 20 FF 00 D8"))
#     time.sleep(0.1)
#     GPIO.output(18, GPIO.LOW)
#     time.sleep(3)
