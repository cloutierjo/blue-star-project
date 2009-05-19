#-*- coding: iso-8859-1 -*-
from Tkinter import*
import tkMessageBox, tkSimpleDialog
class ListeProjets(object):
#fenetre affichant les projets existants
    def __init__(self,data,parent):
        self.fen=Toplevel()
        self.parent = parent
        self.data = data
        self.fen.title("Projets")
        self.fen.resizable(False,False)
        #fenetre reste devant fenetre principale
        self.fen.grab_set()
        self.fen.focus_set()
        
        self.scroll = Scrollbar(self.fen)
        self.scroll.pack(side=RIGHT, fill=Y)
        
        self.maliste=Liste(self.fen,data=data,width=25,height=3)
        self.maliste.pack()
        
        self.scroll.config(command=self.maliste.yview)
        self.maliste.config(yscrollcommand=self.scroll.set)
        
        self.choix=Entry(self.fen,width=40)
        self.choix.pack()
        self.b = Button(self.fen,text="   OK   ",command=self.choisirProjet)
        self.b.pack()
    def choisirProjet(self):
        if self.maliste.getData() != None:
            self.parent.parent.ouvrirProjet(self.data[self.maliste.getData()][0])
            #projet ouvert
            self.parent.etat=1
            self.parent.filemenu.entryconfig(6,state=NORMAL)
            #affichage des onglets
            self.parent.onglets.frame.pack()
            self.parent.chargerEnMemoireProjet()
            #nom du projet dans le titre de la fenetre
            self.parent.root.title("Blue Star        "+self.parent.parent.m.projet.nom)
            self.fen.destroy()
        else:
            tkMessageBox.showwarning(
            "Echec d'ouverture",
            "impossible d'ouvrir le projet")
            #print "impossible d'ouvrir le projet"
        
#----------------------------------------------------------------------------
class Liste(Listbox):
    #liste des projets existants
    def __init__(self,parent,data=[],width=20,height=1):
        Listbox.__init__(self,parent,width=40)#,parent,width,height)
        self.fillListe(data)
        
    def fillListe(self,data):
        for i in data:
            self.insert(END,i[1])
            
    def getData(self,evt=0):
        ca=self.curselection()
        if ca:
            return int(ca[0])
      