from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

data_dim = 16
timesteps = 8
num_classes = 10

# 想定する入力データshape: (batch_size, timesteps, data_dim)
model = Sequential()
model.add(LSTM(32, return_sequences=True,
               input_shape=(timesteps, data_dim)))  # 32次元のベクトルのsequenceを出力する
model.add(LSTM(32, return_sequences=True)) # 32次元のベクトルのsequenceを出力する
model.add(LSTM(32))  # 32次元のベクトルを一つ出力する
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# 疑似訓練データを生成する
x_train = np.random.random((1000, timesteps, data_dim))
y_train = np.random.random((1000, num_classes))

# 疑似検証データを生成する
x_val = np.random.random((100, timesteps, data_dim))
y_val = np.random.random((100, num_classes))

model.fit(x_train, y_train,
          batch_size=64, epochs=200,
          validation_data=(x_val, y_val))