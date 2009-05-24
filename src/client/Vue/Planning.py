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
from time import strftime

class ButtonCallback(object):
    def __init__(self, method, bouton):
        self.method = method
        self.bouton = bouton
        
    def invoke(self):
        self.method(self.bouton)

class Planning:
    def __init__(self, parent, listeSprint=[]): 
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
        self.windows.pack(pady=15)
        
        
        
        if not listeSprint:
           datefinString = tkSimpleDialog.askstring("Nouveau Projet", "Veuillez entrez la date de fin d'un projet sous la forme jj-mm-aaaa : ", parent=self.windows.window)
           if datefinString:
               nbsemaineparsprint = tkSimpleDialog.askinteger("Nouveau Projet", "Veillez entrer la durée d'un sprint en semaine (ex: 3) :", parent=self.windows.window, initialvalue=3, minvalue=1)
               
           dateFin = date(int(datefinString.split("-")[2]),int(datefinString.split("-")[1]),int(datefinString.split("-")[0]))
           td = timedelta(weeks=nbsemaineparsprint)
           dateDebutSprint = date.today()
           while dateDebutSprint + td <= dateFin:
               dateDebutSprint = dateDebutSprint + td
               unSprint = Sprint.Sprint()
               unSprint.dateFin=dateDebutSprint.strftime("%d-%m-%Y")
               self.listeSprint.append(unSprint)
           
           if dateDebutSprint != dateFin: # si il y reste encore du temps entre la fin du projet, mais moins que pour un sprint regulier de x semaine on en cree un plus petit avec le restant du temps
               unSprint = Sprint.Sprint()
               unSprint.dateFin=dateFin.strftime("%d-%m-%Y")
               self.listeSprint.append(unSprint)
        
        
          
        #Creation d'un nouveau sprint
        if self.listeSprint:                                              
            for i in self.listeSprint:
                self.creationNouveauObjetGraphiqueSprint(i)
                
            self.frameGenTotal.pack()
            self.afficherDetails(0)
                                    
        Button(self.frameGenTotal,text="Sauvegarder", command=self.update).pack()
        
        
    def creationNouveauObjetGraphiqueSprint(self, i): # i est un objet sprint
        hauteurTxtBox = 200
        largeurTxtBox = 300
        padxGen = 25
        frameGen = Frame(self.windows.window)
        #Label(frameGen, text=titre).pack(side=TOP)
        txtGenTempo = ScrolledText(frameGen, scrollbar='y', height=hauteurTxtBox, width=largeurTxtBox)
        if self.listeSprint.index(i) == len(self.listeSprint)-1:
            titre = "\tFIN DU PROJET:\n\t"+i.dateFin
        else:
            titre = "\tFIN DU SPRINT\n\tET\n\tDEBUT DU PROCHAIN:\n\t"+i.dateFin
        self.pg = PlanningGeneral(frameGen, txtGenTempo.text, titre, i.taskGeneral)
        callback = ButtonCallback(self.afficherDetails, self.listeSprint.index(i))
        self.boutonAddRow=Button(frameGen, text='Afficher Les Détails',
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
             
    
if __name__ == '__main__':
        
    lsp=Sprint.LstSprint()
    for i in range(5):
        sp=Sprint.Sprint()
        sp.dateFin="29 avr"
        
        sp.taskGeneral.append(["gentask1 - "+str(i),0])
        sp.taskGeneral.append(["gentask2 - "+str(i),1])
            
        tlf=TaskList.TaskList()
        
        tb=TaskList.Task()
        tb.name="task1b - "+str(i)
        tb.priorite=1
        tb.user = "moib - "+str(i)
        tlf.tasklist.append(tb)
        
        tb=TaskList.Task()
        tb.name="task2b - "+str(i)
        tb.priorite=2
        tb.user = "301b - "+str(i)
        tlf.tasklist.append(tb)
        
        sp.taskFull=tlf
        
        lsp.sprints.append(sp)
    
    root = Tk()
    p = Planning(1,lsp.sprints)
    p.frameGenTotal.pack()
    root.mainloop()
