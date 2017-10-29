import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

label_index = {
    'zero' : 0,
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
}

timesteps = 140
result = []
label_dataset = []

for index, label in enumerate(os.listdir('dataset')):
   
    if label != '.DS_Store':
        data = np.load('dataset/' + label)

        number = label[0:-4]
        for d in data:
            for i in range(timesteps-len(d)):
                d.append([0.0,0.0,0.0])
            result.append(d)

            label_dataset.append(label_index[number])

np.save("./numbers_test.npy", np.array(result))
np.save("./label_test.npy", np.array(label_dataset))

