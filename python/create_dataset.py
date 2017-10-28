import numpy as np
from PIL import Image
import os

image_dataset = []
label_dataset = []


for index, label in enumerate(os.listdir('hiragana73')):
    if label == '.DS_Store':
        continue

    hiragana_dir = 'hiragana73/' + label

    print(label)

    for hiragana_data in os.listdir(hiragana_dir):
        if hiragana_data != '.DS_Store':
            filepath = hiragana_dir + '/' + hiragana_data
            image = np.array(Image.open(filepath).resize((32, 32)))
            if image.size != 3072:
                image_dataset.append(image.astype('float32') / 255.)
                label_dataset.append(index)

np.save('hiragana_labels.npy', np.array(label_dataset))
np.save('hiragana_dataset.npy', np.array(image_dataset))