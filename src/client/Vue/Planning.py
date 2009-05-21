#-*- coding: iso-8859-1 -*-
from  Tix import *
import Tkinter as tk
from PlanningDetail import *



class Planning:
    def __init__(self, parent):
        
        
        self.parent = parent
        self.listeSprint = []
        #Timeline
        hauteurTxtBox = 100
        largeurTxtBox = 300
        padxGen = 15
        #Creation du Frame
        self.frameGenTotal = Frame()
        self.windows = ScrolledWindow(self.frameGenTotal, scrollbar='auto', width=(largeurTxtBox+padxGen)*4)
        self.windows.pack(pady=15)
        
        
            
        for i in range(10):
            frameGen = Frame(self.windows.window)
            frameTempo = Frame()
            titre = "Date" + str(i+1)
            Label(frameGen, text=titre).pack(side=TOP)
            txtGenTempo = ScrolledText(frameGen, scrollbar='y', height=hauteurTxtBox, width=largeurTxtBox)
            
            txtGenTempo.pack()
            self.listeSprint.append(txtGenTempo.text)
            frameGen.pack(side=LEFT, padx=padxGen)
       
        self.listeSprint[0].focus_set()
        
                  
        Button(self.frameGenTotal, text="Afficher Les Détails Du Sprint Séléctionné", width=40, command=self.retournerFocus).pack()
        self.frameGenTotal.pack()
        
        self.frameDetail = Frame()
        scrollbar = Scrollbar(self.frameDetail)
        self.textDetail = Text(self.frameDetail, width=52, height=35, yscrollcommand=scrollbar.set)
        self.plandet = PlanningDetail(self.frameDetail, self.textDetail, "Tache Priorité User",scrollbar)
        
        self.frameDetail.pack(side=BOTTOM, anchor=E)
        
        
       
    def retournerFocus(self, evt=None):
        monobjet=root.focus_get()
        print self.listeSprint.index(monobjet)
        #print monobjet.get(1.0, END)    
            
            

            
             
    
if __name__ == '__main__':
      root = Tk()
      p = Planning(1)
      p.frameGenTotal.pack()
      root.mainloop()
