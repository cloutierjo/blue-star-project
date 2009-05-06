#-*- coding: iso-8859-1 -*-

# Classe : DictionnaireDonnee
# Projet : blue-star-project
# Auteur : Jonathan Hallée

from Tkinter import *

class DictionnaireDonnee(object):
    def __init__(self, vueParent):
        self.vueParent = vueParent
        self.dictionnaireDonnee = Frame()
        
        title = Label(self.dictionnaireDonnee, text = "Dictionnaire de données")
        title.pack()
        
        self.dictionnaireDonnee.pack()
        
        d = Donnee()
        a = Action()

class Donnee(object):
    def __init__(self):
        self.initDonnee()
        
    def initDonnee(self):
        self.frameDonnee = Frame()
        self.retoursData=[]
        self.rowsData=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbarData = Scrollbar(self.frameDonnee)
        self.textData = Text(self.frameDonnee, yscrollcommand=scrollbarData.set)
        self.textData.config(width=40)
        
        self.frameDonnee.config(width=50)
        
        Label(self.frameDonnee,text = 'Données').pack()
        
        self.boutonAddRowData=Button(self.frameDonnee,text='Ajouter une ligne',command=self.addRow)
        self.boutonAddRowData.pack()
           
        scrollbarData.pack(side=RIGHT, fill=Y)
        scrollbarData.config(command=self.textData.yview)
        
        self.textData.pack(side=LEFT, fill=Y)
        self.frameDonnee.pack(side=LEFT, fill=Y)
        
    def addRow(self):
        retour=IntVar()
        self.col = []
        
        # ligne -> frame avec 1 Entry
        self.ligneData=Frame(self.textData)
            
        check=Checkbutton(self.ligneData,variable=retour,cursor="arrow",command=self.gestion)
        check.var=retour
            
        self.retoursData.append(check.var)
            
        check.pack(side=LEFT)
        self.addEntry()
        self.rowsData.append(self.col)
                
        self.textData.window_create(INSERT,window=self.ligneData)
            
    def gestion(self):
        i=0
            # self.retours contient chaque retour associe a chaque checkButton
        for r in self.retoursData:
            #mettre a gere
            if r.get()==1:
                self.rowsData[i][1].delete(0, END) 
                self.rowsData[i][1].insert(END,1)                                  
                                                            
                self.rowsData[i][0].config(state=DISABLED)
            #mettre a non gere
            else:
                self.rowsData[i][0].config(state=NORMAL)
                self.rowsData[i][1].config(state=NORMAL)
                          
                self.rowsData[i][1].delete(0, END)
                self.rowsData[i][1].insert(END,0)
            i+=1
            
    def addEntry(self):
        for j in range(2) :# Création des deux entrées de ma ligne
            entree = Entry(self.ligneData,relief=RIDGE)
            entree.config(width=50)
                
            if j < 1:
                entree.pack(side=LEFT)
            else:
                # si < 3 = le handled : 0 par defaut (pas packé)
                entree.insert(END,0)
            self.col.append(entree)
            
class Action(object):
    def __init__(self):
        self.initMethodes()
        
    def initMethodes(self):
        self.frameMethodes = Frame()
        self.retours=[]
        self.rows=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbar = Scrollbar(self.frameMethodes)
        self.text = Text(self.frameMethodes, yscrollcommand=scrollbar.set)
        self.text.config(width=50)
         
        self.boutonAddRow=Button(self.frameMethodes,text='Ajouter une action',command=self.addRow)
        self.boutonAddRow.pack()
        
        Label(self.frameMethodes,text = 'Actions').pack()
        
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text.yview)
        
        self.text.pack(side=LEFT, fill=Y)
        self.frameMethodes.pack(side=RIGHT, fill=Y)
        
    def addRow(self):
        retour=IntVar()
        self.col = []
        
        # ligne -> frame avec 1 Entry
        self.ligne=Frame(self.text)
            
        check=Checkbutton(self.ligne,variable=retour,cursor="arrow",command=self.gestion)
        check.var=retour
            
        self.retours.append(check.var)
            
        check.pack(side=LEFT)
        self.addEntry()
        self.rows.append(self.col)
                
        self.text.window_create(INSERT,window=self.ligne)
        
    def gestion(self):
        i=0
            # self.retours contient chaque retour associe a chaque checkButton
        for r in self.retours:
            #mettre a gere
            if r.get()==1:
                self.rows[i][1].delete(0, END) 
                self.rows[i][1].insert(END,1)                                  
                                                            
                self.rows[i][0].config(state=DISABLED)
            #mettre a non gere
            else:
                self.rows[i][0].config(state=NORMAL)
                self.rows[i][1].config(state=NORMAL)
                          
                self.rows[i][1].delete(0, END)
                self.rows[i][1].insert(END,0)
            i+=1
             
    def addEntry(self):
        for j in range(2) :# Création des deux entrées de ma ligne
            entree = Entry(self.ligne,relief=RIDGE)
            entree.config(width=50)
                
            if j < 1:
                entree.pack(side=LEFT)
            else:
                # si < 3 = le handled : 0 par defaut (pas packé)
                entree.insert(END,0)
            self.col.append(entree)
        
if __name__ == '__main__':
    #TESTING DE MA VUE EN LOCAL
    class Vue(object):
        def __init__(self):
            self.root=Tk()
            self.root.title("Blue Star")
            self.root.geometry("1024x768")
    
    v = Vue()
    d = DictionnaireDonnee()
    
    v.root.mainloop()