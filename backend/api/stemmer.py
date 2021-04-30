from backend.model.preprocessing import Preprocessing

class Stemmer():

    @classmethod
    def get_stemming(cls, input):
        return Preprocessing.clean_sentences(input)