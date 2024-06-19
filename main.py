import serial
import time


ser = serial.Serial('COM3', 9600, timeout=1)  

time.sleep(2)  

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line + "cm")
except KeyboardInterrupt:
    print("Exit program.")
finally:
    ser.close()
