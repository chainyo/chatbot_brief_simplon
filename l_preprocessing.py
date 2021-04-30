import nltk
nltk.download('punkt')
from nltk.stem.snowball import FrenchStemmer
stemmer = FrenchStemmer(ignore_stopwords=False)
import re

import numpy as np
import tensorflow as tf
import random
import json
import pickle


ignore_words = ['la', 'le', 'ce', 'du', 'de', 'sa', 'une', 'un', 'on']

def preprocess_database(json_path):
    words = []
    classes = []
    documents = []
    with open(json_path) as f:
        intents = json.load(f)
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern = re.sub(r'[^\w\s]', ' ', pattern)
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            documents.append((w, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])


    words = [stemmer.stem(w.lower()) for w in words if len(w)>1]
    words = [w for w in words if w not in ignore_words]
    words = sorted(list(set(words)))

    classes = sorted(list(set(classes)))

    print (len(documents), "documents") #liste de tupples
    print (len(classes), "classes", classes)
    print (len(words), "unique stemmed words", words)
    return words, classes, documents

def process_sentence(input, bow):
    words = []
    sentence = re.sub(r'[^\w\s]', ' ', input)
    w = nltk.word_tokenize(sentence)
    words.extend(w)
    words = [stemmer.stem(w.lower()) for w in words if len(w)>1]
    words = [w for w in words if w not in ignore_words]
    print(words)

    vector = []
    for w in bow:
        vector.append(1) if w in words else vector.append(0)

    return vector

def create_train_set(documents, words, classes):
    training = []
    output = []
    output_empty = [0] * len(classes)
    #bow
    for doc in documents:
        bag = []
        pattern_words = doc[0]
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words if len(word)>1]
        pattern_words = [word for word in pattern_words if word not in ignore_words]
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])

    random.shuffle(training)

    x_train = []
    y_train = []
    for i in range(len(documents)):
        x_train.append(training[i][0])
        y_train.append(training[i][1])

    x_train = np.asarray(x_train)
    y_train = np.asarray(y_train)
    return x_train, y_train



"""
data_path = './model/ressources/intents/intents.json'
maphrase = "actuel être évaluées salut puis-je avoir un coup de main svp ?"

bag_of_words, classes, documents = preprocess_database(data_path)

out = process_sentence(maphrase, bag_of_words)
print(out)
"""