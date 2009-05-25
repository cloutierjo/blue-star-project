#-*- coding: iso-8859-1 -*-
from Tkinter import *
import tkMessageBox, tkSimpleDialog
class ScenarioVue(object):
    def __init__(self,vueParent):
        self.vueParent = vueParent
        self.frame = Frame(pady=5,borderwidth=2, relief="groove")
        label=Label(self.frame,text=u"Sc�nario d'utilisation")
        label.pack()
        self.lb = Listbox(self.frame, selectmode=SINGLE,width=40,height=20)#height=100
        
        self.scroll = Scrollbar(self.frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.scroll.config(command=self.lb.yview)
        self.lb.config(yscrollcommand=self.scroll.set)
        
        self.lb.pack(side=RIGHT, anchor=N)
        self.btnUp= Button(self.frame, text=u"Monter", width=10, command=self.monter)
        self.btnRen= Button(self.frame, text=u"Renommer", width=10, command=self.renommer)
        self.btnAdd= Button(self.frame, text=u"Ajouter", width=10, command=self.ajouter)
        self.btnDel= Button(self.frame, text=u"Supprimer", width=10, command=self.supprimer)
        self.btnDown= Button(self.frame, text=u"Descendre", width=10, command=self.descendre)
        self.btnUp.pack()
        self.btnAdd.pack(pady=10)
        self.btnRen.pack()
        self.btnDel.pack(pady=10)
        self.btnDown.pack()
        
        self.remplirListe()
        
        
    def monter(self):
        if self.lb.curselection()[0] != None and int(self.lb.curselection()[0]): # ! (est s�lection ou est le premier element)
            indexAMonter = int(self.lb.curselection()[0])
            self.vueParent.parent.monterEtapeScenario(indexAMonter)
        else:
            tkMessageBox.showwarning(u"Veuillez s�lectionner un �l�ment dans la liste diff�rent du Premier")
        
        self.remplirListe()
        
        
    def descendre(self):
        if self.lb.get(self.lb.curselection()[0])!= None and int(self.lb.curselection()[0]) != self.lb.size()-1: # ! (est s�lection ou est le dernier element)
            indexADescendre = int(self.lb.curselection()[0])
            self.vueParent.parent.descendreEtapeScenario(indexADescendre)
        else:
            tkMessageBox.showwarning(u"Selection Invalide", u"Veuillez s�lectionner un �l�ment dans la liste diff�rent du Dernier")
        self.remplirListe()
    
    def renommer(self):
        if self.lb.get(self.lb.curselection()[0])!= None:
            nomAncient = self.lb.get(self.lb.curselection()[0])
            nouveauNom = tkSimpleDialog.askstring(u"Modifier "+nomAncient , u"Veuillez entrer un nouveau nom pour Cette Etape "+ nomAncient+" : ")
            if nouveauNom != "":
                self.vueParent.parent.renommerEtapsScenario(int(self.lb.curselection()[0]), nouveauNom)
        else:
            tkMessageBox.showwarning(u"Selection Invalide", u"Veuillez s�lectionner un �l�ment dans la liste")    
        
        self.remplirListe()
        
        
    def ajouter(self):
        nouveauNom = tkSimpleDialog.askstring(u"Ajouter Cas Usage" , u"Veuillez entrer un nom pour le nouveau cas d'usage : ")
        if nouveauNom != "":
            self.vueParent.parent.ajouterEtapeScenario(nouveauNom)
         
        self.remplirListe()
        
        
    def supprimer(self):
          if self.lb.curselection()[0]!= None:
              index = int(self.lb.curselection()[0])
              self.vueParent.parent.supprimerEtapsScenario(index)
          self.remplirListe()
              
              
              
    def remplirListe(self, evt = None):
        self.lb.delete(0, END)
        if self.vueParent.casUsage:
            if self.vueParent.parent.ouvrirScenario():
                for item in self.vueParent.parent.ouvrirScenario():
                    self.lb.insert(END,item)
                  
    def updateCasUsage(self):
        return 0
    
    
    
if __name__ == '__main__':
    root = Tk()
    c = CasUsageVue([])
    c.frame.pack()
    root.mainloop()