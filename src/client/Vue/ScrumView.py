#-*- coding: iso-8859-1 -*-
'''
Created on 20 mai 2009

@author: Jonatan Cloutier
'''

import sys
sys.path.append( "../../commun" )

import Scrum
from Tkinter import *
import Tix

class ScrumView(object):
    def __init__(self, vueParent, scrumLst):
        self.vueParent = vueParent
        self.frame = Frame()
                
        title = Label(self.frame, text = "Scrum")
        title.pack()
        
        self.d = GridView(self, [])
        self.t = GridView(self, [])
        self.p = GridView(self, [])
        
    def updateListes(self):
        self.done = self.d.getData
        self.todo = self.t.getData
        self.problem = self.p.getData
        
        self.vueParent.parent.updateScrums(self.done, self.todo, self.problem)

class GridView(object):
    def __init__(self, vueParent, data):
        self.vueParent=vueParent
        self.data=data
        self.initDonnee()
        
    def initDonnee(self):
        self.frameDonnee = Frame(self.vueParent.frame)
        self.retoursData=[]
        self.rowsData=[]
        self.etats=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbarData = Scrollbar(self.frameDonnee)
        self.textData = Text(self.frameDonnee, yscrollcommand=scrollbarData.set)
        self.textData.config(width=50, height=10)
        
        ##############################
        if len(self.data) != 0:
            for ligneVariable in self.data:
                col = []
                
                # ligne -> frame avec 2 Entry (grille 1x2)
                ligne=Frame(self.textData)
                
                #pour gestion
                retour=IntVar()
                checkData=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
                checkData.var=retour
                self.retoursData.append(checkData.var)
                
                checkData.pack(side=LEFT)
                
                if ligneVariable[1]==1:
                    checkData.select()
                    gere=True
                else:
                    gere=False
                
                #pour deleteRow 
                etat=IntVar()
                delRow=Radiobutton(ligne,text=u'x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
                delRow.var=etat
                self.etats.append(delRow.var)
                delRow.pack(side=LEFT)
                    
                for j in range(2):
                    entree = Entry(ligne,relief=RIDGE)
                    entree.config(width=35)
                    entree.insert(END,ligneVariable[j])
                    if gere==True:
                        entree.config(state=DISABLED)
                    
                    #ne pack pas le entry qui contient le handled
                    if j<1:
                        entree.pack(side=LEFT)
                    col.append(entree)
                
                self.rowsData.append(col)
                #
                self.textData.window_create(INSERT,window=ligne)
                
            self.textData.config(state=DISABLED)
            #sinon vide
        else:
            self.addRow()
            #self.infoDonnee.config(state=DISABLED)
        
        ##############################
        
        titre=Tix.Label(self.frameDonnee,text=u'Données')
        titre.pack()
        
        self.boutonAddRowData=Button(self.frameDonnee,text=u'Ajouter une ligne',command=self.addRow)
        self.boutonAddRowData.pack()
        
        #self.readDataFromProject()
   
        scrollbarData.pack(side=RIGHT, fill=Y)
        scrollbarData.config(command=self.textData.yview)
        
        self.textData.pack(side=LEFT)
        self.frameDonnee.pack(side=BOTTOM)
        
    def getData(self):
        data = []
        
        for row in self.rowsData:
            col=[]
            col.append(row[0].get())
            col.append(int(row[1].get()))
            data.append(col)
        
        return data
    
    def deleteRow(self):
        self.textData.config(state=NORMAL)
        i=0;
        while self.etats[i].get()!=1:  #donne l'indice de la row a deleter
            i=i+1
         
        reste=[]   
        for row in self.rowsData:    #transfert des donnees des rows dans reste
            col=[]
            for c in range(2):
                col.append(row[c].get())
            col.append(int(row[1].get()))  # int le handled
            reste.append(col)
            
        reste.remove(reste[i]) #delete les donnees non voulues
        
        #update  # re-creation de l'analyse avec les donnees restantes
        self.textData.delete(0.0,END)
        self.retoursData=[]        
        self.etats=[]
        self.rowsData=[]
        
        for row in reste:
            
            col = []
            ligne=Frame(self.textData)
            
            retour=IntVar()
            checkData=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
            checkData.var=retour
            self.retoursData.append(checkData.var)
            checkData.pack(side=LEFT)
            
            if row[2]==1:
                checkData.select()
                gere=True
            else:
                gere=False
               
            etat=IntVar()
            delRow=Radiobutton(ligne,text=u'x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
            delRow.var=etat
            self.etats.append(delRow.var)
            delRow.pack(side=LEFT)
            
            for j in range(2):
                    entree = Entry(ligne,relief=RIDGE)
                    entree.config(width = 50)
                    entree.insert(END,row[j])
                    if gere==True:
                        entree.config(state=DISABLED)
                    #ne pack pas le entry qui contient le handled
                    if j<1:
                        entree.pack(side=LEFT)
                    col.append(entree)
                
            self.rowsData.append(col)   
                
            self.textData.window_create(INSERT,window=ligne)
            
        self.textData.config(state=DISABLED)
                 
    def addRow(self):
        retour=IntVar()
        self.col = []
        
        # ligne -> frame avec 1 Entry
        ligneData=Frame(self.textData)
            
        checkData=Checkbutton(ligneData,variable=retour,cursor="arrow",command=self.gestion)
        checkData.var=retour
            
        self.retoursData.append(checkData.var)
            
        checkData.pack(side=LEFT)
        
        etat=IntVar()
        delRow=Radiobutton(ligneData,text=u'x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
        delRow.var=etat
        self.etats.append(delRow.var)
        delRow.pack(side=LEFT)
        
        for j in range(2) :# Création des deux entrées de ma ligne
            entree = Entry(ligneData,relief=RIDGE)
            entree.config(width=50)
                
            if j < 1:
                entree.pack(side=LEFT)
            else:
                # si < 3 = le handled : 0 par defaut (pas packé)
                entree.insert(END,0)
            self.col.append(entree)
            
        #self.addEntry()
        self.rowsData.append(self.col)
                
        self.textData.window_create(INSERT,window=ligneData)
        
    def gestion(self):
        self.textData.config(state=NORMAL)
        i=0
            # self.retours contient chaque retour associe a chaque checkButton
        for r in self.retoursData:
            #mettre a gere
            if r.get()==1:
                
                self.rowsData[i][1].delete(0, END) 
                self.rowsData[i][1].insert(END,1)                                  
                                                    
                self.rowsData[i][0].config(state=DISABLED)
                self.rowsData[i][1].config(state=DISABLED)
                  
            #mettre a non gere
            else:
                self.rowsData[i][0].config(state=NORMAL)
                self.rowsData[i][1].config(state=NORMAL)
                                                     #le entry du handle mis a normal pour sauvegarde
                                                    #sinon delete et insert ne fonctionne pas
                
                
                self.rowsData[i][1].delete(0, END)
                self.rowsData[i][1].insert(END,0)
            i+=1
            
        self.textData.config(state=DISABLED)
            

if __name__ == '__main__':
    
    scl=Scrum.ScrumList()
    
    sc=Scrum.Scrum()
    
    sc.date="19 mai"
    sc.user="moi"
    sc.done.append(["fais1",0])
    sc.done.append(["fais2",0])
    sc.todo.append(["afaire1",0])
    sc.todo.append(["afaire2",0])
    sc.probleme.append(["prob1",0])
    sc.probleme.append(["prob2",0])
    
    scl.scrums.append(sc)
    
    sc=Scrum.Scrum()
    
    sc.date="20 mai"
    sc.user="s01"
    sc.done.append(["bfais1",0])
    sc.done.append(["bfais2",0])
    sc.todo.append(["bafaire1",0])
    sc.todo.append(["bafaire2",0])
    sc.probleme.append(["bprob1",0])
    sc.probleme.append(["bprob2",0])
    
    scl.scrums.append(sc)
    
    root = Tk()
    c = ScrumView(None,scl)
    c.frame.pack()
    root.mainloop()