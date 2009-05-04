#-*- coding: iso-8859-1 -*-

# Classe : DictionnaireDonnee
# Projet : blue-star-project
# Auteur : Jonathan Hallée

from Tkinter import *

class DictionnaireDonnee(object):
    def __init__(self):
    #def __init__(self, vueParent):
        #self.vueParent = vueParent
        self.frame = Frame()
        self.retours=[]
        self.rows=[]
        
        title = Label(self.frame, text = "Dictionnaire de données")
        title.pack()
        
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x3
        scrollbar = Scrollbar(self.frame)
        self.dictionnaireDonnee = Text(self.frame, yscrollcommand=scrollbar.set)
        self.dictionnaireDonnee.config(width=50)
        
        self.boutonAddRow=Button(self.frame,text='Ajouter une ligne',command=self.addRow)
        self.boutonAddRow.pack()
        
        Label(self.frame,text = 'Données / Méthodes').pack()
        
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.dictionnaireDonnee.yview)
        
        self.dictionnaireDonnee.pack(side=LEFT,fill=Y)
        
    def addRow(self):
        #nextRow = self.dictionnaireDonnee.grid_size()[1]
        self.col = []
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
                self.rows[i][2].delete(0, END) 
                self.rows[i][2].insert(END,1)                                  
                                                    
                self.rows[i][0].config(state=DISABLED)
                self.rows[i][1].config(state=DISABLED)
                
            #mettre a non gere
            else:
                self.rows[i][0].config(state=NORMAL)
                self.rows[i][1].config(state=NORMAL)
                self.rows[i][2].config(state=NORMAL)
                  
                self.rows[i][2].delete(0, END)
                self.rows[i][2].insert(END,0)
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
    d.frame.pack()
    
    v.root.mainloop()