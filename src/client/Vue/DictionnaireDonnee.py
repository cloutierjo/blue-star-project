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
        
        self.d = Donnee(self, self.variables)
        self.a = Action(self, self.fonctions)
        
    def updateListes(self):
        self.variables = []
        
        for row in self.d.rowsData:
            col=[]
            col.append(row[0].get())
            col.append(int(row[1].get()))
            self.variables.append(col)
            
        self.fonctions = []
        
        for row in self.a.rows:
            col=[]
            col.append(row[0].get())
            col.append(int(row[1].get()))
            self.fonctions.append(col)
        
        self.vueParent.parent.updateDictionnaireDonnee(self.variables, self.fonctions)

class Donnee(object):
    def __init__(self, vueParent, variables):
        self.vueParent=vueParent
        self.variables=variables
        self.initDonnee()
        
    def initDonnee(self):
        self.frameDonnee = Frame(self.vueParent.frame)
        self.retoursData=[]
        self.rowsData=[]
        self.etats=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbarData = Scrollbar(self.frameDonnee)
        self.textData = Text(self.frameDonnee, yscrollcommand=scrollbarData.set)
        self.textData.config(width=30, height=60)
        
        ##############################
        if len(self.variables) != 0:
            for ligneVariable in self.variables:
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
            self.textData.config(state=DISABLED)
        
        ##############################
        
        Label(self.frameDonnee,text = 'Données').pack()
        
        self.boutonAddRowData=Button(self.frameDonnee,text='Ajouter une ligne',command=self.addRow)
        self.boutonAddRowData.pack()
        
        #self.readDataFromProject()
   
        scrollbarData.pack(side=RIGHT, fill=Y)
        scrollbarData.config(command=self.textData.yview)
        
        self.textData.pack(side=LEFT)
        self.frameDonnee.pack(side=LEFT)
        
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
            
class Action(object):
    def __init__(self, vueParent, fonctions):
        self.vueParent=vueParent
        self.fonctions=fonctions
        self.initActions()
        
    def initActions(self):
        self.frameMethodes = Frame(self.vueParent.frame)
        self.retours=[]
        self.rows=[]
        self.etats=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbar = Scrollbar(self.frameMethodes)
        self.text = Text(self.frameMethodes, yscrollcommand=scrollbar.set)
        self.text.config(width=30, height=60)
        
        Label(self.frameMethodes,text = 'Actions').pack()
         
        self.boutonAddRow=Button(self.frameMethodes,text='Ajouter une action',command=self.addRow)
        self.boutonAddRow.pack()
        
        if len(self.fonctions) != 0:
            for ligneFonctions in self.fonctions:
                col = []
                
                # ligne -> frame avec 2 Entry (grille 1x2)
                ligne=Frame(self.text)
                
                #pour gestion
                retour=IntVar()
                check=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
                check.var=retour
                self.retours.append(check.var)
                
                check.pack(side=LEFT)
                
                if ligneFonctions[1]==1:
                    check.select()
                    gere=True
                else:
                    gere=False
                
                #pour deleteRow 
                etat=IntVar()
                self.delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
                self.delRow.var=etat
                self.etats.append(self.delRow.var)
                self.delRow.pack(side=LEFT)
                    
                for j in range(2):
                    entree = Entry(ligne,relief=RIDGE)
                    entree.config(width=35)
                    entree.insert(END,ligneFonctions[j])
                    if gere==True:
                        entree.config(state=DISABLED)
                    
                    #ne pack pas le entry qui contient le handled
                    if j<1:
                        entree.pack(side=LEFT)
                    col.append(entree)
                
                self.rows.append(col)
                #
                self.text.window_create(INSERT,window=ligne)
                
            self.text.config(state=DISABLED)
            #sinon vide
        else:
            self.addRow()
            self.text.config(state=DISABLED)
               
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text.yview)
        
        self.text.pack(side=LEFT)
        self.frameMethodes.pack(side=RIGHT)
        
    def deleteRow(self):
        self.text.config(state=NORMAL)
        i=0;
        while self.etats[i].get()!=1:  #donne l'indice de la row a deleter
            i=i+1
         
        reste=[]   
        for row in self.rows:    #transfert des donnees des rows dans reste
            col=[]
            for c in range(2):
                col.append(row[c].get())
            col.append(int(row[1].get()))  # int le handled
            reste.append(col)
            
        reste.remove(reste[i]) #delete les donnees non voulues
        
        #update  # re-creation de l'analyse avec les donnees restantes
        self.text.delete(0.0,END)
        self.retours=[]        
        self.etats=[]
        self.rows=[]
        
        for row in reste: 
            col = []
            ligne=Frame(self.text)
            
            retour=IntVar()
            check=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
            check.var=retour
            self.retours.append(check.var)
            check.pack(side=LEFT)
            
            if row[2]==1:
                check.select()
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
                
            self.rows.append(col)   
                
            self.text.window_create(INSERT,window=ligne)
            
        self.text.config(state=DISABLED)
        
    def addRow(self):
        retour=IntVar()
        self.col = []
        
        # ligne -> frame avec 1 Entry
        ligne=Frame(self.text)
            
        check=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
        check.var=retour
            
        self.retours.append(check.var)
            
        check.pack(side=LEFT)
        
        etat=IntVar()
        delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
        delRow.var=etat
        self.etats.append(delRow.var)
        delRow.pack(side=LEFT)
        
        for j in range(2) :# Création des deux entrées de ma ligne
            entree = Entry(ligne,relief=RIDGE)
            entree.config(width=50)
                
            if j < 1:
                entree.pack(side=LEFT)
            else:
                # si < 3 = le handled : 0 par defaut (pas packé)
                entree.insert(END,0)
            self.col.append(entree)
            
        #self.addEntry()
        self.rows.append(self.col)
                
        self.text.window_create(INSERT,window=ligne)
        
    def gestion(self):
        self.text.config(state=NORMAL)
        i=0
            # self.retours contient chaque retour associe a chaque checkButton
        for r in self.retours:
            #mettre a gere
            if r.get()==1:
                
                self.rows[i][1].delete(0, END) 
                self.rows[i][1].insert(END,1)                                  
                                                    
                self.rows[i][0].config(state=DISABLED)
                self.rows[i][1].config(state=DISABLED)
                  
            #mettre a non gere
            else:
                self.rows[i][0].config(state=NORMAL)
                self.rows[i][1].config(state=NORMAL)
                                                     #le entry du handle mis a normal pour sauvegarde
                                                    #sinon delete et insert ne fonctionne pas
                
                self.rows[i][1].delete(0, END)
                self.rows[i][1].insert(END,0)
            i+=1
            
        self.text.config(state=DISABLED)