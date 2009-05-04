#-*- coding: iso-8859-1 -*-
from Tkinter import *
import tkMessageBox, tkSimpleDialog
class CasUsage(object):
    def __init__(self,vueParent):
        self.vueParent = vueParent
        self.frame = Frame()
        
        self.lb = Listbox(self.frame, selectmode=SINGLE)
        '''for item in vueParent.parent.ouvrirCasUsages():
            lb.insert(END,item[0])
            '''
        self.lb.insert(END,"1")
        self.lb.insert(END,"2")
        self.lb.insert(END,"3")
        
        self.lb.pack(side=RIGHT)
        self.btnUp= Button(self.frame, text="Monter", width=10, command=self.monter)
        self.btnRen= Button(self.frame, text="Renommer", width=10)
        self.btnDown= Button(self.frame, text="Descendre", width=10)
        self.btnUp.pack(side=TOP)
        self.btnDown.pack(side=BOTTOM)
        
        
        
    def monter(self):
        if self.lb.get(self.lb.curselection()[0]): # ! (est sélection ou est le premier element)
            nomAMonter= self.lb.get(curselection()[0])
            nomADescendre = self.lb.get(curselection()[0]-1)
            self.vueParent.parent.monterPrioriteCas(nomAMonter)
            self.vueParent.parent.descendrePrioriteCas(nomADescendre)
        else:
            tkMessageBox.showwarning("Veuillez sélectionner un élément dans la liste")
        
        self.remplirListe()
        
        
    def descendre(self):
        if self.lb.get(self.lb.curselection()[0])!= None and curselection()[0] != self.lb.size()-1: # ! (est sélection ou est le dernier element)
            nomAMonter= self.lb.get(curselection()[0]+1)
            nomADescendre = self.lb.get(curselection()[0])
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
        
        
        
    def remplirListe(self):
        for item in vueParent.parent.ouvrirCasUsages():
            lb.insert(END,item[0] + " - "  + item[1])         
    def updateCasUsage(self):
        return 0
    
    
    
if __name__ == '__main__':
    root = Tk()
    c = CasUsage([])
    c.frame.pack()
    root.mainloop()