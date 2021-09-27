import json
import nltk
import pickle
import re
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import  WordNetLemmatizer

class Preprocessing():
    
    @classmethod
    def preprocess_word(cls, word):
        cls.special_characters = r'[^A-Za-zàéèùêôûâïäëç]+'
        cls.stop_words = set(stopwords.words('french','english')) 
        if word == "Aujourd'hui":
            word = word.lower()
        else:
            word = word.lower().replace("'"," ")
        word = re.sub(cls.special_characters, ' ' ,word)
        
        filtered_sentence = []
        word_tokens = word.split(" ")
        
        for w in word_tokens:
            if w not in cls.stop_words  and w != "":
                filtered_sentence.append(w)
        return filtered_sentence

    @classmethod
    def clean_sentences(cls, sentence):
        cls.new_sentence = []
        #je tokenise le pattern et split les mots en array
        cls.sentences_words = nltk.word_tokenize(sentence.item_content)
        for word in cls.sentences_words:
            cls.new_sentence.extend(cls.preprocess_word(word))
        #Je réduis chaque mot à sa forme de base
        cls.lemmatizer = WordNetLemmatizer
        cls.final_sentences_words = [cls.lemmatizer().lemmatize(word.lower()) for word in cls.new_sentence]
        return cls.final_sentences_words

    #Cette fonction va retourner un sac de mot sous forme d'array(0 ou 1 pour les mots existant dans la phrase)
    @classmethod
    def bag_of_words(cls, sentence):
        cls.words_list = cls.read_file("words")
        #Je tokenise les patterns
        cls.sentences_words = cls.clean_sentences(sentence)
        #sac de mots matrice de vocabulaire
        cls.bag = [0]*len(cls.words_list)
        for s in cls.sentences_words:
            for i, words in enumerate(cls.words_list):
                if words == s:
                    #j'assigne 1 si le mot est dans le vocabulaire
                    cls.bag[i] = 1
        return cls.bag

    @classmethod
    def read_file(cls, file_name):
        with open(f'./app/model/ressources/obj/{file_name}.pkl', 'rb') as f:
            return pickle.load(f)
