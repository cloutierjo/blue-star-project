#-*- coding: iso-8859-1 -*-

# Classe : DictionnaireDonnee
# Projet : blue-star-project
# Auteur : Jonathan Hallée

import sys

sys.path.append( "../../commun" )

from DictDonne import *
from Tkinter import *

class DictionnaireDonnee(object):
    def __init__(self, vueParent, variables, fonctions):
        self.vueParent = vueParent
        self.frame = Frame()
        
        self.variables = variables
        self.fonctions = fonctions
        
        title = Label(self.frame, text = "Dictionnaire de données")
        title.pack()
        
        d = Donnee(self, self.variables)
        a = Action(self, self.fonctions)
        
    def updateDictionnaire(self):
        listeDic = []
        
        for row in d.rowsData:
            dic = {}
            dic['Donnee']=row[0].get()
            
        listeDic.append(dic)
        
        for row in a.rows:
            dicAc = {}
            dicAc['Actions']=row[0].get()
        
        listeDic.append(dicAc)

class Donnee(object):
    def __init__(self, vueParent, variables):
        self.vueParent=vueParent
        self.variables=variables
        self.initDonnee()
        
    def initDonnee(self):
        self.frameDonnee = Frame(self.vueParent.frame)
        self.retoursData=[]
        self.rowsData=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbarData = Scrollbar(self.frameDonnee)
        self.textData = Text(self.frameDonnee, yscrollcommand=scrollbarData.set)
        self.textData.config(width=30, height=60)
        
        Label(self.frameDonnee,text = 'Données').pack()
        
        self.boutonAddRowData=Button(self.frameDonnee,text='Ajouter une ligne',command=self.addRow)
        self.boutonAddRowData.pack()
        
        self.readDataFromProject()
   
        scrollbarData.pack(side=RIGHT, fill=Y)
        scrollbarData.config(command=self.textData.yview)
        
        self.textData.pack(side=LEFT)
        self.frameDonnee.pack(side=LEFT)
        
    def readDataFromProject(self):
        if len(self.variables) != 0:
            for ligneVariable in self.variables:       
                ligne=Frame(self.textData)
                
                #self.rowsData.append(ligneVariable[0])
                
                retour = ligneVariable[1]
                checkData=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
                checkData.var=retour
                
                self.retoursData.append(checkData.var)
                checkData.pack(side=LEFT)
                
                entree=Entry(ligne,relief=RIDGE)
                entree.insert(END,ligneVariable[0])
                entree.insert(END,ligneVariable[1])
                
                if ligneVariable[1] == 1:
                    checkData.select()
                    entree.config(state=DISABLED)
                    gere=True
                else:
                    gere=False

                entree.pack(side=LEFT)
                
                #entrer les ligneVariable ???
                self.rowsData.append([ligneVariable[0], ligneVariable[1]])
                
                self.textData.window_create(INSERT,window=ligne)
                 
    def addRow(self):
        retour=IntVar()
        self.col = []
        
        # ligne -> frame avec 1 Entry
        self.ligneData=Frame(self.textData)
            
        checkData=Checkbutton(self.ligneData,variable=retour,cursor="arrow",command=self.gestion)
        checkData.var=retour
            
        self.retoursData.append(checkData.var)
            
        checkData.pack(side=LEFT)
        self.addEntry()
        self.rowsData.append(self.col)
                
        self.textData.window_create(INSERT,window=self.ligneData)
            
    def gestion(self):
        
        i = 0
        
        for r in self.retoursData:
            if r == 0:
                self.rowsData[i][1] = 1
                self.retoursData[i] = 1
            else:
                self.rowsData[i][1] = 0
                self.retoursData[i] = 0
            
            i+=1
        
        self.readDataFromTemp()
    
    def readDataFromTemp(self):
        #self.textData.delete(0, END)
        
        if len(self.rowsData) != 0:
            for row in self.rowsData:       
                ligne=Frame(self.textData)
                
                #self.rowsData.append(ligneVariable[0])
                
                retour = self.rowsData[1]
                checkData=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
                checkData.var=retour
                
                checkData.pack(side=LEFT)
                
                entree=Entry(ligne,relief=RIDGE)
                entree.insert(END,row[0])
                entree.insert(END,row[1])
                
                print row[1]
                
                if row[1] == 1:
                    checkData.select()
                    entree.config(state=DISABLED)
                    gere=True
                else:
                    gere=False

                entree.pack(side=LEFT)
                
                #entrer les ligneVariable ???               
                self.textData.window_create(INSERT,window=ligne)
                
    def addEntry(self):
        for j in range(2) :# Création des deux entrées de ma ligne
            entree = Entry(self.ligneData,relief=RIDGE)
            entree.config(width=50)
                
            if j < 1:
                entree.pack(side=LEFT)
            else:
                # si < 3 = le handled : 0 par defaut (pas packé)
                entree.insert(END,0)
            self.col.append(entree)
            
class Action(object):
    def __init__(self, vueParent, fonctions):
        self.vueParent=vueParent
        self.fonctions=fonctions
        self.initActions()
        
    def initActions(self):
        self.frameMethodes = Frame(self.vueParent.frame)
        self.retours=[]
        self.rows=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbar = Scrollbar(self.frameMethodes)
        self.text = Text(self.frameMethodes, yscrollcommand=scrollbar.set)
        self.text.config(width=30, height=60)
        
        Label(self.frameMethodes,text = 'Actions').pack()
         
        self.boutonAddRow=Button(self.frameMethodes,text='Ajouter une action',command=self.addRow)
        self.boutonAddRow.pack()
        
        if(len(self.fonctions)) != 0:
           for ligneFonction in self.fonctions:          
               ligne=Frame(self.text)
                
               #self.rowsData.append(ligneVariable[0])
                
               retour = ligneFonction[1]
               check=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
               check.var=retour
                
               self.retours.append(check.var) 
               check.pack(side=LEFT)
               
               entree=Entry(ligne,relief=RIDGE)
               entree.insert(END,ligneFonction[0])
               entree.insert(END,ligneFonction[1])
                
               if ligneFonction[1] == 1:
                   check.select()
                   entree.config(state=DISABLED)
                   gere=True
               else:
                   gere=False

               entree.pack(side=LEFT)
                
               #entrer les ligneVariable ???
               self.rows.append([ligneFonction[0], ligneFonction[1]])
               self.text.window_create(INSERT,window=ligne)
               
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text.yview)
        
        self.text.pack(side=LEFT)
        self.frameMethodes.pack(side=RIGHT)
        
    def addRow(self):
        retour=IntVar()
        self.col = []
        
        # ligne -> frame avec 1 Entry
        self.ligne=Frame(self.text)
            
        check=Checkbutton(self.ligne,variable=retour,cursor="arrow",command=self.gestion)
        check.var=retour
            
        self.retours.append(check.var)
            
        check.pack(side=LEFT)
        self.addEntry()
        self.rows.append(self.col)
                
        self.text.window_create(INSERT,window=self.ligne)
        
    def gestion(self):
        i=0
            # self.retours contient chaque retour associe a chaque checkButton
        for r in self.retours:
            #mettre a gere
            if r == 1:
                self.rows[i][1].delete(0, END) 
                self.rows[i][1].insert(END,1)                                  
                                                            
                self.rows[i][0].config(state=DISABLED)
            #mettre a non gere
            else:
                self.rows[i][0].config(state=NORMAL)
                self.rows[i][1].config(state=NORMAL)
                          
                self.rows[i][1].delete(0, END)
                self.rows[i][1].insert(END,0)
            i+=1
             
    def addEntry(self):
        for j in range(2) :# Création des deux entrées de ma ligne
            entree = Entry(self.ligne,relief=RIDGE)
            entree.config(width=50)
                
            if j < 1:
                entree.pack(side=LEFT)
            else:
                # si < 3 = le handled : 0 par defaut (pas packé)
                entree.insert(END,0)
            self.col.append(entree)