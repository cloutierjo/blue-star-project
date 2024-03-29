#-*- coding: iso-8859-1 -*-
from Tkinter import *
import tkMessageBox, tkSimpleDialog
class CasUsageVue(object):
    def __init__(self,vueParent):
        self.vueParent = vueParent
        self.frame = Frame(pady=5,borderwidth=2, relief="groove")
        self.DerniereSelection = None
        self.lb = Listbox(self.frame, selectmode=SINGLE,width=40,height=20)#height=100
        '''for item in vueParent.parent.ouvrirCasUsages():
            lb.insert(END,item[0])
            '''
        self.scroll = Scrollbar(self.frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.scroll.config(command=self.lb.yview)
        self.lb.config(yscrollcommand=self.scroll.set)
        
        label=Label(self.frame,text=u"Cas d'usage")
        label.pack()
        self.lb.pack(side=RIGHT, anchor=N)
        self.btnUp= Button(self.frame, text=u"Monter", width=10, command=self.monter)
        self.btnRen= Button(self.frame, text=u"Renommer", width=10, command=self.renommer)
        self.btnAdd= Button(self.frame, text=u"Ajouter", width=10, command=self.ajouter)
        self.btnDel= Button(self.frame, text=u"Supprimer", width=10, command=self.supprimer)
        self.btnDown= Button(self.frame, text=u"Descendre", width=10, command=self.descendre)
        self.btnUp.pack()
        #self.btnAdd.pack(pady=50)
        self.btnAdd.pack(pady=10)
        self.btnRen.pack()
        #self.btnDel.pack(pady=50)
        self.btnDel.pack(pady=10)
        self.btnDown.pack()
        
        self.lb.bind("<ButtonRelease-1>", self.updateScenarioAssocie)
        
        self.remplirListe()
        
        
    def monter(self):
        if self.lb.get(self.lb.curselection()[0]): # ! (est s�lection ou est le premier element)
            nomAMonter= self.lb.get(self.lb.curselection()[0])
            nomADescendre = self.lb.get(int(self.lb.curselection()[0])-1)
            self.vueParent.parent.monterPrioriteCas(nomAMonter)
            self.vueParent.parent.descendrePrioriteCas(nomADescendre)
        else:
            tkMessageBox.showwarning(u"Veuillez s�lectionner un �l�ment dans la liste")
        
        self.remplirListe()
        
        
    def descendre(self):
        if self.lb.get(self.lb.curselection()[0])!= None and self.lb.curselection()[0] != self.lb.size()-1: # ! (est s�lection ou est le dernier element)
            nomAMonter= self.lb.get(int(self.lb.curselection()[0])+1)
            nomADescendre = self.lb.get(self.lb.curselection()[0])
            self.vueParent.parent.monterPrioriteCas(nomAMonter)
            self.vueParent.parent.descendrePrioriteCas(nomADescendre)
        else:
            tkMessageBox.showwarning(u"Veuillez s�lectionner un �l�ment dans la liste")
        self.remplirListe()
    
    def renommer(self):
        if self.lb.get(self.lb.curselection()[0])!= None:
            nomAncient = self.lb.get(self.lb.curselection()[0])
            nouveauNom = tkSimpleDialog.askstring(unicode("Modifier "+nomAncient) , unicode("Veuillez entrer un nouveau nom pour le cas d'usage "+ nomAncient+" : "))
            if nouveauNom != "":
                self.vueParent.parent.renommerCasUsage(nomAncient, nouveauNom)
        else:
            tkMessageBox.showwarning(u"Veuillez s�lectionner un �l�ment dans la liste")    
        
        self.remplirListe()
        
        
    def ajouter(self):
        nouveauNom = tkSimpleDialog.askstring(u"Ajouter Cas Usage" , u"Veuillez entrer un nom pour le nouveau cas d'usage : ")
        if nouveauNom:
            retour = self.vueParent.parent.ajouterCasUsage(nouveauNom)
            if not retour:
                tkMessageBox.showwarning(u"Impossible d'ajouter le cas d'usage v�rifier si un autre cas d'usage n'a pas le m�me nom") 
            self.remplirListe()
        
        
    def supprimer(self):
          if self.lb.get(self.lb.curselection()[0])!= None:
              nomSuppr = self.lb.get(self.lb.curselection()[0])
              index = int(self.lb.curselection()[0])
              for i in range(index+1,self.lb.size()):
                   self.vueParent.parent.monterPrioriteCas(self.lb.get(i))
              self.vueParent.parent.supprimerCasUsage(nomSuppr)
          self.remplirListe()
              
              
              
    def remplirListe(self):
        self.lb.delete(0, END)
        for item in self.vueParent.parent.ouvrirCasUsages():
            self.lb.insert(END,item[1])   
     
    def updateScenarioAssocie(self,evt=None):
        self.DerniereSelection = self.lb.get(self.lb.curselection()[0])
        self.vueParent.scenario.remplirListe()             
    def updateCasUsage(self):
        return 0
    
    
    
if __name__ == '__main__':
    root = Tk()
    c = CasUsageVue([])
    c.frame.pack()
    root.mainloop()