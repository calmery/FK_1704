import smbus
import time
import numpy as np
import sys

sample_num = 100
batch = 25
count = 0
arr = []

channel = 1
address = 0x68
bus = smbus.SMBus(channel)
bus.write_i2c_block_data(address, 0x6B, [0x80])
time.sleep(0.1)
bus.write_i2c_block_data(address, 0x6B, [0x00])
time.sleep(0.1)


def main(num):
    global arr
    global count
    x,y,z = [],[],[]
    try:
        while True:
            data = bus.read_i2c_block_data(address, 0x3B ,6)
            
            x_data = (2.0 / float(0x8000)) * (data[0] << 8 | data[1])
            y_data = (2.0 / float(0x8000)) * (data[2] << 8 | data[3])
            z_data = (2.0 / float(0x8000)) * (data[4] << 8 | data[5])
            
            x.append(x_data)
            y.append(y_data)
            z.append(z_data)

            print ("X:%+8.7f" %x_data + " Y:%+8.7f" %y_data + " Z:%8.7f" %z_data)
            
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("==================================================")
        time.sleep(0.3)
        count += 1

        arr.append([x,y,z])
        x,y,z = [],[],[]
        if count < num:
            main(sample_num)
        
        if sample_num % count == batch:
            make_arr(name,count,arr)

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

def make_arr(name,num,arr):
    with open("./tmp/" + name + "_" + num + ".txt", "w") as f:
        f.write(arr)

name = sys.argv[1]
make_dataset(sample_num,name)
