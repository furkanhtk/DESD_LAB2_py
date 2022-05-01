import time

import serial



serialPort = serial.Serial(port="COM2", baudrate=9600, bytesize=8, timeout=None, stopbits=serial.STOPBITS_ONE)

while True:
    average = serialPort.read(24)
    average_int1 = int(average[0:8], 2)
    average_int2 = int(average[8:16], 2)
    average_int3 = int(average[16:24], 2)
    # print("int1:{} int2:{} int3:{}".format(average[0:8], average[8:16], average[16:24]))
    print("int1:{} int2:{} int3:{}".format(average_int1, average_int2, average_int3))
    average_int = int((average_int1 + average_int2 + average_int3) / 3)
    average_int = format(average_int, '08b')
    serialPort.write(str.encode(average_int))




