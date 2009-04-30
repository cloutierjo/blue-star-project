#-*- coding: iso-8859-1 -*-

# Classe : DictionnaireDonnee
# Projet : blue-star-project
# Auteur : Jonathan Hallée

class DictionnaireDonnee(object):
    def __init__(self, vueParent):
        self.frame = Frame()
        
        title = Label(self.frame, text = "Dictionnaire de données")
        title.pack()
        #Euuuh ca s'arrête la pour l'instant étant donnée que j'ai absolumen aucune idée comment faire pour la tester
        
if __name__ == '__main__':
    pass