#-*- coding: iso-8859-1 -*-
from  Tix import *
import Tkinter as tk

class PlanningGeneral:
    def __init__(self, frameParent, txtParent, lblText, uneListe=[]):
        #pour deleteRow (retours des Radiobuttons pour deleteRow)
        self.etats=[]
        self.retours=[]
        self.rows = []
        self.grille = txtParent

        if uneListe:
            for i in uneListe:
                col=[]
                ligne=Frame(txtParent)
                
                valeur=IntVar()
                checkHandled=Checkbutton(ligne,variable=valeur,cursor="arrow",command=self.gestion)
                checkHandled.var=valeur
                checkHandled.pack(side=LEFT)
                self.retours.append(checkHandled.var)
                
                etat=IntVar()
                delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False, command=self.deleteRow)
                delRow.var=etat
                self.etats.append(delRow.var)
                delRow.pack(side=LEFT)
                
                entree = Entry(ligne, relief=RIDGE, width=42)
                entree.insert(END, i[0])
                entree.pack(side=LEFT)
                col.append(entree)
                entreeH = Entry(ligne, relief=RIDGE, width=42)
                if int(i[1])==0:
                    entreeH.insert(END,0)
                else:
                    entreeH.insert(END,1)
                    checkHandled.select()
                    entree.config(state=DISABLED)
                col.append(entreeH)
                self.rows.append(col)
                self.grille.window_create(INSERT, window=ligne)
            txtParent.config(state=DISABLED) 
        else:
            self.addRow()
            self.grille.config(state=DISABLED)
        self.boutonAddRow=Button(frameParent,text=u'Ajouter', command=self.addRow)
        self.boutonAddRow.pack(side=TOP, anchor=W, padx =130)
        Label(frameParent,text = ""+lblText).pack(side=RIGHT)
            
    def addRow(self):
        #nextRow = self.grille.grid_size()[1]
        self.grille.config(state=NORMAL)
        # ligne -> frame
        ligne=Frame(self.grille)
        
        valeur=IntVar()
        checkHandled=Checkbutton(ligne,variable=valeur,cursor="arrow",command=self.gestion)
        checkHandled.var=valeur
        checkHandled.pack(side=LEFT)
        self.retours.append(checkHandled.var)
        
        etat=IntVar()
        delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
        delRow.var=etat
        self.etats.append(delRow.var)
        delRow.pack(side=LEFT)
        col=[]
        entree = Entry(ligne,relief=RIDGE, width=42)
        entree.pack(side=LEFT)
        col.append(entree)
        entreeH=Entry(ligne,relief=RIDGE, width=42)
        entreeH.insert(END,0)
        col.append(entreeH)
        self.rows.append(col)
        self.grille.window_create(INSERT,window=ligne)
        self.grille.config(state=DISABLED)
        
    def deleteRow(self):
        self.grille.config(state=NORMAL)
        i=0;
        while self.etats[i].get()!=1:  #donne l'indice de la row a deleter
            i=i+1
        self.rows.remove(self.rows[i])#delete les donnees non voulues 
        
        tempo=[]# transfert ici pour pas perdre les données dans grilleDelete...
        for row in self.rows:
            t=[]
            t.append(row[0].get())
            t.append(row[1].get())
            tempo.append(t)
        
        #update  # re-creation  avec les donnees du tempo
        self.grille.delete(0.0,END)      
        self.etats=[]
        self.retours=[]
        self.rows=[]
        
        for r in tempo:
            col=[]
            ligne=Frame(self.grille)
            
            valeur=IntVar()
            checkHandled=Checkbutton(ligne,variable=valeur,cursor="arrow",command=self.gestion)
            checkHandled.var=valeur
            self.retours.append(checkHandled.var)
            checkHandled.pack(side=LEFT)
            
            etat=IntVar()
            delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False, command=self.deleteRow)
            delRow.var=etat
            self.etats.append(delRow.var)
            delRow.pack(side=LEFT)
            
            entree = Entry(ligne, relief=RIDGE, width=42)
            entree.insert(END, r[0])
            entree.pack(side=LEFT)
            col.append(entree)
            entreeH = Entry(ligne, relief=RIDGE, width=42)
            entreeH.insert(END,r[1])
            if int(r[1])==1:
                checkHandled.select()
                entree.config(state=DISABLED)

            col.append(entreeH)
            self.rows.append(col)  
            self.grille.window_create(INSERT, window=ligne)
             
        self.grille.config(state=DISABLED)
        
        
    def update(self):
        listeTacheGen = []
        for i in self.rows:
            listeTacheGen.append([i[0].get(),i[1].get()])
        
        return listeTacheGen
    
    def gestion(self):
        self.grille.config(state=NORMAL)
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
            
        self.grille.config(state=DISABLED)
        