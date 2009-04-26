#-*- coding: iso-8859-1 -*-
'''
classe vue
auteur: Pascal Lemay
            '''
from Tkinter import*
import tkMessageBox, tkSimpleDialog
import sys
sys.path.append( "../commun" )
import Projet

class Vue(object):
#initialisation
    def __init__(self,parent):
        self.parent=parent
        #0:Aucune Project loade,    1:Projet Loade
        self.etat=0

        self.root=Tk()
        self.root.title("Blue Star")
        self.root.geometry("1024x768")
        
# toute les composantes graphiques
        
#L'objet graphique Mandat
        self.mandat = None
        
#L'objet graphique des  AT
        self.ATImplicite = None
        self.ATExplicite = None
        self.casUsage = None



#Haut    
    def menuPrincipal(self):
        #cree une barre de menu (qui est aussi un objet Menu)
        menu = Menu(self.root)
        #assigne cette barre a la fenetre
        self.root.config(menu=menu)
        
        filemenu = Menu(menu)
        #menu 
        menu.add_cascade(label="Fichier", menu=filemenu)
        #Nouveau projet
        filemenu.add_command(label="Nouveau projet", command=self.NouveauProjet)
        #projet
        filemenu.add_command(label="Ouvrir Projet", command=self.OuvrirProjet)
        
        filemenu.add_command(label="Sauvegarder", command=self.save)
        
        filemenu.add_command(label="Fermer le projet", command=self.fermerProjet)
        filemenu.add_separator()
        #quitter
        filemenu.add_command(label="Quitter", command=self.parent.quitter)
        
        
        #commandes de l'affichage
        displaymenu=Menu(menu)
        menu.add_cascade(label="Affichage",menu=displaymenu)
        displaymenu.add_command(label="Afficher le mandat/analyse explicite",command=self.afficherFenMandat)
        displaymenu.add_command(label="Afficher analyse explicite/implicite",command=self.afficherLesAnalyses)
        displaymenu.add_command(label="Cacher ATEXPLICTITE",command=self.cacherAnalyse)
        #...
        
        #Aide
        helpmenu = Menu(menu)
        menu.add_cascade(label="Aide", menu=helpmenu)
        

#fonction sur l'ouverture projet
    def OuvrirProjet(self):
        if self.etat==0:
            projets=ListeProjets(self.parent.getListeProjets(),self)
            self.etat=1
    def chargerEnMemoireProjet(self):
        self.mandat=Mandat(self,self.parent.ouvrirMandat())
        self.ATExplicite = analyseTextuelle(self,self.parent.ouvrirATExplicite(),explicite=True)
        self.ATImplicite = analyseTextuelle(self,self.parent.ouvrirATImplicite(),implicite=True)
        
    def NouveauProjet(self):
         if self.etat==0:
            nom=tkSimpleDialog.askstring('Nom de projet',
                                     'Entrez un nom pour le projet:', 
                                     parent=self.root)
            if nom:
                self.parent.creerProjet(nom)
                self.etat=1
                
    def fermerProjet(self):
        pass
    
    def save(self):
        if self.etat !=0:
            self.parent.sauvegarder()
            
#mandat->String et analyse ->liste de dictionnaire
    def afficherFenMandat(self):
        self.mandat.frame.pack(side=LEFT,fill=Y)
        self.afficherAnalyse()
        
    def afficherAnalyse(self):
        if self.ATExplicite != None:
            self.ATExplicite.frame.pack()
            
    def afficherLesAnalyses(self):
        if self.ATExplicite != None:
            self.ATExplicite.frame.pack(side=LEFT)
        if self.ATImplicite != None:
            self.ATImplicite.frame.pack()
####            
    def cacherAnalyse(self):
        self.ATExplicite.frame.pack_forget()
#--------------------------------------------------------------------------
class Mandat(object):
    def __init__(self,vueParent,mandat):
        self.vueParent=vueParent
        self.mandat=mandat
        
        self.frame = Frame()
        
#        if(self.etat==1 or self.etat==2):
            #etat 1: affiche mandat vide pour en creer un pour un nouveau projet
            #etat 2: affiche le mandat du projet ouvert
        self.frame.pack(side=LEFT,fill=Y)
        nom = Label(self.frame,text = 'Mandat :')
        nom.pack()
        s = Scrollbar(self.frame)
        #t->texte mandat
        self.t = Text(self.frame)
        self.t.config(width=80)
        self.t.focus_set()
        s.pack(side=RIGHT, fill=Y)
        self.t.pack(side=LEFT, fill=Y)
        s.config(command=self.t.yview)
        self.t.config(yscrollcommand=s.set)
        if self.mandat == None:
            self.t.insert(END,"")
        else:
            self.t.insert(END,self.mandat)
        
        self.updateMandat()    
        self.frame.pack_forget()
        
    def updateMandat(self):
        self.vueParent.parent.creerMandat(self.t.get(1.0,END))
                
        #instance d'analyseTextuelle (vide si nouveau projet)
#           if len(self.parent.ouvrirATExplicite()) != 0:
#               self.analyseGrid=analyseTextuelle(self,self.parent.ouvrirATExplicite())
#           else:
#               self.analyseGrid = analyseTextuelle(self,[])
                    
                #1:fenetre mandat et analyse textuelle vide        
            #self.fenOuverte=1
#---------------------------------------------------------------------------           
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
        
                                                                                                                        
                                                                                                                        
      # Insertion des données existante dans le tableau
        if len(analyse) !=0:                                                                                                       
            for i in range(len(analyse)):
                self.tableauAnalyse.insert(END, "\n2232")
                laLigneAnalyse=analyse[i]
                col = []
                for j in range(3):
                    entree = Entry(self.tableauAnalyse,relief=RIDGE)
                    entree.grid(row=i, column=j, sticky=NSEW)
                    if j == 0:
                        entree.insert(END,laLigneAnalyse['nom'])
                    elif j == 1:
                        entree.insert(END,laLigneAnalyse['verbe'])
                    elif j == 2:
                        entree.insert(END,laLigneAnalyse['adjectif'])
                    col.append(entree)
                self.rows.append(col)
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
        for j in range(3) :# Utilisation d'une entr
            entree = Entry(self.tableauAnalyse,relief=RIDGE)
            entree.grid(row=nextRow, column=j,sticky=NSEW)
            col.append(entree)
        self.rows.append(col)

#---------------------------------------------------------------------------            
class ListeProjets(object):
#fenetre affichant les projets existants
    def __init__(self,data,parent):
        self.fen=Tk()
        self.parent = parent
        self.data = data
        self.fen.title("Projets")
        self.fen.resizable(False,False)
        
        self.scroll = Scrollbar(self.fen)
        self.scroll.pack(side=RIGHT, fill=Y)
        
        self.maliste=Liste(self.fen,data=data,width=25,height=3)
        self.maliste.pack()
        
        self.scroll.config(command=self.maliste.yview)
        self.maliste.config(yscrollcommand=self.scroll.set)
        
        self.choix=Entry(self.fen)
        self.choix.pack()
        self.b = Button(self.fen,text="OK",command=self.choisirProjet)
        self.b.pack()
    def choisirProjet(self):
        if self.maliste.getData():
            self.parent.parent.ouvrirProjet(self.data[self.maliste.getData()][0])
            #projet ouvert
            self.parent.etat=1
            self.parent.chargerEnMemoireProjet()
            self.fen.destroy()
        else:
            tkMessageBox.showwarning(
            "Echec d'ouverture",
            "impossible d'ouvrir le projet")
            #print "impossible d'ouvrir le projet"
        
#----------------------------------------------------------------------------
class Liste(Listbox):
    #liste des projets existants
    def __init__(self,parent,data=[],width=20,height=1):
        Listbox.__init__(self,parent)#,parent,width,height)
        self.fillListe(data)
        
    def fillListe(self,data):
        for i in data:
            self.insert(END,i[1])
            
    def getData(self,evt=0):
        ca=self.curselection()
        if ca:
            return int(ca[0])
        
#----------------------------------------------------------------------------

        
        
