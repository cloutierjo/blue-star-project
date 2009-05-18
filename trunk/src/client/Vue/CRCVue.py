#-*- coding: iso-8859-1 -*-
from Tkinter import *
import Tix

class CrcVUE(object):
    def __init__(self,vueParent,listeDeCRC):
        self.vueParent=vueParent
        self.listeDeCRC=listeDeCRC
        self.crcCourant=None # objet crc qui est affiché et qui provient du projet

        self.rows=[]
        self.retours=[]
        self.etats=[]
        
        self.frame = Frame()        
        
        self.frameNom = Frame(self.frame)#########################################
        self.entreeProp = Entry(self.frameNom,width=40)
        self.varcombo = Tix.StringVar()
        self.comboClasse=Tix.ComboBox(self.frameNom,label='Classe:',editable=0,variable=self.varcombo,dropdown=1,command=self.getCrc,options='listbox.width 30')
        self.comboClasse.pack()
        
        for crc in listeDeCRC:  #load la liste des crc du projet dans le combobox
            self.comboClasse.insert(END,crc)
            
        titreProp = Label(self.frameNom,text="Propriétaire")
        titreProp.pack()
        
        self.entreeProp.pack()

        
        self.frameInfo = Frame(self.frame)##############################################
        
        titreInfo = Label(self.frameInfo,text="Données et Fonctions")
        titreInfo.pack()
        self.boutonAddRow=Button(self.frameInfo,text='+',command=self.addRow)
        self.boutonAddRow.pack()
        
        self.infoDonnee = Text(self.frameInfo, width=30,height=30)#height=20    
        self.scrollbarInfo = Scrollbar(self.frameInfo)
        self.scrollbarInfo.pack(side=RIGHT, fill=Y)
        self.infoDonnee.pack(side=LEFT, fill=Y)
        self.scrollbarInfo.config(command=self.infoDonnee.yview)
        self.infoDonnee.config(yscrollcommand=self.scrollbarInfo.set)
        

        self.frameCollabo = Frame(self.frame)############################################
        
        self.titreCollabo = Label(self.frameCollabo,text="Les collaborateurs")
        self.titreCollabo.pack()
        
        self.collaboration = Text(self.frameCollabo, width=30,height=35)#height=22
        self.scrollbarCol=Scrollbar(self.frameCollabo)
        self.scrollbarCol.pack(side=RIGHT, fill=Y)
        self.collaboration.pack(side=LEFT, fill=Y)
        self.scrollbarCol.config(command=self.collaboration.yview)
        self.collaboration.config(yscrollcommand=self.scrollbarCol.set)
   

        self.frameNom.grid(padx=20,pady=10,row=1,column=1)
        self.frameInfo.grid(row=2,column=1)
        self.frameCollabo.grid(padx =20,pady=10,row=1,rowspan=4,column=3)
        
        
#-----------------------------------------------------------------fin du init        
    
    def getCrc(self,evt):
        nom = self.varcombo.get()
        if nom:
            print "test"
            self.crcCourant=self.vueParent.parent.getCRC(nom)
            self.afficherCRC()
        
    def afficherCRC(self):
        
        if self.crcCourant != None:
            self.retours=[]        
            self.etats=[]
            self.rows=[]
            
            self.entreeProp.delete(0,END)
            self.entreeProp.insert(0, self.crcCourant.proprio)
            self.infoDonnee.delete(0.0,END)
                                                                                                                  
            #for i,laLigneAnalyse in enumerate(analyse):
            for responsabilite in self.crcCourant.responsabilite:
                col = []
                
                # ligne -> frame avec 2 Entry (grille 1x2)
                ligne=Frame(self.infoDonnee)
                
                #pour gestion
                retour=IntVar()
                check=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
                check.var=retour
                self.retours.append(check.var)
                
                check.pack(side=LEFT)
                
                if responsabilite[1]==1:
                    check.select()
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
                    entree.insert(END,responsabilite[j])
                    if gere==True:
                        entree.config(state=DISABLED)
                    
                    #ne pack pas le entry qui contient le handled
                    if j<1:
                        entree.pack(side=LEFT)
                    col.append(entree)
                
                self.rows.append(col)
                #
                self.infoDonnee.window_create(INSERT,window=ligne)
        #sinon vide
        else:
            self.addRow()
       
    def addRow(self):
        pass
        #nextRow = self.tableauAnalyse.grid_size()[1]
        col = []
        # ligne -> frame avec 1 Entry
        ligne=Frame(self.infoDonnee)
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
        
        for j in range(2) :# Utilisation d'une entr
            entree = Entry(ligne,relief=RIDGE)
            entree.config(width=35)
            if j < 1:
                entree.pack(side=LEFT)
            else:
                # si < 1 = le handled : 0 par defaut (pas packé)
                entree.insert(END,0)
            col.append(entree)
        self.rows.append(col)
        #
        self.infoDonnee.window_create(INSERT,window=ligne)
        
        

    def gestion(self):
        
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
            
            
            
    def deleteRow(self):
        i=0;
        while self.etats[i].get()!=1:  #donne l'indice de la row a deleter
            i=i+1
         
        reste=[]   
        for row in self.rows:    #transfert des donnees des rows dans reste
            col=[]
            for c in range(1):
                col.append(row[c].get())
            col.append(int(row[1].get()))  # int le handled
            reste.append(col)
            
        reste.remove(reste[i]) #delete les donnees non voulues
        
        #update  # re-creation de l'analyse avec les donnees restantes
        self.infoDonnee.delete(0.0,END)
        self.retours=[]        
        self.etats=[]
        self.rows=[]
        
        for row in reste:
            
            col = []
            ligne=Frame(self.infoDonnee)
            
            retour=IntVar()
            check=Checkbutton(ligne,variable=retour,cursor="arrow",command=self.gestion)
            check.var=retour
            self.retours.append(check.var)
            check.pack(side=LEFT)
            
            if row[1]==1:
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
                    entree.config(width=35)
                    entree.insert(END,row[j])
                    if gere==True:
                        entree.config(state=DISABLED)
                    #ne pack pas le entry qui contient le handled
                    if j<1:
                        entree.pack(side=LEFT)
                    col.append(entree)
                
            self.rows.append(col)   
                
            self.infoDonnee.window_create(INSERT,window=ligne)
        
            