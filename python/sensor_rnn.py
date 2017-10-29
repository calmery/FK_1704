from keras.models import Sequential
from keras.layers import LSTM, Dense, GRU, Activation
import numpy as np
from keras.utils import np_utils

def main():
    x_train = np.load('numbers.npy')
    y_train = np_utils.to_categorical(np.load('label.npy'), num_classes=10)

    model = Sequential()
    model.add(LSTM(32, return_sequences=True,
                input_shape=(3000, 400)))
    model.add(LSTM(32, return_sequences=True)) 
    # model.add(LSTM(32)) 
    # model.add(Dense(10, activation='softmax'))
    model.add(LSTM(32, return_sequences=True)) 
    model.add(LSTM(10, activation='softmax')) 


    model.compile(loss='categorical_crossentropy',
                optimizer='Adam',
                metrics=['accuracy'])

    model.fit(x_train, y_train,
            batch_size=32, epochs=20)

    model.save('specal_pen_model.h5')


def test():
    x_train = np.load('numbers_test.npy')
    y_train = np_utils.to_categorical(np.load('label_test.npy'), num_classes=10)

    print(x_train.shape)

    model = Sequential()
    model.add(LSTM(32, return_sequences=True,
                input_shape=(150, 140)))
    model.add(LSTM(64, return_sequences=True)) 
    model.add(LSTM(32)) 
    model.add(Dense(10, activation='softmax'))
    # model.add(LSTM(32, return_sequences=True)) 
    # model.add(LSTM(10, activation='softmax')) 


    model.compile(loss='categorical_crossentropy',
                optimizer='Adam',
                metrics=['accuracy'])

    model.fit(x_train, y_train,
            batch_size=25, epochs=30)

    model.save('specal_pen_test_model.h5')

if __name__ == '__main__':
    test()
    # main()