#-*- coding: iso-8859-1 -*-
from Tkinter import *
import tkMessageBox, tkSimpleDialog
class CasUsageVue(object):
    def __init__(self,vueParent):
        self.vueParent = vueParent
        self.frame = Frame(pady=40)
        
        self.lb = Listbox(self.frame, selectmode=SINGLE)
        '''for item in vueParent.parent.ouvrirCasUsages():
            lb.insert(END,item[0])
            '''
        
        self.lb.pack(side=RIGHT, anchor=N)
        self.btnUp= Button(self.frame, text="Monter", width=10, command=self.monter)
        self.btnRen= Button(self.frame, text="Renommer", width=10, command=self.renommer)
        self.btnAdd= Button(self.frame, text="Ajouter", width=10, command=self.ajouter)
        self.btnDown= Button(self.frame, text="Descendre", width=10, command=self.descendre)
        self.btnUp.pack()
        self.btnAdd.pack(pady=20)
        self.btnRen.pack()
        self.btnDown.pack(pady=20)
        
        self.remplirListe()
        
        
    def monter(self):
        if self.lb.get(self.lb.curselection()[0]): # ! (est sélection ou est le premier element)
            nomAMonter= self.lb.get(self.lb.curselection()[0])
            nomADescendre = self.lb.get(int(self.lb.curselection()[0])-1)
            self.vueParent.parent.monterPrioriteCas(nomAMonter)
            self.vueParent.parent.descendrePrioriteCas(nomADescendre)
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
            nouveauNom = tkSimpleDialog.askstring("Modifier "+nomAncient , "Veuillez entrer un nouveau nom pour le cas d'usage "+ nomAncient+" : ")
            self.vueParent.parent.renommerCasUsage(nomAncient, nouveauNom)
        else:
            tkMessageBox.showwarning("Veuillez sélectionner un élément dans la liste")    
        
        self.remplirListe()
        
        
    def ajouter(self):
        nouveauNom = tkSimpleDialog.askstring("Ajouter Cas Usage" , "Veuillez entrer un nom pour le nouveau cas d'usage : ")
        self.vueParent.parent.m.projet.casEtScenario.addCasUsage(nouveauNom)
        self.remplirListe()
        
    def remplirListe(self):
        self.lb.delete(0, END)
        for item in self.vueParent.parent.ouvrirCasUsages():
            self.lb.insert(END,item[1])         
    def updateCasUsage(self):
        return 0
    
    
    
if __name__ == '__main__':
    root = Tk()
    c = CasUsageVue([])
    c.frame.pack()
    root.mainloop()