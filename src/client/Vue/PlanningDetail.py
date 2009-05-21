#-*- coding: iso-8859-1 -*-
from  Tix import *
import Tkinter as tk

class PlanningDetail:

 #Debut Detaill�#
    def __init__(self,uneListeDeListe):
        self.frameDetail = Frame()       
        #pour gestion (retours des Checkbuttons pour "handled")
        self.retours=[]
        #pour deleteRow (retours des Radiobuttons pour deleteRow)
        self.etats=[]

        self.rows = []
        
        scrollbar = Scrollbar(self.frameDetail)
        
        self.grille = Text(self.frameDetail, width=52, height=35, yscrollcommand=scrollbar.set)  #
        if True: 
                for i in uneListeDeListe:
                    col = []
                    ligne=Frame(self.grille)
                    
                    #pour gestion
                    retour=IntVar()
                    check=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
                    check.var=retour
                    self.retours.append(check.var)
                    
                    check.pack(side=LEFT)
                    
                    #pour deleteRow 
                    etat=IntVar()
                    delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
                    delRow.var=etat
                    self.etats.append(delRow.var)
                    delRow.pack(side=LEFT)
                    for j in i:
                        entree = Entry(ligne,relief=RIDGE)
                        entree.insert(END,j)
                        if j< 4:
                            entree.pack(side=LEFT)
                        col.append(entree)
                    self.rows.append(col)
                    
                    #
                    self.grille.window_create(INSERT,window=ligne)
                self.grille.config(state=DISABLED)
                    #sinon vide
        else:
            self.addRow()
            self.grille.config(state=DISABLED)
    
    

        self.boutonAddRow=Button(self.frameDetail,text='Ajouter',command=self.addRow)
        self.boutonAddRow.pack()
        Label(self.frameDetail,text = "Taches   -  Priorit� -  User").pack()
    
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.grille.yview)
        self.grille.pack(side=TOP,fill=Y)
 
        
    def addRow(self):
        #nextRow = self.grille.grid_size()[1]
        self.grille.config(state=NORMAL)
        col = []
        # ligne -> frame avec 3 Entry
        ligne=Frame(self.grille)
        retour=IntVar()
        check=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
        check.var=retour
        self.retours.append(check.var)
        check.pack(side=LEFT)
        
        etat=IntVar()
        delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
        delRow.var=etat
        self.etats.append(delRow.var)
        delRow.pack(side=LEFT)
        
        for j in range(4) :# Utilisation d'une entr
            entree = Entry(ligne,relief=RIDGE)
            if j < 3:
                entree.pack(side=LEFT)
            else:
                # si < 3 = le handled : 0 par defaut (pas pack�)
                entree.insert(END,0)
            col.append(entree)
        self.rows.append(col)
        #
        self.grille.window_create(INSERT,window=ligne)
        self.grille.config(state=DISABLED)
        
    def gestion(self):
        self.grille.config(state=NORMAL)
        i=0
            # self.retours contient chaque retour associe a chaque checkButton
        for r in self.retours:
            #mettre a gere
            if r.get()==1:
                self.rows[i][3].delete(0, END) 
                self.rows[i][3].insert(END,1)                                  
                                                    
                self.rows[i][0].config(state=DISABLED)
                self.rows[i][1].config(state=DISABLED)
                self.rows[i][2].config(state=DISABLED)
                
            #mettre a non gere
            else:
                self.rows[i][0].config(state=NORMAL)
                self.rows[i][1].config(state=NORMAL)
                self.rows[i][2].config(state=NORMAL)
                self.rows[i][3].config(state=NORMAL) #le entry du handle mis a normal pour sauvegarde
                                                    #sinon delete et insert ne fonctionne pas
                
                
                self.rows[i][3].delete(0, END)
                self.rows[i][3].insert(END,0)
            i+=1
            
        self.grille.config(state=DISABLED)
            
            
            
    def deleteRow(self):
        self.grille.config(state=NORMAL)
        i=0;
        while self.etats[i].get()!=1:  #donne l'indice de la row a deleter
            i=i+1
         
        reste=[]   
        for row in self.rows:    #transfert des donnees des rows dans reste
            col=[]
            for c in range(3):
                col.append(row[c].get())
            col.append(int(row[3].get()))  # int le handled
            reste.append(col)
            
        reste.remove(reste[i]) #delete les donnees non voulues
        
        #update  # re-creation de l'analyse avec les donnees restantes
        self.grille.delete(0.0,END)
        self.retours=[]        
        self.etats=[]
        self.rows=[]
        
        for row in reste:
            
            col = []
            ligne=Frame(self.grille)
            
            retour=IntVar()
            check=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
            check.var=retour
            self.retours.append(check.var)
            check.pack(side=LEFT)
            
            if row[3]==1:
                check.select()
                gere=True
            else:
                gere=False
               
            etat=IntVar()
            delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
            delRow.var=etat
            self.etats.append(delRow.var)
            delRow.pack(side=LEFT)
            
            for j in range(4):
                    entree = Entry(ligne,relief=RIDGE)
                    entree.insert(END,row[j])
                    if gere==True:
                        entree.config(state=DISABLED)
                    #ne pack pas le entry qui contient le handled
                    if j<3:
                        entree.pack(side=LEFT)
                    col.append(entree)
                
            self.rows.append(col)   
                
            self.grille.window_create(INSERT,window=ligne)
            
        self.grille.config(state=DISABLED)
         