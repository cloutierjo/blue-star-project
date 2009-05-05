#-*- coding: iso-8859-1 -*-

# Classe : DictionnaireDonnee
# Projet : blue-star-project
# Auteur : Jonathan Hallée

from Tkinter import *

class DictionnaireDonnee(object):
    def __init__(self):
        self.dictionnaireDonnee = Frame()
        
        title = Label(self.dictionnaireDonnee, text = "Dictionnaire de données")
        title.pack()
        
        self.dictionnaireDonnee.pack()
        
        self.initDonnee()
        self.initMethodes()
        
    def initDonnee(self):
        self.frameDonnee = Frame(self.dictionnaireDonnee)
        self.retoursData=[]
        self.rowsData=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbarData = Scrollbar(self.frameDonnee)
        self.textData = Text(self.frameDonnee, yscrollcommand=scrollbarData.set)
        self.textData.config(width=50)
        
        self.frameDonnee.config(width=50)
        
        Label(self.frameDonnee,text = 'Données').pack()
        
        self.boutonAddRowData=Button(self.frameDonnee,text='Ajouter une donnée',command=self.addRow(0))
        self.boutonAddRowData.pack()
           
        scrollbarData.pack(side=RIGHT, fill=Y)
        scrollbarData.config(command=self.textData.yview)
        
        self.textData.pack()
        self.frameDonnee.pack(side=LEFT, fill=Y)
          
    def initMethodes(self):
        self.frameMethodes = Frame(self.dictionnaireDonnee)
        self.retours=[]
        self.rows=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbar = Scrollbar(self.frameMethodes)
        self.text = Text(self.frameMethodes, yscrollcommand=scrollbar.set)
        self.text.config(width=50)
            
        self.frameMethodes.config(width=50)
        
        Label(self.frameMethodes,text = 'Actions').pack()
        
        self.boutonAddRow=Button(self.frameMethodes,text='Ajouter une action',command=self.addRow(1))
        self.boutonAddRow.pack()
         
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text.yview)
        
        self.text.pack()
        self.frameMethodes.pack(side=RIGHT, fill=Y)
        
    def addRow(self, valeur):
        if valeur == 0: #on est dans les données
            self.colData = []
            # ligne -> frame avec 1 Entry
            self.ligneData=Frame(self.frameDonnee)
            retourData=IntVar()
            checkData=Checkbutton(self.ligneData,variable=retourData,cursor="arrow",command=self.gestion(valeur))
            checkData.var=retourData
            self.retoursData.append(checkData.var)
            checkData.pack(side=LEFT)
            self.addEntry(0)
            self.rowsData.append(self.colData)
        
            self.textData.window_create(INSERT,window=self.ligneData)
        
    def gestion(self, value):
        i=0
        
        if value == 0:
            # self.retours contient chaque retour associe a chaque checkButton
            for r in self.retoursData:
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
            
    def addEntry(self, valeur):
        if valeur == 0:
            for j in range(2) :# Création des deux entrées de ma ligne
                entreeData = Entry(self.ligneData,relief=RIDGE)
                entreeData.config(width=50)
                
                if j < 1:
                    entreeData.pack(side=LEFT)
                else:
                    # si < 3 = le handled : 0 par defaut (pas packé)
                    entreeData.insert(END,0)
                self.colData.append(entreeData)
        
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