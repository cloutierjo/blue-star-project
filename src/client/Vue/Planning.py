#-*- coding: iso-8859-1 -*-
from  Tix import *
import Tkinter as tk
from PlanningDetail import *
from PlanningGeneral import *

class ButtonCallback(object):
    def __init__(self, method, bouton):
        self.method = method
        self.bouton = bouton
        
    def invoke(self):
        self.method(self.bouton)

class Planning:
    def __init__(self, parent):
        
        
        self.parent = parent
        self.listeSprint = []
        #Timeline
        hauteurTxtBox = 200
        largeurTxtBox = 300
        padxGen = 15
        #Creation du Frame
        self.frameGenTotal = Frame()
        self.windows = ScrolledWindow(self.frameGenTotal, scrollbar='auto', width=(largeurTxtBox+padxGen)*4)
        self.windows.pack(pady=15)
        
            
        for i in range(6):
            frameGen = Frame(self.windows.window)
            titre = "Date" + str(i+1)
            #Label(frameGen, text=titre).pack(side=TOP)
            txtGenTempo = ScrolledText(frameGen, scrollbar='y', height=hauteurTxtBox, width=largeurTxtBox)
            listeDonne = []
            listeDonne.append(i)
            self.pg = PlanningGeneral(frameGen, txtGenTempo.text, titre,[1,2,3,0])
            txtGenTempo.pack()
            
            callback = ButtonCallback(self.retournerFocus, i)
            
            self.boutonAddRow=Button(frameGen, text='Afficher Les Détails',
                                     command = callback.invoke)
            self.boutonAddRow.pack(side=BOTTOM)
            self.listeSprint.append("test" + str(i))
            
            frameGen.pack(side=LEFT, padx=padxGen)
        self.frameGenTotal.pack()
        
                  

        listeDonneDetail = []
        listeDonneDetail.append([1,2,3,4])
        self.plandet = PlanningDetail(listeDonneDetail)
        self.plandet.frameDetail.pack(side=RIGHT)
        
        
       
    def retournerFocus(self, index):
        print self.listeSprint[index]
        #print monobjet.get(1.0, END)    
            
        

            
             
    
if __name__ == '__main__':
      root = Tk()
      p = Planning(1)
      p.frameGenTotal.pack()
      root.mainloop()
