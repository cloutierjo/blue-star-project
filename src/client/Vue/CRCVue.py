#-*- coding: iso-8859-1 -*-
'''
 Auteurs: Jean-Philippe Chan et Pascal Lemay
 '''
from Tkinter import *
import tkMessageBox, tkSimpleDialog
import Tix

class CrcVUE(object):
    def __init__(self,vueParent,listeDeCRC):
        self.vueParent=vueParent
        self.listeDeCRC=listeDeCRC
        self.crcCourant=None # objet crc qui est affich� et qui provient du projet

        self.rows=[]    # section R�les (donn�es fonctions)
        self.retours=[]
        self.etats=[]
        
        self.rowsCollabo=[] # section collaboratiion
        self.etatsCollabo=[]
        
        
        self.frame = Frame(borderwidth=2, relief="groove")        
        self.frameInfo = Frame(self.frame)
        self.frameCollabo = Frame(self.frame)#les frames
        
        self.entreeProprio=Text(self.frameInfo,relief=RIDGE)#######
        self.entreeProprio.config(width=20,height=1)
        
        self.varUser = Tix.StringVar()
        self.comboProprio = Tix.ComboBox(self.frameInfo,label='Propri�taire   :',editable=0,variable=self.varUser,dropdown=1,command=self.setProprietaire,width=30)
                                                                                                                                                        #option='listbox.width 30'
        self.varcombo = Tix.StringVar()#comboClasse->liste des crc du projet
        self.comboClasse=Tix.ComboBox(self.frameInfo,label='Liste des CRC:',editable=0,variable=self.varcombo,dropdown=1,command=self.getCrc,width=30)
        self.comboClasse.pack()
        
#######collaborateur potentiel dans combobox        
        self.col = Tix.StringVar()
        self.comboCRC=Tix.ComboBox(self.frameCollabo,editable=0,variable=self.col,dropdown=1,command=self.addCollaborateur,width=30)
        
        self.updateListeCRC()#load la liste des crc du projet dans le combobox
        
        self.updateListeUser()#load la liste des users du projet dans le combo de users
        

        self.comboProprio.pack(pady=2)
        self.entreeProprio.pack(pady=2)
        self.entreeProprio.config(state=DISABLED)

        
        titreInfo = Label(self.frameInfo,text=u"R�les:(Donn�es et Fonctions)")
        titreInfo.pack()
        self.boutonAddRow=Button(self.frameInfo,text=u'ajouter un r�le',command=self.addRow)
        self.boutonAddRow.pack()
        
        self.infoDonnee = Text(self.frameInfo, width=25,height=12)   
        self.scrollbarInfo = Scrollbar(self.frameInfo)
        self.scrollbarInfo.pack(side=RIGHT, fill=Y)
        self.infoDonnee.pack(side=LEFT, fill=Y)
        self.scrollbarInfo.config(command=self.infoDonnee.yview)
        self.infoDonnee.config(yscrollcommand=self.scrollbarInfo.set)
        
        ##
        miniFrameBoutons=Frame(self.frameCollabo)
        self.boutonNewCrc=Button(miniFrameBoutons,text=u'Cr�er nouveau CRC',command=self.nouveauCrc)
        self.boutonNewCrc.pack(side=LEFT)
        
        valeur=IntVar()
        self.checkHandled=Checkbutton(miniFrameBoutons,variable=valeur,cursor="arrow",command=self.setHandled)
        self.checkHandled.var=valeur
        self.checkHandled.pack(side=LEFT)
        
        miniFrameBoutons.pack()
        
        self.titreCollabo = Label(self.frameCollabo,text=u"Les collaborateurs")
        self.titreCollabo.pack()
######collaborateur potentiel dans combobox
        self.comboCRC.pack()
        
#######collaborateurs
        
        self.collaboration = Text(self.frameCollabo, width=25,height=15)
        self.scrollbarCol=Scrollbar(self.frameCollabo)
        self.scrollbarCol.pack(side=RIGHT, fill=Y)
        self.collaboration.pack(side=LEFT, fill=Y)
        self.scrollbarCol.config(command=self.collaboration.yview)
        self.collaboration.config(yscrollcommand=self.scrollbarCol.set)
   

        self.frameInfo.pack(side=LEFT)
        self.frameCollabo.pack(side=LEFT)
        
        self.infoDonnee.config(state=DISABLED)
        self.collaboration.config(state=DISABLED)
        
#--------------------------------------------------------------------
    def nouveauCrc(self):
        nom=tkSimpleDialog.askstring(u'Nouveau CRC',
                                         u'Entrez le nom de la classe :',parent=self.vueParent.root)
        if nom:
            if self.vueParent.parent.createNewCrc(nom):
                self.vueParent.updateListeCRC()
                self.updateCRC()
                self.varcombo.set(nom)
                self.checkHandled.deselect()
                self.crcCourant=self.vueParent.parent.getCRC(nom)
                self.afficherRoles()
                self.afficherCollabo()
            if self.crcCourant.handled==1:
                self.checkHandled.select()
        else:
            self.vueParent.afficherUnMessage(u"Un Crc porte ce nom",erreur="ERREUR!!!")        
    
    def getCrc(self,evt):
        self.updateCRC()
        nom = self.varcombo.get()
        if nom:
            self.checkHandled.deselect()
            self.crcCourant=self.vueParent.parent.getCRC(nom)
            self.afficherRoles()
            self.afficherCollabo()
            if self.crcCourant.handled==1:
                self.checkHandled.select()
            
    def setProprietaire(self,evt):
        self.entreeProprio.config(state=NORMAL)
        self.entreeProprio.delete(0.0,END)###################################
        self.entreeProprio.insert(END,self.varUser.get())
        self.entreeProprio.config(state=DISABLED)
        
    def setHandled(self):
        if self.crcCourant != None:
            if self.checkHandled.var.get()==1:
                self.crcCourant.handled=1
                for row in self.rowsCollabo:
                    row.config(state=DISABLED)
                    
            else:
                self.crcCourant.handled=0
                for row in self.rowsCollabo:
                    row.config(state=NORMAL)
                
        
            
    def updateListeCRC(self):
        self.comboClasse.subwidget_list['slistbox'].subwidget_list['listbox'].delete(0,END)
        self.comboCRC.subwidget_list['slistbox'].subwidget_list['listbox'].delete(0,END)
        self.listeDeCRC=self.vueParent.parent.getListeCRC()
        for crc in self.listeDeCRC:  #load la liste des crc du projet dans les comboboxs
            self.comboClasse.insert(END,crc)
            self.comboCRC.insert(END,crc)
            
            
    def updateListeUser(self):
        self.comboProprio.subwidget_list['slistbox'].subwidget_list['listbox'].delete(0,END)
        user=self.vueParent.parent.getUsers()
        for proprio in user:
            self.comboProprio.insert(END,proprio)
        
        
    def afficherRoles(self):
        self.infoDonnee.config(state=NORMAL)
        if self.crcCourant != None:
            self.retours=[]        
            self.etats=[]
            self.rows=[]
            
            self.entreeProprio.config(state=NORMAL)
            self.entreeProprio.delete(0.0,END)#############################
            self.entreeProprio.insert(END,self.crcCourant.proprio)
            self.entreeProprio.config(state=DISABLED)
            
            self.infoDonnee.delete(0.0,END)
                                                                                                                  
            for responsabilite in self.crcCourant.responsabilite:
                col = []
                
                # ligne -> frame 
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
                delRow=Radiobutton(ligne,text=u'x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
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
            self.infoDonnee.config(state=DISABLED)
        #sinon vide
        else:
            self.addRow()
            self.infoDonnee.config(state=DISABLED)
            
    def afficherCollabo(self):
        self.collaboration.config(state=NORMAL)
        if self.crcCourant != None:
            self.etatsCollabo=[]        
            self.rowsCollabo=[]
            
            self.collaboration.delete(0.0,END)
                                                                                                                  
            for collaborateur in self.crcCourant.collaboration:
                
            # ligne -> frame
                ligne=Frame(self.collaboration)
            #pour delete 
                state=IntVar()
                delRowCol=Radiobutton(ligne,text=u'x',variable=state,value=1,cursor="arrow",indicatoron=False,command=self.deleteRowCollabo)
                delRowCol.var=state
                self.etatsCollabo.append(delRowCol.var)
                delRowCol.pack(side=LEFT)
                    
                entree = Entry(ligne,relief=RIDGE)
                entree.config(width=38)
                entree.insert(END,collaborateur)
        
                entree.pack(side=LEFT)
                self.rowsCollabo.append(entree)
                self.collaboration.window_create(INSERT,window=ligne)
                
                if self.crcCourant.handled==1:
                    entree.config(state=DISABLED)
        self.collaboration.config(state=DISABLED)
        
    
    def updateCRC(self):
        if self.crcCourant!=None:
            self.crcCourant.responsabilite=[]
            self.crcCourant.collaboration=[]
            
            self.entreeProprio.config(state=NORMAL)
            self.crcCourant.proprio=self.entreeProprio.get(0.0,END)############
            self.entreeProprio.config(state=DISABLED)
            
            for row in self.rows:
                unRole=[]
                unRole.append(row[0].get())
                unRole.append(int(row[1].get()))
                self.crcCourant.responsabilite.append(unRole)
                
            for collaborateur in self.rowsCollabo:
                self.crcCourant.collaboration.append(collaborateur.get())

            self.vueParent.parent.updateCrc(self.crcCourant)
            
       
    def addRow(self):
        if self.crcCourant != None and self.crcCourant.handled!=1:
        
            self.infoDonnee.config(state=NORMAL)
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
            delRow=Radiobutton(ligne,text=u'x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
            delRow.var=etat
            self.etats.append(delRow.var)
            delRow.pack(side=LEFT)
            
            for j in range(2) :# Utilisation d'une entr
                entree = Entry(ligne,relief=RIDGE)
                entree.config(width=35)
                if j < 1:
                    entree.pack(side=LEFT)
                else:
                    # si < 1 = le handled : 0 par defaut (pas pack�)
                    entree.insert(END,0)
                col.append(entree)
            self.rows.append(col)
            #
            self.infoDonnee.window_create(INSERT,window=ligne)
            
            self.infoDonnee.config(state=DISABLED)
        
    def addCollaborateur(self,evt):
        if self.crcCourant != None and self.crcCourant.handled!=1:
            present=False
            nouveauCollabo = self.col.get()
            if nouveauCollabo:
                for collaborateur in self.crcCourant.collaboration:
                    if nouveauCollabo==collaborateur:
                        present=True
                if present==False:
                    self.crcCourant.collaboration.append(nouveauCollabo)
                    
            self.afficherCollabo()

    def gestion(self):
        self.infoDonnee.config(state=NORMAL)
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
            
        self.infoDonnee.config(state=DISABLED)
            
            
            
    def deleteRow(self):
        self.infoDonnee.config(state=NORMAL)
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
            
        #update  # re-creation du crc avec les donnees restantes
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
            delRow=Radiobutton(ligne,text=u'x',variable=etat,value=1,cursor="arrow",indicatoron=False,command=self.deleteRow)
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
                
            self.infoDonnee.config(state=DISABLED)
        
    def deleteRowCollabo(self):
            self.collaboration.config(state=NORMAL)
            i=0
            while self.etatsCollabo[i].get()!=1:  #donne l'indice de la row a deleter
                i=i+1
            
            self.crcCourant.collaboration=[]
                
            for row in self.rowsCollabo:  #transfert des donnees des rows dans self.crcCourant.collaboration
                self.crcCourant.collaboration.append(row.get())
        
            self.crcCourant.collaboration.remove(self.crcCourant.collaboration[i]) #delete le collaborateur
            
            #r�affichage
            self.afficherCollabo()  