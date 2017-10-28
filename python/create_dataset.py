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

image_dataset = []
label_dataset = []

for index, label in enumerate(os.listdir('dataset')):
   
    if label != '.DS_Store':
        data = np.load('dataset/' + label)
        print(data[0][0])
        break;
        # print(data.shape)
        # for d in data:
        #     print(d.shape)

