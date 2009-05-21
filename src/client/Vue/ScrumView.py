#-*- coding: iso-8859-1 -*-
'''
Created on 20 mai 2009

@author: Jonatan Cloutier
'''

import sys
sys.path.append( "../../commun" )

import Scrum
from Tkinter import *

class ScrumView(object):
    def __init__(self, vueParent, done, todo, problem):
        self.vueParent = vueParent
        self.frame = Frame()
        
        self.done = done
        self.todo = todo
        self.problem = problem
        
        title = Label(self.frame, text = "Scrum")
        title.pack()
        
        self.d = Donnee(self, self.done)
        self.t = Action(self, self.todo)
        self.p = Action(self, self.problem)
        
    def updateListes(self):
        self.done = self.d.getData
        self.todo = self.t.getData
        self.problem = self.p.getData
        
        self.vueParent.parent.updateScrums(self.done, self.todo, self.problem)

class GridView(object):
    def __init__(self, vueParent, variables):
        self.vueParent=vueParent
        self.data=variables
        self.initDonnee()
        
    def initDonnee(self):
        self.frameDonnee = Frame(self.vueParent.frame)
        self.retoursData=[]
        self.rowsData=[]
        self.etats=[]
        
        #Ajout du tableau C'est un textbox avec des entr�e en grille 1x1
        scrollbarData = Scrollbar(self.frameDonnee)
        self.textData = Text(self.frameDonnee, yscrollcommand=scrollbarData.set)
        self.textData.config(width=30, height=60)
        
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
                delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
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
            self.infoDonnee.config(state=DISABLED)
        
        ##############################
        
        Label(self.frameDonnee,text = 'Donn�es').pack()
        
        self.boutonAddRowData=Button(self.frameDonnee,text='Ajouter une ligne',command=self.addRow)
        self.boutonAddRowData.pack()
        
        #self.readDataFromProject()
   
        scrollbarData.pack(side=RIGHT, fill=Y)
        scrollbarData.config(command=self.textData.yview)
        
        self.textData.pack(side=LEFT)
        self.frameDonnee.pack(side=LEFT)
        
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
            delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
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
        delRow=Radiobutton(ligneData,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
        delRow.var=etat
        self.etats.append(delRow.var)
        delRow.pack(side=LEFT)
        
        for j in range(2) :# Cr�ation des deux entr�es de ma ligne
            entree = Entry(ligneData,relief=RIDGE)
            entree.config(width=50)
                
            if j < 1:
                entree.pack(side=LEFT)
            else:
                # si < 3 = le handled : 0 par defaut (pas pack�)
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
            
