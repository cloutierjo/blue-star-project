#-*- coding: iso-8859-1 -*-
from  Tix import *
import Tkinter as tk

class PlanningGeneral:
    def __init__(self, frameParent, txtParent, lblText, uneListe=[]):
        #pour deleteRow (retours des Radiobuttons pour deleteRow)
        self.etats=[]

        self.rows = []
        self.grille = txtParent

        if uneListe:
            for i in uneListe:
                ligne=Frame(txtParent)
                etat=IntVar()
                delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False, command=self.deleteRow)
                delRow.var=etat
                self.etats.append(delRow.var)
                delRow.pack(side=LEFT)
                entree = Entry(ligne, relief=RIDGE, width=42)
                entree.insert(END, i[0])
                entree.pack(side=LEFT)
                txtParent.window_create(INSERT, window=ligne)
                self.rows.append(i)
            self.grille.config(state=DISABLED) 
        else:
            self.addRow()
            self.grille.config(state=DISABLED)
        self.boutonAddRow=Button(frameParent,text='Ajouter', command=self.addRow)
        self.boutonAddRow.pack(side=TOP)
        self.boutonAddRow.pack(side=TOP)
        
        #
        #Label(frameParent,text = lblText).pack() 
        
        #self.grille.pack(side=TOP,fill=Y)     
    def addRow(self):
        #nextRow = self.grille.grid_size()[1]
        self.grille.config(state=NORMAL)
        # ligne -> frame avec 3 Entry
        ligne=Frame(self.grille)
        
        etat=IntVar()
        delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
        delRow.var=etat
        self.etats.append(delRow.var)
        delRow.pack(side=LEFT)
        
        entree = Entry(ligne,relief=RIDGE, width=42)
        entree.pack(side=LEFT)
        self.rows.append("")
        self.grille.window_create(INSERT,window=ligne)
        self.grille.config(state=DISABLED)
        
    def deleteRow(self):
        self.grille.config(state=NORMAL)
        i=0;
        while self.etats[i].get()!=1:  #donne l'indice de la row a deleter
            i=i+1
         
        reste=[]   
        for row in self.rows:    #transfert des donnees des rows dans reste
            reste.append(row)
            
        reste.remove(reste[i]) #delete les donnees non voulues
        
        #update  # re-creation de l'analyse avec les donnees restantes
        self.grille.delete(0.0,END)       
        self.etats=[]
        self.rows=[]
        
        for row in reste:
            ligne=Frame(self.grille)
            etat=IntVar()
            delRow=Radiobutton(ligne,text='x',variable=etat,value=1,cursor="arrow",indicatoron=False, command=self.deleteRow)
            delRow.var=etat
            self.etats.append(delRow.var)
            delRow.pack(side=LEFT)
            entree = Entry(ligne, relief=RIDGE, width=42)
            entree.insert(END, row)
            entree.pack(side=LEFT)
            self.rows.append(row)  
            self.grille.window_create(INSERT, window=ligne)
             
        self.grille.config(state=DISABLED)
    def update(self):
        listeTacheGen = []
        for i in self.rows:
            listeTacheGen.append(i.get())