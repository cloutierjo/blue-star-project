#-*- coding: iso-8859-1 -*-
from Tkinter import*

class CasUsage(object):
    def __init__(self,vueParent):
        self.vueParent=vueParent
        
        self.frame=Frame()
        
        titre = Label(self.frame,text = "Les Cas d'Usage")
        titre.pack()
        #...c'est la que chu rendu