#-*- coding: iso-8859-1 -*-
from Tkinter import *
import tkMessageBox, tkSimpleDialog
class CasUsageVue(object):
    def __init__(self,vueParent):
        self.vueParent = vueParent
        self.frame = Frame(pady=40)
        
        self.lb = Listbox(self.frame, selectmode=SINGLE, height=100, width=40)
        
        self.lb.pack(side=RIGHT, anchor=N)
        self.btnUp= Button(self.frame, text="Monter", width=10, command=self.monter)
        self.btnRen= Button(self.frame, text="Renommer", width=10, command=self.renommer)
        self.btnAdd= Button(self.frame, text="Ajouter", width=10, command=self.ajouter)
        self.btnDel= Button(self.frame, text="Supprimer", width=10, command=self.supprimer)
        self.btnDown= Button(self.frame, text="Descendre", width=10, command=self.descendre)
        self.btnUp.pack()
        self.btnAdd.pack(pady=50)
        self.btnRen.pack()
        self.btnDel.pack(pady=50)
        self.btnDown.pack()
        
        self.remplirListe()
        
        
    def monter(self):
        if self.lb.curselection()[0] != None and int(self.lb.curselection()[0]): # ! (est sélection ou est le premier element)
            indexAMonter = int(self.lb.curselection()[0])
            indexADescendre = indexAMonter-1
            self.vueParent.parent.m.projet.casEtScenario.items
        else:
            tkMessageBox.showwarning("Veuillez sélectionner un élément dans la liste")
        
        self.remplirListe()
        
        
    def descendre(self):
        if self.lb.get(self.lb.curselection()[0])!= None and self.lb.curselection()[0] != self.lb.size()-1: # ! (est sélection ou est le dernier element)
            nomAMonter= self.lb.get(int(self.lb.curselection()[0])+1)
            nomADescendre = self.lb.get(self.lb.curselection()[0])
            self.vueParent.parent.monterPrioriteCas(nomAMonter)
            self.vueParent.parent.descendrePrioriteCas(nomADescendre)
        else:
            tkMessageBox.showwarning("Veuillez sélectionner un élément dans la liste")
        self.remplirListe()
    
    def renommer(self):
        if self.lb.get(self.lb.curselection()[0])!= None:
            nomAncient = self.lb.get(self.lb.curselection()[0])
            nouveauNom = tkSimpleDialog.askstring("Modifier "+nomAncient , "Veuillez entrer un nouveau nom pour Cette Etape "+ nomAncient+" : ")
            if nouveauNom != "":
                self.vueParent.parent.renommerEtapsScenario(int(self.lb.curselection()[0]), nouveauNom)
        else:
            tkMessageBox.showwarning("Veuillez sélectionner un élément dans la liste")    
        
        self.remplirListe()
        
        
    def ajouter(self):
        nouveauNom = tkSimpleDialog.askstring("Ajouter Cas Usage" , "Veuillez entrer un nom pour le nouveau cas d'usage : ")
        if nouveauNom != "":
            self.vueParent.parent.ajouterCasUsage(nouveauNom)
         
        self.remplirListe()
        
        
    def supprimer(self):
          if self.lb.curselection()[0]!= None:
              index = int(self.lb.curselection()[0])
              self.vueParent.parent.supprimerEtapsScenario(index)
          self.remplirListe()
              
              
              
    def remplirListe(self):
        self.lb.delete(0, END)
        for item in self.vueParent.parent.ouvrirScenario():
            self.lb.insert(END,item)
                  
    def updateCasUsage(self):
        return 0
    
    
    
if __name__ == '__main__':
    root = Tk()
    c = CasUsageVue([])
    c.frame.pack()
    root.mainloop()