import nltk
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords

lemmatizer = WordNetLemmatizer
stop_words = set(stopwords.words('french')) 
special_characters = r'[^A-Za-z0-9àéèùêôûâïäëç]+'

class Preprocessing:

    @classmethod
    def preprocess_word(cls, word):

            if word == "Aujourd'hui":
                word = word.lower()
            else:
                word = word.lower().replace("'"," ")
            word = re.sub(special_characters, ' ' ,word)

            cls.filtered_sentence = []
            cls.word_tokens = word.split(" ")

            for w in cls.word_tokens:
                if w not in stop_words  and w != "":
                    cls.filtered_sentence.append(w)
            return cls.filtered_sentence

    @classmethod
    def clean_sentences(cls, sentence):

        cls.new_sentence = []

        cls.sentences_words = nltk.word_tokenize(sentence)
        for word in cls.sentences_words:
            cls.new_sentence.extend(cls.preprocess_word(word))
        cls.final_sentences_words = [lemmatizer().lemmatize(word.lower()) for word in cls.new_sentence]
        return cls.final_sentences_words
