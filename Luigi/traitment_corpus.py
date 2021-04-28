import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle

intents_files = open("C:/Users/Shadow/Documents/Chatbot_pour_l_ecole_Microsoft_IA_Brest/chatbot_brief_simplon/Luigi/ressources/intents/intents.json").read()
intents = json.loads(intents_files)
lemmatizer = WordNetLemmatizer

#Traitement du corpus

class traitment_intents():

    def __init__(self):
        
        self.documents = []
        self.words_list = []
        self.classes = []
        self.special_characters = ["!","?",",","."]
    
    #Tokenisation
    def tokenize(self):
        
        for intent in intents["intents"]:
            for pattern in intent["patterns"]:
                self.word = nltk.word_tokenize(pattern)
                self.words_list.extend(self.word)
                
                #la méthode ".extend" extrait les éléments un à un avant de les ajouter à la liste en question
                # démonstration
                # maListe = [1, 2, 3]
                # maListe.append([4, 5])
                # Résulatat:maliste = [1,2,3,[4,5]]
                # maListe.extend([4, 5])
                # Résulatat:maliste = [1,2,3,4,5]
                
                #J'ajoute les docs dans le corpus
                #les documents sont la combinaison entre les patterns et les classes
                self.documents.append((self.word,intent["tag"]))
                #print(intent['tag'])
                if intent["tag"] not in self.classes:#J'ajoute les classes dans ma liste de classe si elle  n'existent pas déjà
                    self.classes.append(intent["tag"])
        #print(self.classes)
        #print(self.documents)
        #print(self.words_list)
        return self.words_list,self.documents,self.classes

######################################################################################################################################################################################################   
    
    #lemmatisation
    def lemmatisation(self):

       self.words_list,self.documents,self.classes = traitment_intents.tokenize(self)
       #Je lemmatise met en minuscule chaque mot et supprime toutes les duplications s'il en ya en remplaçant ces dernières par un mot synonyme
       
       #print(self.words_list)
       self.words_list = [lemmatizer().lemmatize(word.lower()) for word in self.words_list if word not in self.special_characters ]
       self.words_list = sorted(list(set(self.words_list)))
       #print('*'*30)
       print(self.words_list,len(self.words_list))
       #Je trie les classes 
       #print(self.classes)
       self.classes = sorted(list(set(self.classes)))
       print('*'*30)
       print(self.classes,len(self.classes))
       print(self.documents,len(self.documents))

       return self.classes,self.words_list,self.documents
    
######################################################################################################################################################################################################

    def save(self):

        self.classes,self.words_list,self.documments = traitment_intents.lemmatisation(self)
        list_elements = [self.classes,self.words_list,self.documents]
        list_name_save = ["classes","words","documents"]
        i = 0
        for element in list_elements:
            with open(f'C:/Users/Shadow/Documents/Chatbot_pour_l_ecole_Microsoft_IA_Brest/chatbot_brief_simplon/Luigi/ressources/obj/{list_name_save[i]}.pkl', 'wb') as f:
                        pickle.dump(element, f, pickle.HIGHEST_PROTOCOL)
            i += 1
        print("sauvegarde terminée")

    def read_file(file_name):
            
            with open(f'C:/Users/Shadow/Documents/Chatbot_pour_l_ecole_Microsoft_IA_Brest/chatbot_brief_simplon/Luigi/ressources/obj/{file_name}.pkl', 'rb') as f:
                    return pickle.load(f)


    



#traitment_intents().tokenize()
#traitment_intents().lemmatisation()
#traitment_intents().save()
# words = traitment_intents.read_file("words")
# print(words)
# classes = traitment_intents.read_file("classes")
# print(classes)
# documents = traitment_intents.read_file("documents")
# print(documents)




