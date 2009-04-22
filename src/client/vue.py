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
#0:Aucune Project loadé,1:Projet Loade
        self.etat=0

        self.root=Tk()
        self.root.title("Blue Star")
        self.root.geometry("1024x768")
        
# toute les composantes graphiques
        
#L'objet graphique Mandat
        self.mandat = None
        
#L'objet graphique des  AT
        self.ATImplicite = None
        Self.ATExplicite = None



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
        filemenu.add_command(label="Nouveau projet", command=self.saisirNomProjet)
        #projet
        filemenu.add_command(label="Ouvrir un projet", command=self.afficherProjet)
        filemenu.add_command(label="Creation d'un mandat", command=self.creationMandat)
        #?
        filemenu.add_command(label="Sauvegarder", command=self.parent.sauvegarder)
        
        filemenu.add_command(label="Fermer le projet", command=self.fermerProjet)
        filemenu.add_separator()
        #quitter
        filemenu.add_command(label="Quitter", command=self.parent.quitter)
        
        
        #commandes de l'affichage
        displaymenu=Menu(menu)
        menu.add_cascade(label="Affichage",menu=displaymenu)
        displaymenu.add_command(label="Afficher le mandat",command=self.afficherFenMandat)
        displaymenu.add_command(label="Afficher cas d'usage",command=self.afficherCasUsage)
        #...
        
        
        #Aide
        helpmenu = Menu(menu)
        menu.add_cascade(label="Aide", menu=helpmenu)
        helpmenu.add_command(label="Info", command=self.callback)
        

#fonction sur l'ouverture projet
    def OuvrirProjet(self):
        if self.etat==0:
            projets=ListeProjets(self.parent.getListeProjets(),self)
            #self.etat=2
    def chargerEnMemoireProjet(self):
        pass
    
    def NouveauProjet(self):
         
        if self.etat==0:
            nom=tkSimpleDialog.askstring('Nom de projet',
                                     'Entrez un nom pour le projet:', 
                                     parent=self.root)
            if nom:
                self.parent.creerProjet(nom)
                self.etat=1
                                # etat 1:pret pour creation de mandat
                self.afficherFenMandat()
                


    def fermerProjet(self):
        self.frame.destroy()
        self.analyseGrid.effacerFrame()
        self.etat=0
            
            
    def creationMandat(self):
        if self.etat==0:
            tkMessageBox.showwarning(
            "Attention",
            "Vous devez creer un projet \navant le mandat")

        elif self.t.get(1.0,1.99)=="":
            tkMessageBox.showwarning(
            "Attention",
            "Le champ texte mandat est vide")
        elif self.etat==1:
                self.parent.creerMandat(self.t.get(1.0,END))
                tkMessageBox.showinfo("Mandat","Projet mis a jour avec le nouveau mandat")
                self.parent.sauvegarder()
        #projet creeer et ouvert (fenetre mandat et analyse textuelle ouverte)
                self.etat=2
#-----------------------------------------------------------------------------
#mandat->String et analyse ->liste de dictionnaire
    def afficherFenMandat(self):
        self.frame=Frame(self.root)
#Mandat
        if self.fenOuverte!=1:
            if(self.etat==1 or self.etat==2):
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
                if self.parent.ouvrirMandat() == None:
                    self.t.insert(END,"")
                else:
                    self.t.insert(END,self.parent.ouvrirMandat())
                
    #instance d'analyseTextuelle (vide si nouveau projet)
                if len(self.parent.ouvrirATExplicite()) != 0:
                    self.analyseGrid=analyseTextuelle(self,self.parent.ouvrirATExplicite())
                else:
                    self.analyseGrid = analyseTextuelle(self,[])
                    
                #1:fenetre mandat et analyse textuelle vide        
                self.fenOuverte=1
        
#----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class analyseTextuelle(object):
    def __init__(self,vueParent,analyse,implicite=False,explicite=False):
        self.vueParent=vueParent
        self.rows=[]
        self.cols=[]
        
        
        #Creation du Frame
        self.frame = Frame()
        
        
        #Ajout du Label Tite
        titreImplicite = "Analyse Implicite"
        titreExplicite = "Analyse Explicite"
        if implicite:
            lblTitre = Label(self.frame,text = titreImplicite,width=100)
        elif explicite:
            lblTitre = Label(self.frame,text = titreExplicite,width=100)
        else:
            lblTitre = Label(self.frame,text = titreExplicite,width=100)
            print "Aucun type d'analyse spécifié, Explicite par défault"
            
        #Ajout du tableau C'est un textbox avec des entrée en grille 1x3
        tableauAnalyse = Text(self.frame)
        tableauAnalyse.config(width=100)
        
        
        #ajout du scroll
        scrollbar = Scrollbar(self.frame)
                                                                                                                        
                                                                                                                        
      # Insertion des données existante dans le tableauc                                                                                                                  
        for i in range(len(analyse)):
            
            cols = []
            laLigneAnalyse=analyse[i]
            for j,champs in enumerate(laLigneAnalyse.keys()):
                entree = Entry(tableauAnalyse,relief=RIDGE)
                entree.grid(row=i, column=j, sticky=NSEW)
                e.insert(END,laLigneAnalyse['champs'])
                cols.append(e) # A koi ca sert?!?
                self.rows.append(cols) # A koi ca sert?!? 

## TODO CONTINUER LE REFACTOR D'ANALYSE ET FAIRE LE REFACTOR DE MANDAT##JAI FAIM JE VAIS MANGER
        sc.config(command=ta.yview)
        ta.config(yscrollcommand=sc.set)

        
        def updateAnalyse():
            listeDictionnaires=[]
            for row in self.rows:
                dict={}
                dict['nom']=row[0].get()
                dict['verbe']=row[1].get()
                dict['adjectif']=row[2].get()
                listeDictionnaires.append(dict)
                
            self.master.parent.creerATExplicite(listeDictionnaires)
                
            
        def addRow():
            i=0
            for r in self.rows:
                i+=1
            cols = []
            for j in range(3):
                e = Entry(ta,relief=RIDGE)
                e.grid(row=i, column=j,sticky=NSEW)
                cols.append(e)
            self.rows.append(cols)
        
        self.boutonAddRow=Button(self.frame2,text='Ajouter une ligne',command=addRow)
        self.boutonAddRow.pack()    
        self.boutonUpdate=Button(self.frame2,text='Update Analyse',command=updateAnalyse)
        self.boutonUpdate.pack()
        Label(self.frame2,text = 'Noms: Verbe: Adjectifs:',width=100).pack()
        sc.pack(side=RIGHT, fill=Y)
        ta.pack(side=LEFT,fill=Y)
        sc.config(command=ta.yview)
        ta.config(yscrollcommand=sc.set)

    def effacerFrame(self):
        self.frame2.destroy()        
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
            self.parent.etat=2
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

        
        
