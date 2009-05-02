#-*- coding: iso-8859-1 -*-
#Classe AnalyseTextuelle
#Auteurs Pascal Lemay / Mathieu Lavoie
from Tkinter import*

class AnalyseTextuelle(object):
    def __init__(self,vueParent,analyse,implicite=False,explicite=False):
        self.rows=[]
        self.vueParent=vueParent
        self.implicite = implicite
        self.explicite  = explicite
        
        #Creation du Frame
        self.frame = Frame()
        
        #pour gestion (retour des CheckButtons)
        self.retours=[]

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
        self.tableauAnalyse.config(width=50)
        
                                                                                                                                                                                                                                       
      # Insertion des données existante dans le tableau si il y en a
        if len(analyse) !=0:                                                                                                       
            for i,laLigneAnalyse in enumerate(analyse):
                col = []
                # ligne -> frame avec 3 Entry (grille 1x3)
                ligne=Frame(self.tableauAnalyse)
                
                #pour gestion
                retour=IntVar()
                check=Checkbutton(ligne,variable=retour,command=self.gestion)
                check.var=retour
                self.retours.append(check.var)
                
                check.pack(side=LEFT)
                if analyse[i]['handled']==1:
                    check.select()
                    gere=True
                else:
                    gere=False
                    
                for j,champ in enumerate(['nom','verbe','adjectif','handled']):
                    entree = Entry(ligne,relief=RIDGE)
                    entree.insert(END,laLigneAnalyse.get(champ))
                    if gere==True:
                        entree.config(state=DISABLED)
                    
                    #ne pack pas le entry qui contient le handled
                    if j<3:
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
           dict['handled']=int(row[3].get())
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
        retour=IntVar()
        check=Checkbutton(ligne,variable=retour,command=self.gestion)
        check.var=retour
        self.retours.append(check.var)
        check.pack(side=LEFT)
        for j in range(4) :# Utilisation d'une entr
            entree = Entry(ligne,relief=RIDGE)
            if j < 3:
                entree.pack(side=LEFT)
            else:
                #le handled 0 par defaut (pas packé)
                entree.insert(END,0)
            col.append(entree)
        self.rows.append(col)
        #
        self.tableauAnalyse.window_create(INSERT,window=ligne)
        
    def gestion(self):
        i=0
                #chaque retour associe a chaque checkButton
        for r in self.retours:
            #mettre a gere
            if r.get()==1:
                self.rows[i][3].delete(0, END) 
                self.rows[i][3].insert(END,1)
                
                self.rows[i][0].config(state=DISABLED)
                self.rows[i][1].config(state=DISABLED)
                self.rows[i][2].config(state=DISABLED)
                
            #mettre a non gere
            else:
                self.rows[i][0].config(state=NORMAL)
                self.rows[i][1].config(state=NORMAL)
                self.rows[i][2].config(state=NORMAL)
                
                self.rows[i][3].delete(0, END)
                self.rows[i][3].insert(END,0)
            i+=1
