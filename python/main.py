from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.optimizers import Adam
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.utils import np_utils
import numpy as np

# データセット読み込み
image_dataset = np.load('hiragana_dataset.npy')
label_dataset = np.load('hiragana_labels.npy')

print(image_dataset.shape)
print(label_dataset.shape)

# データ整形
image_dataset = image_dataset.reshape(image_dataset.shape[0], 32, 32, 1)

# ラベルデータ
Y = np_utils.to_categorical(label_dataset, num_classes=74)

# モデル定義
model = Sequential()

# レイヤー
model.add(Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 1)))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(74))
model.add(Activation('softmax'))

# 最適化アルゴリズム
opt = Adam(lr=0.0001, decay=1e-6)

model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# 学習実行。10%はテストに使用。
model.fit(image_dataset, Y, epochs=200, batch_size=100, validation_split=0.1, shuffle=True)

model.save('hiragana_model.h5')