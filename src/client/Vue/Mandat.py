#-*- coding: iso-8859-1 -*-
#classe Mandat
#Auteur Pascal Lemay
from Tkinter import*

class Mandat(object):
    def __init__(self,vueParent,mandat):
        self.vueParent=vueParent
        self.mandat=mandat
        
        self.frame = Frame(borderwidth=1, relief="groove")
        
        nom = Label(self.frame,text = 'Mandat :')
        nom.pack()
        s = Scrollbar(self.frame)
    #t->texte mandat
        self.t = Text(self.frame)
        self.t.config(width=74)
        self.t.focus_set()
        s.pack(side=RIGHT, fill=Y)
        self.t.pack(side=LEFT, fill=Y)
        s.config(command=self.t.yview)
        self.t.config(yscrollcommand=s.set)
        
        #si pas de mandat, creation d'un mandat vide
        if self.mandat == None:
            self.t.insert(END,"")
        else:
            self.t.insert(END,self.mandat)
            
        #sauvegarde du mandat
        self.updateMandat()    
        
    def updateMandat(self):
        self.vueParent.parent.creerMandat(self.t.get(1.0,END))