#-*- coding: iso-8859-1 -*-

# Classe : DictionnaireDonnee
# Projet : blue-star-project
# Auteur : Jonathan Hall�e

from Tkinter import *

class DictionnaireDonnee(object):
    def __init__(self):
    #def __init__(self, vueParent):
        #self.vueParent = vueParent
        self.frame = Frame()
        title = Label(self.frame, text = "Dictionnaire de donn�es")
        title.pack()
        #Euuuh ca s'arr�te la pour l'instant �tant donn�e que j'ai absolument aucune id�e comment faire pour la tester de mon bord
        
if __name__ == '__main__':
    #TESTING DE MA VUE EN LOCAL
    class Vue(object):
        def __init__(self):
            self.root=Tk()
            self.root.title("Blue Star")
            self.root.geometry("1024x768")
    
    v = Vue()
    d = DictionnaireDonnee()
    d.frame.pack()
    
    v.root.mainloop()