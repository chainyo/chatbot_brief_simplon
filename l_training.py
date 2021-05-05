import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import SGD
import random
import pickle
from nltk.stem import WordNetLemmatizer
import tensorflowjs as tfjs
import tensorflow as tf
from l_preprocessing import preprocess_database, create_train_set

def create_model(data_path):

    bag_of_words, classes, documents = preprocess_database(data_path)

    X_train,y_train = create_train_set(documents, bag_of_words, classes)

    model = Sequential()
    model.add(Dense(256, input_shape=(len(X_train[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(y_train[0]), activation='softmax'))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    print(model.summary())

    hist = model.fit(np.array(X_train), np.array(y_train), epochs=500, batch_size=5, verbose=1)
    model.save('l_test/chatbot_modelX.h5', hist)
    try:
        tfjs.converters.save_keras_model(model, "l_test/tfjsmodel")
        print("model crée")
        print(bag_of_words)
        pickle.dump(bag_of_words, open("l_test/bow.pkl", "wb"))
    except:
        print("pb_enregistrement")

data_path = './model/ressources/intents/intents.json'
modelX = create_model(data_path)

print(modelX.summary)
