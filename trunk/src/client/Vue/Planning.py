#-*- coding: iso-8859-1 -*-
from  Tix import *
import Tkinter as tk
from PlanningDetail import *
from PlanningGeneral import *
sys.path.append( "../../commun" )
import Sprint
import TaskList
import tkMessageBox, tkSimpleDialog
from datetime import *
from time import strftime, strptime
import tkFont

class ButtonCallback(object):
    def __init__(self, method, bouton):
        self.method = method
        self.bouton = bouton
        
    def invoke(self):
        self.method(self.bouton)

class Planning:
    def __init__(self, parent, CRC, listeSprint=[]):
        self.crc = CRC
        self.ancienIndexDetaille = 0
        self.listeSprint = listeSprint
        self.parent = parent
        self.listeFrame = []
        self.listeDetaille = []
        #Timeline
        hauteurTxtBox = 200
        largeurTxtBox = 300
        padxGen = 25
        #Creation du Frame
        self.frameGenTotal = Frame()
        self.windows = ScrolledWindow(self.frameGenTotal, scrollbar='auto', width=(largeurTxtBox+padxGen)*4)
        txtFont = tkFont.Font(size=8)
        Label(self.frameGenTotal, text=u"PLANNING GENERAL", font=txtFont).pack()
        Button(self.frameGenTotal, text="Ajouter Un Nouveau Sprint", command=self.ajouterNouveauSprint).pack()
        
        #Creation d'un nouveau sprint
        if not listeSprint:
           datefinString = tkSimpleDialog.askstring(u"Nouveau Projet", u"Veuillez entrez la date de fin d'un projet sous la forme AAAA-MM-JJ : ", parent=self.windows.window)
           if datefinString:
               nbsemaineparsprint = tkSimpleDialog.askinteger(u"Nouveau Projet", u"Veillez entrer la durée d'un sprint en semaine (ex: 3) :", parent=self.windows.window, initialvalue=3, minvalue=1)
               
           dateFin = datetime(*strptime(datefinString, "%Y-%m-%d")[0:5])
           td = timedelta(weeks=nbsemaineparsprint)
           dateDebutSprint = datetime.now()
           while dateDebutSprint + td <= dateFin:
               dateDebutSprint = dateDebutSprint + td
               unSprint = Sprint.Sprint()
               unSprint.dateFin=dateDebutSprint.strftime("%Y-%m-%d")
               self.listeSprint.append(unSprint)
           
           if dateDebutSprint != dateFin: # si il y reste encore du temps entre la fin du projet, mais moins que pour un sprint regulier de x semaine on en cree un plus petit avec le restant du temps
               unSprint = Sprint.Sprint()
               unSprint.dateFin=dateFin.strftime("%Y-%m-%d")
               self.listeSprint.append(unSprint)
        
        
          
        
        if self.listeSprint:                                              
            for i in self.listeSprint:
                self.creationNouveauObjetGraphiqueSprint(i)
                                        
        
    def creationNouveauObjetGraphiqueSprint(self, i): # i est un objet sprint
        hauteurTxtBox = 200
        largeurTxtBox = 300
        padxGen = 25
        frameGen = Frame(self.windows.window)
        #Label(frameGen, text=titre).pack(side=TOP)
        txtGenTempo = ScrolledText(frameGen, scrollbar='y', height=hauteurTxtBox, width=largeurTxtBox)
        if self.listeSprint.index(i) == len(self.listeSprint)-1:
            titre = u"\tFIN DU PROJET:\n\t"+i.dateFin
        else:
            titre = u"\tFIN DU SPRINT\n\tET\n\tDEBUT DU PROCHAIN:\n\t"+i.dateFin
        self.pg = PlanningGeneral(frameGen, txtGenTempo.text, titre, i.taskGeneral)
        callback = ButtonCallback(self.afficherDetails, self.listeSprint.index(i))
        self.boutonAddRow=Button(frameGen, text=u'Afficher Les Détails',
                                 command = callback.invoke)
        
        
        self.listeFrame.append(self.pg)
        self.boutonAddRow.pack(side=BOTTOM)
        txtGenTempo.pack()
        frameGen.pack(side=LEFT, padx=padxGen, pady=padxGen)
        self.listeDetaille.append(PlanningDetail(i.taskFull.tasklist)) 
            
    def afficherDetails(self, indexSprint):
        for i in self.listeDetaille:
            i.frameDetail.pack_forget()
        self.listeDetaille[indexSprint].frameDetail.pack(side=RIGHT)
        
    def ajouterNouveauSprint(self):
        unSprint = Sprint.Sprint()
        datefinString = tkSimpleDialog.askstring(u"Nouveau Sprint", u"Veuillez entrez la date de fin du nouveau sprint sous la forme AAAA-MM-JJ : ", parent=self.windows.window)
        dateFin = datetime(*strptime(datefinString, "%Y-%m-%d")[0:5])
        unSprint.dateFin=dateFin.strftime("%Y-%m-%d")
        self.listeSprint.append(unSprint)
        self.creationNouveauObjetGraphiqueSprint(unSprint)
        titre = u"\tFIN DU SPRINT\n\tET\n\tDEBUT DU PROCHAIN:\n\t"+self.listeSprint[-2].dateFin
        self.listeFrame[-2].lblText.set(titre)
        
        
                
    def update(self):
        for index in range(len(self.listeFrame)):
           self.listeSprint[index].taskGeneral = self.listeFrame[index].update()
           self.listeSprint[index].taskFull = []
           listeRetourDetails = self.listeDetaille[index].update()
           tlf=TaskList.TaskList()
           for uneTacheRetournee in listeRetourDetails :
               tb=TaskList.Task()
               tb.name=uneTacheRetournee[0]
               tb.priorite=int(uneTacheRetournee[1])
               tb.user = uneTacheRetournee[2]
               tb.handled = int(uneTacheRetournee[3])
               tlf.tasklist.append(tb)
           self.listeSprint[index].taskFull = tlf
        
        lsp=Sprint.LstSprint()
        lsp.sprints = self.listeSprint
        return lsp.sprints
             
    def cacher(self):
        self.frameGenTotal.pack_forget()
        self.windows.pack_forget()
        for i in self.listeDetaille:
            i.frameDetail.pack_forget()
        self.crc.frame.pack_forget()
        
        
    def afficherDetailSelectionne(self,date):
        for i in self.listeDetaille:
            i.frameDetail.pack_forget()
        dte=strptime(date, "%Y-%m-%d")
        retour = self.listeDetaille[-1].frameDetail
        for i in range(len(self.listeSprint)):
            spDte=strptime(self.listeSprint[i].dateFin, "%Y-%m-%d")
            if dte<spDte:
                return self.listeDetaille[i].frameDetail
        else:
            return retour
     
    def afficher(self):
        self.frameGenTotal.pack()
        self.windows.pack(pady=15)
        self.afficherDetails(0)
        self.crc.frame.pack(side=LEFT, anchor=S)
