import smbus
import time
import numpy as np
import sys

sample_num = 10
channel = 1
address = 0x68
bus = smbus.SMBus(channel)

bus.write_i2c_block_data(address, 0x6B, [0x80])
time.sleep(0.1)

bus.write_i2c_block_data(address, 0x6B, [0x00])
time.sleep(0.1)
arr = []
count = 0
def main(num):
    global arr
    global count
    try:
        while True:
            data = bus.read_i2c_block_data(address, 0x3B ,6)
            
            x = (2.0 / float(0x8000)) * (data[0] << 8 | data[1])
            y = (2.0 / float(0x8000)) * (data[2] << 8 | data[3])
            z = (2.0 / float(0x8000)) * (data[4] << 8 | data[5])

            arr.append([x,y,z])

            print ("X:%+8.7f" %x + " Y:%+8.7f" %y + " Z:%8.7f" %z)
            
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("==================================================")
        time.sleep(0.2)
        count += 1
        if count < num:
            main(sample_num)
        return arr

#list -> numpy arrray
def convert(arr):
    data = np.array(arr)
    return data

arr = main(sample_num)
data = convert(arr)

#save dataset
def make_dataset(num,variety):
    for i in range(num):
        np.save("./dataset/" + variety + ".npy", data)


name = sys.argv[1]
make_dataset(sample_num,name)
