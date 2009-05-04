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
        self.retours=[]
        self.rows=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbar = Scrollbar(self.frameDonnee)
        self.text = Text(self.frameDonnee, yscrollcommand=scrollbar.set)
        self.text.pack()
        
        self.frameDonnee.config(width=50)
        
        self.boutonAddRow=Button(self.frameDonnee,text='Ajouter une donnée',command=self.addRow)
        self.boutonAddRow.pack()
        
        Label(self.frameDonnee,text = 'Données').pack()
        
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text.yview)
        
        self.frameDonnee.pack(side=LEFT,fill=Y)
    
    def initMethodes(self):
        self.frameMethodes = Frame(self.dictionnaireDonnee)
        self.retours=[]
        self.rows=[]
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x1
        scrollbar = Scrollbar(self.frameMethodes)
        self.text = Text(self.frameMethodes, yscrollcommand=scrollbar.set)
        self.text.pack()
        
        self.frameMethodes.config(width=50)
        
        self.boutonAddRow=Button(self.frameMethodes,text='Ajouter une action',command=self.addRow)
        self.boutonAddRow.pack()
        
        Label(self.frameMethodes,text = 'Actions').pack()
        
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text.yview)
        
        self.frameMethodes.pack(side=LEFT,fill=Y)
        
    def addRow(self):
        #nextRow = self.dictionnaireDonnee.grid_size()[1]
        self.col = []
        # ligne -> frame avec 1 Entry
        self.ligne=Frame(self.dictionnaireDonnee)
        retour=IntVar()
        check=Checkbutton(self.ligne,variable=retour,cursor="arrow",command=self.gestion)
        check.var=retour
        self.retours.append(check.var)
        check.pack(side=LEFT)
        self.addEntry()
        self.rows.append(self.col)

        self.dictionnaireDonnee.window_create(INSERT,window=self.ligne)
        
    def gestion(self):
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
                  
                self.rows[i][1].delete(0, END)
                self.rows[i][1].insert(END,0)
            i+=1
            
    def addEntry(self):
        for j in range(3) :# Création des deux entrées de ma ligne
            entree = Entry(self.ligne,relief=RIDGE)
            entree.config(width=30)
            
            if j < 2:
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