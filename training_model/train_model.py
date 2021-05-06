import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout
from keras.optimizers import SGD
import random
from nltk.stem import WordNetLemmatizer
import tensorflowjs as tfjs
import tensorflow as tf
from traitment_corpus import traitment_intents

class training ():

    def __init__(self):
        

            self.classes = traitment_intents().read_file("classes")
            self.words_list = traitment_intents().read_file("words")
            self.documents = traitment_intents().read_file("documents")
            self.lemmatizer = WordNetLemmatizer
            self.training = []#on s'en servira pour le training
            self.output_empty = [0]*len(self.classes)#je crèe un array vide pour la sortie
            


    def create_data_training(self):
        
        dico_classes = {}
        dico = {}
        for doc in self.documents: 
            #j'initialise les sacs de mots pour chaque phrases
            self.bag = []
            
            #ici ça sera la liste des mots "tokeneisés" pour les patterns
            self.pattern_words = doc[0]  
            #le fait de lemmatiser chaque mot créer un mot de base pour tenter de représenter un mot apparenté
            # self.pattern_words = [self.lemmatizer().lemmatize(word.lower()) for word in self.pattern_words]
            #je crèe mon array de sac de mots avec 1, si un mot est trouvé dans le pattern en cours
            for word in self.words_list:
                self.bag.append(1) if word in self.pattern_words else self.bag.append(0)
            #la sortie est à 0 pour chaque classe/tag et 1 pour la classe en cours pour chaque pattern
            output_row = list(self.output_empty)
            # print(output_row)
            # print("doc1",doc[1])
            # print("self.classe",self.classes.index(doc[1]))
            output_row[self.classes.index(doc[1])] = 1
            print("self.classe",self.classes.index(doc[1]))
            print(doc[1])
            dico = {self.classes.index(doc[1]):doc[1]}
            for key, value in dico.items():
                if key or value not in dico_classes:
                     dico_classes.update(dico)
            self.training.append([self.bag,output_row])
        #je mélange ensuite mon training et le convertie en array
        random.shuffle(self.training)
        self.training = np.array(self.training)
        #je splite ensuite mon train  
        self.X_train = list(self.training[:,0])#correspond à mes patterns
        self.y_train = list(self.training[:,1])#correspond à mes intents
        print("Dataset d'entraînement crée")
        print(len(self.X_train[0]),len(self.y_train[0]))
        print(dico_classes)
        dico_classes = sorted(dico_classes)
        print(dico_classes)
        return self.X_train,self.y_train



    def create_model(self):

        self.X_train,self.y_train = training().create_data_training()
        
        #je crèe mon model avec  - 3 layers. le 1er avec 256 neurons, le second avec 128 neurons et le  3ème layer a un nombre de neurons
        # égale au nombre d'intents à prédire 
        model = Sequential()
        model.add(Dense(256, input_shape=(len(self.X_train[0]),), activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(len(self.y_train[0]), activation='softmax'))

        # Je Compile le modèle. Stochastic gradient descent avec Nesterov accelerated gradient donne de bons resultats pour ce model
        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

        #Je fit et save le modèle
        hist = model.fit(np.array(self.X_train), np.array(self.y_train), validation_split=0.2,epochs=500, batch_size=5, verbose=1)
        model.save('C:/Users/Shadow/Documents/final_chat_bot/chatbot_brief_simplon/backend/app/model/model/chatbot_model.h5', hist)
        tfjs.converters.save_keras_model(model, "C:/Users/Shadow/Documents/final_chat_bot/chatbot_brief_simplon/backend/app/model/tfjsmodel")

        print("model crée")



    

#training().create_data_training()
training().create_model()  
