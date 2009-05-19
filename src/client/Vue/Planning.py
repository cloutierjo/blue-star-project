#-*- coding: iso-8859-1 -*-
from  Tix import *
import Tkinter as tk



class Planning:

    def __init__(self, parent):
            hauteurTxtBox = 100
            largeurTxtBox = 300
            padxGen = 15
            #Creation du Frame
            self.frameGenTotal = Frame()
            self.windows = ScrolledWindow(self.frameGenTotal, scrollbar='auto', width=largeurTxtBox*2, height=hauteurTxtBox*2)
            self.windows.pack(pady=15)
            
            self.frameGen1 = Frame(self.windows.window)
            Label(self.frameGen1, text="Date 1").pack(side=TOP)
            self.txtGen1 = ScrolledText(self.frameGen1, scrollbar='y', height=hauteurTxtBox, width=largeurTxtBox)
            self.txtGen1.text.insert(END, "ENTRER TEXTE")
            self.txtGen1.pack()
            self.frameGen1.pack(side=LEFT, padx=padxGen)
            
            self.frameGen2 = Frame(self.windows.window)
            Label(self.frameGen2, text="Date 2").pack(side=TOP)
            self.txtGen2 = ScrolledText(self.frameGen2, scrollbar='y', height=hauteurTxtBox,  width=largeurTxtBox)
            self.txtGen2.text.insert(END, "ENTRER TEXTE 2")
            self.txtGen2.pack()
            self.frameGen2.pack(side=LEFT, padx=padxGen)
            
            self.frameGen3 = Frame(self.windows.window)
            Label(self.frameGen3, text="Date 3").pack(side=TOP)
            self.txtGen3 = ScrolledText(self.frameGen3, scrollbar='y', height=hauteurTxtBox,  width=largeurTxtBox)
            self.txtGen3.text.insert(END, "ENTRER TEXTE 3")
            self.txtGen3.pack()
            self.frameGen3.pack(side=LEFT, padx=padxGen)
            
            
            
            self.frameDetail = Frame()

            self.frameDetail.pack()
            
            
            

            
             
    
if __name__ == '__main__':
      root = Tk()
      p = Planning(1)
      p.frameGenTotal.pack()
      root.mainloop()
