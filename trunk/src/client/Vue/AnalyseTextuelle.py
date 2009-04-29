#-*- coding: iso-8859-1 -*-
from Tkinter import*

class analyseTextuelle(object):
    def __init__(self,vueParent,analyse,implicite=False,explicite=False):
        self.rows=[]
        self.vueParent=vueParent
        self.implicite = implicite
        self.explicite  = explicite
        
        #Creation du Frame
        self.frame = Frame()

        #Ajout du Label Tite
        titreImplicite = "Analyse Implicite"
        titreExplicite = "Analyse Explicite"
        if implicite:
            lblTitre = Label(self.frame,text = titreImplicite)
        elif explicite:
            lblTitre = Label(self.frame,text = titreExplicite)
        else:
            lblTitre = Label(self.frame,text = titreExplicite)
            print "Aucun type d'analyse spécifié, Explicite par défault"
        
        lblTitre.pack()
            
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x3
        scrollbar = Scrollbar(self.frame)
        self.tableauAnalyse = Text(self.frame, yscrollcommand=scrollbar.set)
        self.tableauAnalyse.config(width=45)
        
                                                                                                                        
                                                                                                                        
      # Insertion des données existante dans le tableau si il y en a
        if len(analyse) !=0:                                                                                                       
            for i,laLigneAnalyse in enumerate(analyse):
                col = []
                # ligne -> frame avec 3 Entry (grille 1x3)
                ligne=Frame(self.tableauAnalyse)
                for j,champ in enumerate(['nom','verbe','adjectif']):
                    entree = Entry(ligne,relief=RIDGE)
                    entree.insert(END,laLigneAnalyse.get(champ))
                    entree.pack(side=LEFT)
                    col.append(entree)
                
                self.rows.append(col)
                #
                self.tableauAnalyse.window_create(INSERT,window=ligne)
        #sinon vide
        else:
            self.addRow()
        
        

        self.boutonAddRow=Button(self.frame,text='Ajouter une ligne',command=self.addRow)
        self.boutonAddRow.pack()
        Label(self.frame,text = 'Noms: Verbe: Adjectifs:').pack()
        
        
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.tableauAnalyse.yview)
        
        
        self.tableauAnalyse.pack(side=LEFT,fill=Y)
        
        
    def updateAnalyse(self):
        listeDictionnaires=[]
        for row in self.rows:
           dict={}
           dict['nom']=row[0].get()
           dict['verbe']=row[1].get()
           dict['adjectif']=row[2].get()
           listeDictionnaires.append(dict)

            
            
        if self.implicite:
           self.vueParent.parent.creerATImplicite(listeDictionnaires)
        elif self.explicite:
            self.vueParent.parent.creerATExplicite(listeDictionnaires)
                
            
    def addRow(self):
        nextRow = self.tableauAnalyse.grid_size()[1]
        col = []
        # ligne -> frame avec 3 Entry
        ligne=Frame(self.tableauAnalyse)
        for j in range(3) :# Utilisation d'une entr
            entree = Entry(ligne,relief=RIDGE)
            entree.pack(side=LEFT)
            col.append(entree)
        self.rows.append(col)
        #
        self.tableauAnalyse.window_create(INSERT,window=ligne)
