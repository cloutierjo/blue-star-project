#-*- coding: iso-8859-1 -*-

# Classe : DictionnaireDonnee
# Projet : blue-star-project
# Auteur : Jonathan Hall�e

class DictionnaireDonnee(object):
    def __init__(self, vueParent):
        self.frame = Frame()
        
        title = Label(self.frame, text = "Dictionnaire de donn�es")
        title.pack()
        #Euuuh ca s'arr�te la pour l'instant �tant donn�e que j'ai absolumen aucune id�e comment faire pour la tester
        
if __name__ == '__main__':
    pass