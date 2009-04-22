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

    def __init__(self,parent):
        self.parent=parent
#0:free,1:projet en cour de creation,2:projet ouvert
        self.etat=0
#ce qui est affiche dans la fenetre
#0:rien, 1:mandat et analyse,2:a venir...
        self.fenOuverte=0
        self.root=Tk()
        self.root.title("Blue Star")
        self.root.geometry("1024x768")


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
        
        #commandes d'edition                                            
        editmenu=Menu(menu)
        menu.add_cascade(label="Edition",menu=editmenu)
        editmenu.add_command(label="update",command=self.callback)
        #...
        
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
        
#----------------------------------------------------------------------------
#temporaire        
    def callback(self):
        pass
#---------------------------------------------------------------------------
#liste des projets en cour
    def afficherProjet(self):
        if self.etat==0:
            projets=ListeProjets(self.parent.getListeProjets(),self)
            #self.etat=2
#---------------------------------------------------------------------------
    def afficherCasUsage(self):
        pass
#---------------------------------------------------------------------------
    def saisirNomProjet(self):
         
        if self.etat==0:
            nom=tkSimpleDialog.askstring('Nom de projet',
                                     'Entrez un nom pour le projet:', 
                                     parent=self.root)
            if nom:
                self.parent.creerProjet(nom)
                self.etat=1
                                # etat 1:pret pour creation de mandat
                self.afficherFenMandat()
                
#-----------------------------------------------------------------------------
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
    def fermerProjet(self):
        if(self.etat!=0):
            if self.fenOuverte==1:
                self.frame.destroy()
                self.analyseGrid.effacerFrame()
                self.fenOuverte=0
            #elif...
            self.etat=0
#-----------------------------------------------------------------------------
class analyseTextuelle(object):
    def __init__(self,master,analyse):
        #analyse->liste de dictionnaire
        self.master=master
        self.rows=[]
        self.cols=[]
        #Analyse
        self.frame2=Frame()
                
        self.frame2.pack(side=RIGHT,fill=Y)
        Label(self.frame2,text = 'Analyse textuelle',width=100).pack()
#ta->texte analyse
        ta = Text(self.frame2)
        ta.config(width=100)
        sc = Scrollbar(self.frame2)
                                                                                                                        
        c=0
        for d in analyse:
            c+=1
        self.rows = []
        for i in range(c):
            cols = []
            d=analyse[i]

            e = Entry(ta,relief=RIDGE)
            e.grid(row=i, column=0, sticky=NSEW)
            e.insert(END,d['nom'])
            cols.append(e)
            e = Entry(ta,relief=RIDGE)
            e.grid(row=i, column=1, sticky=NSEW)
            e.insert(END,d['verbe'])
            cols.append(e)
            e = Entry(ta,relief=RIDGE)
            e.grid(row=i, column=2, sticky=NSEW)
            e.insert(END,d['adjectif'])
            cols.append(e)
            self.rows.append(cols)

        sc.config(command=ta.yview)
        ta.config(yscrollcommand=sc.set)

        
        def updateAnalyse():
            for row in self.rows:
                nom=row[0].get()
                verbe=row[1].get()
                adj=row[2].get()    
                self.master.parent.creerATExplicite(nom,verbe,adj)
                
            
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

        
        
