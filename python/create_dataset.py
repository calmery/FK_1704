# import numpy as np
# from PIL import Image
# import os

# image_dataset = []
# label_dataset = []


# for index, label in enumerate(os.listdir('dataset')):
#     if label == '.DS_Store':
#         continue

#     dataset_dir = 'dataset/' + label

#     print(label)

#     for number_data in os.listdir(dataset_dir):
#         if number_data != '.DS_Store':
#             filepath = dataset_dir + '/' + number_data
#             image = np.array(Image.open(filepath).resize((32, 32)))
#             if image.size != 3072:
#                 image_dataset.append(image.astype('float32') / 255.)
#                 label_dataset.append(index)

# np.save('hiragana_labels.npy', np.array(label_dataset))
# np.save('hiragana_dataset.npy', np.array(image_dataset))

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

# result = np.array([])
result = []
label_dataset = []

arr = []

for index, label in enumerate(os.listdir('dataset')):
   
    if label != '.DS_Store':
        data = np.load('dataset/' + label)
        number = label[0:-4]
        # print(data)
        # break
        for d in data:
            print(len(d[0]))
            print(timesteps-len(d[0]))
            for i in d:
                for j in range(timesteps-len(d[0])):
                    i = np.append(i, 0.0)
                arr.append(i)
            print(arr)
            # d = np.c_[d, np.zeros([3, timesteps-len(d[0])])]
            # d = np.column_stack((d, np.zeros((3, timesteps-len(d[0])))))
            print(d)
            # break

            # result = np.append(result,d)
            result.append(arr)
            label_dataset.append(label_index[number])
            print(label)
        # break

np.save("./numbers.npy", result)
np.save("./label.npy", np.array(label_dataset))

