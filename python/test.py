# from keras.models import Sequential
# from keras.layers import Dense, Activation
import numpy as np
# from keras.utils import np_utils
import matplotlib.pylab as plt
import PIL



# digits = datasets.load_digits()  
# features = digits.data
# targets = digits.target

# データセット読み込み
image_dataset = np.load('hiragana_dataset.npy')
label_dataset = np.load('hiragana_labels.npy')


a = np.array(image_dataset[6000])

print(label_dataset[6000])
plt.imshow(a)
plt.show()