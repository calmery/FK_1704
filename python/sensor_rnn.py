from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

data_dim = 3
timesteps = 140
num_classes = 10

x_train = np.load('numbers.npy')
y_train = np.load('label.npy')

print(x_train.shape)
model = Sequential()
model.add(LSTM(30, return_sequences=True,
               input_shape=(None, timesteps, 3)))
model.add(LSTM(30, return_sequences=True)) 
model.add(LSTM(30)) 
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=2, epochs=20)