#-*- coding: iso-8859-1 -*-

# Classe : DictionnaireDonnee
# Projet : blue-star-project
# Auteur : Jonathan Hallée

from Tkinter import *

class DictionnaireDonnee(object):
    def __init__(self, vueParent):
        self.vueParent = vueParent
        self.frame = Frame()
        
        title = Label(self.frame, text = "Dictionnaire de données")
        title.pack()
        
        #self.frame.pack()
        
        d = Donnee(self)
        a = Action(self)

class Donnee(object):
    def __init__(self, vueParent):
        self.vueParent=vueParent
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
           
        scrollbarData.pack(side=RIGHT, fill=Y)
        scrollbarData.config(command=self.textData.yview)
        
        self.textData.pack(side=LEFT)
        self.frameDonnee.pack(side=LEFT)
        
    def addRow(self):
        retour=IntVar()
        self.col = []
        
        # ligne -> frame avec 1 Entry
        self.ligneData=Frame(self.textData)
            
        check=Checkbutton(self.ligneData,variable=retour,cursor="arrow",command=self.gestion)
        check.var=retour
            
        self.retoursData.append(check.var)
            
        check.pack(side=LEFT)
        self.addEntry()
        self.rowsData.append(self.col)
                
        self.textData.window_create(INSERT,window=self.ligneData)
            
    def gestion(self):
        i=0
            # self.retours contient chaque retour associe a chaque checkButton
        for r in self.retoursData:
            #mettre a gere
            if r.get()==1:
                self.rowsData[i][1].delete(0, END) 
                self.rowsData[i][1].insert(END,1)                                  
                                                            
                self.rowsData[i][0].config(state=DISABLED)
            #mettre a non gere
            else:
                self.rowsData[i][0].config(state=NORMAL)
                self.rowsData[i][1].config(state=NORMAL)
                          
                self.rowsData[i][1].delete(0, END)
                self.rowsData[i][1].insert(END,0)
            i+=1
            
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
    def __init__(self, vueParent):
        self.vueParent=vueParent
        self.initMethodes()
        
    def initMethodes(self):
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
            if r.get()==1:
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