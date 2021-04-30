import nltk
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords

lemmatizer = WordNetLemmatizer
stop_words = set(stopwords.words('french')) 
special_characters = r'[^A-Za-z0-9àéèùêôûâïäëç]+'

class Preprocessing:

    def preprocess_word(self,word):

            if word == "'Aujourd','hui'":
                word = word.lower()
            else:
                word = word.lower().replace("'"," ")
            word = re.sub(special_characters, ' ' ,word)

            filtered_sentence = []
            word_tokens = word.split(" ")

            for w in word_tokens:
                if w not in stop_words  and w != "":
                    filtered_sentence.append(w)
            return filtered_sentence

    def clean_sentences(self,sentence):

            self.new_sentence = []
            #je tokenise le pattern et split les mots en array
            self.sentences_words = nltk.word_tokenize(sentence)
            for word in self.sentences_words:
                print(word)
                self.new_sentence.extend(self.preprocess_word(word))
            #print(self.sentences_words)
            #Je réduis chaque mot à sa forme de base
            self.final_sentences_words = [lemmatizer().lemmatize(word.lower()) for word in self.new_sentence]
            print(self.final_sentences_words)
            return self.final_sentences_words
