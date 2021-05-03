import json
import nltk
import pickle
import re

from nltk.corpus import stopwords
from nltk.stem import  WordNetLemmatizer

    
class Preprocessing():
    
    @classmethod
    def preprocess_word(cls, word):
        cls.special_characters = r'[^A-Za-z0-9àéèùêôûâïäëç]+'
        cls.stop_words = set(stopwords.words('french','english')) 
        if word == "'Aujourd','hui'":
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
        cls.sentences_words = nltk.word_tokenize(sentence)
        for word in cls.sentences_words:
            cls.new_sentence.extend(cls.preprocess_word(word))
        #Je réduis chaque mot à sa forme de base
        cls.lemmatizer = WordNetLemmatizer
        cls.final_sentences_words = [cls.lemmatizer().lemmatize(word.lower()) for word in cls.new_sentence]
        return cls.final_sentences_words

    #Cette fonction va retourner un sac de mot sous forme d'array(0 ou 1 pour les mots existant dans la phrase)
    @classmethod
    def bag_of_words(cls, sentence):
        cls.words_list = read_file("words")
        #Je tokenise les patterns
        cls.sentences_words = cls.clean_sentences(sentence)
        #sac de mots matrice de vocabulaire
        bag = [0]*len(words_list)
        for sentence in self.sentences_words:
            for i, words in enumerate(cls.words_list):
                if words == sentence:
                    #j'assigne 1 si le mot est dans le vocabulaire
                    bag[i] = 1
        return(np.array(bag))

    @classmethod
    def read_file(file_name):
        with open(f'./app/model/ressources/obj/{file_name}.pkl', 'rb') as f:
            return pickle.load(f)

    # def predict(self,sentence):
    #     #seuil de prediction
    #     p = bot.bag_of_words(self,sentence,words_list,show_details=False)
    #     print(p.shape)
    #     res = model.predict(np.array([p]))[0]
    #     ERROR_THRESHOLD = 0.2
    #     results = [[i,r] for i,r in enumerate(res) if r> ERROR_THRESHOLD]
    #     #probabilité de force de tri
    #     results.sort(key=lambda x: x[1],reverse=True)
    #     return_list = []
    #     [return_list.append({"intents":classes[r[0]], "probabilty":str([r[1]])}) for r in results]
    #     return return_list

    # def get_reponse(self,ints):

    #     tag = ints[0]['intents']
    #     list_of_intents = intents_files['intents']
    #     for i in list_of_intents:
    #         if(i['tag'] == tag):
    #             result = random.choice(i['responses'])
    #             print(ints)
    #             print("classe correspondante:",tag)
    #             print(result)
    #             break
    #     return result
