#-*- coding: iso-8859-1 -*-
from  Tix import *
import Tkinter as tk
from PlanningDetail import *
from PlanningGeneral import *
sys.path.append( "../../commun" )
import Sprint
import TaskList

class ButtonCallback(object):
    def __init__(self, method, bouton):
        self.method = method
        self.bouton = bouton
        
    def invoke(self):
        self.method(self.bouton)

class Planning:
    def __init__(self, parent, listeSprint): 
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
        
            
        for i in self.listeSprint:
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
        self.frameGenTotal.pack()
        
        if self.listeSprint[0]:
            self.afficherDetails(0)

        
        
        
       
    def afficherDetails(self, indexSprint):
        for i in self.listeDetaille:
            i.frameDetail.pack_forget()
        self.listeDetaille[indexSprint].frameDetail.pack(side=RIGHT)
        
            
    def update(self):
       for index in len(self.listeFrame):
           listeTacheGeneral = self.listeFrame[index].update()
           self.listeSprint[index].taskGeneral = listeTacheGeneral
            
             
    
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
