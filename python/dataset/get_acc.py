import smbus
import time
import numpy as np
import sys

sample_num = 10
batch = 25
count = 0
arr = []
name = sys.argv[1]

#use_connet_sensor
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
    d = []
    try:
        while True:
            data = bus.read_i2c_block_data(address, 0x3B ,6)
            
            x_data = (2.0 / float(0x8000)) * (data[0] << 8 | data[1])
            y_data = (2.0 / float(0x8000)) * (data[2] << 8 | data[3])
            z_data = (2.0 / float(0x8000)) * (data[4] << 8 | data[5])
            
            d.append([x_data,y_data,z_data])

            print ("X:%+8.7f" %x_data + " Y:%+8.7f" %y_data + " Z:%8.7f" %z_data)
            
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("================================================")
        print("=                    "+str(count + 1)  +"                  = ")        
        print("==================================================")
        time.sleep(0.3)
        count += 1

        arr.append(d)

        d = []
        
        f = open("test.txt","w")
        f.write(str(arr))
        
        if count < num:
            main(sample_num)
        
        if count == 50:
            f.close()

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
        np.save('./dataset/' + variety + '.npy', data)

#def make_arr(arr):
#    with open('data.txt', 'w') as f:
#        f.write(arr)

make_dataset(sample_num,name)
