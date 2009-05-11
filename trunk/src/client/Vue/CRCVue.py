#-*- coding: iso-8859-1 -*-
from Tkinter import *

class CRC(object):
    def __init__(self,parent):
        self.parent = parent
        self.frame = Frame()        
        
        self.frameNom = Frame(self.frame)#########################################
        
        self.titreClass = Label(self.frameNom,text="Nom du Classe")
        self.titreClass.pack(side=LEFT)
        
        self.entree = Entry(self.frameNom,width=40)
        self.entree.pack()

        
        self.frameInfo = Frame(self.frame)##############################################
        
        self.titreInfo = Label(self.frameInfo,text="Données et Fonctions")
        self.titreInfo.pack()
        
        self.infoDonnee = Text(self.frameInfo, width=40, height=20)    
        self.scrollbarInfo = Scrollbar(self.frameInfo)
        self.scrollbarInfo.pack(side=RIGHT, fill=Y)
        self.infoDonnee.pack(side=LEFT, fill=Y)
        self.scrollbarInfo.config(command=self.infoDonnee.yview)
        self.infoDonnee.config(yscrollcommand=self.scrollbarInfo.set)
        

        self.frameCollabo = Frame(self.frame)############################################
        
        self.titreCollabo = Label(self.frameCollabo,text="Les collaborateurs")
        self.titreCollabo.pack()
        
        self.collaboration = Text(self.frameCollabo, width=40, height=22)
        self.scrollbarCol=Scrollbar(self.frameCollabo)
        self.scrollbarCol.pack(side=RIGHT, fill=Y)
        self.collaboration.pack(side=LEFT, fill=Y)
        self.scrollbarCol.config(command=self.collaboration.yview)
        self.collaboration.config(yscrollcommand=self.scrollbarCol.set)
   

        self.frameNom.grid(padx=20,pady=10,row=1,column=1)
        self.frameInfo.grid(row=2,column=1)
        self.frameCollabo.grid(padx =20,pady=10,row=1,rowspan=4,column=3)