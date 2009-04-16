from Tkinter import*
import tkMessageBox, tkSimpleDialog
sys.path.append( "../server" )
import Projet

class Vue(object):

    def __init__(self,parent):
        self.parent=parent
        self.mode=0
        self.root=Tk()
        self.root.title("Blue Star")
        self.root.geometry("1024x768")
        #Frames utilisees tout au long de programme (un ou les deux)
        self.frame=Frame(self.root)
        self.frame2=Frame(self.root)


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
        #?
        filemenu.add_command(label="Sauvegarder", command=self.parent.sauvegarder)
        filemenu.add_separator()
        #quitter
        filemenu.add_command(label="Quitter", command=self.parent.quitter)
        
        #commandes d'edition                                            
        editmenu=Menu(menu)
        menu.add_cascade(label="Edition",menu=editmenu)
        editmenu.add_command(label="update",command=self.callback)
        editmenu.add_command(label="blabla",command=self.callback)
        editmenu.add_command(label="blabla",command=self.callback)
        #...
        
        #commandes de l'affichage
        displaymenu=Menu(menu)
        menu.add_cascade(label="Affichage",menu=displaymenu)
        displaymenu.add_command(label="Afficher le mandat",command=self.afficherFenMandat)
        displaymenu.add_command(label="Afficher ...",command=self.effacerFenetre)
        #...
        
        
        #Aide
        helpmenu = Menu(menu)
        menu.add_cascade(label="Aide", menu=helpmenu)
        helpmenu.add_command(label="blabla...", command=self.callback)
        
#----------------------------------------------------------------------------
#temporaire        
    def effacerFenetre(self):
        if self.mode==1:
            self.frame.destroy()
            self.frame2.destroy()
#---------------------------------------------------------------------------
    def callback(self):
        pass
#---------------------------------------------------------------------------
#liste des projets en cour
    def afficherProjet(self):
       ListeProjets(self.parent.getListeProjets(),self)
        
#-----------------------------------------------------------------------------
    def saisirNomProjet(self):
        nom=tkSimpleDialog.askstring('Nom de projet',
                                     'Entrez un nom pour le projet:', 
                                     parent=self.root)
        if nom:
            self.parent.creerProjet(nom)
#-----------------------------------------------------------------------------
#mandat->liste et analyse ->liste de dictionnaire
    def afficherFenMandat(self):
#        self.frame=Frame(self.root)
#Mandat
        self.frame.pack(side=LEFT,fill=Y)
        nom = Label(self.frame,text = 'Mandat :')
        nom.pack()
        s = Scrollbar(self.frame)
#t->texte mandat
        t = Text(self.frame)
        t.config(width=90)
        t.focus_set()
        s.pack(side=RIGHT, fill=Y)
        t.pack(side=LEFT, fill=Y)
        s.config(command=t.yview)
        t.config(yscrollcommand=s.set)
        
        t.insert(END,self.parent.ouvrirMandat())
        
#Analyse        
#        self.frame2=Frame(self.root)
        self.frame2.pack(side=RIGHT,fill=Y)
        nom = Label(self.frame2,text = 'Analyse textuelle\nNoms :  Verbe :  Adjectifs :')
        nom.pack()
        s = Scrollbar(self.frame2)
#ta->texte analyse
        ta = Text(self.frame2)
        ta.config(width=30)
#prend ce qu'il y a dans le champ texte analyse et l'envoie au contreleur pour update            
                    
        boutonUpdate=Button(self.frame2,text='Update Analyse',command=self.updateAnalyse)
        boutonUpdate.pack()
        s.pack(side=RIGHT, fill=Y)
        ta.pack(side=LEFT,fill=Y)
        s.config(command=ta.yview)
        ta.config(yscrollcommand=s.set)
        
        for i in self.parent.ouvrirATExplicite():
            dict=i
            ta.insert(END,dict['nom']+" "+dict['verbe']+" "+dict['adjectif'])
            ta.insert(END,'\n')
            
    def updateAnalyse():
        listeAnalyse=[]
        listeDictionnaires=[]
        i=1.0
        j=1.99
        while (ta.get(i,j)!=""):
            ligne=ta.get(i,j)
            i+=1.0
            j+=1.0
#transformation de la liste saisie en liste de dictionnaires pour controleur
#                for l in range(len(line)):
            nom,verbe,adjectif="","",""
            l=0
            while ligne[l]!=" ":
                nom+=ligne[l]
                l+=1
            l+=1
            if l<len(ligne):
                while ligne[l]!=" ":
                    verbe+=ligne[l]
                    l+=1
                l+=1
            if l<len(ligne):
                while l<len(ligne):
                    adjectif+=ligne[l]
                    l+=1
#pour test        
            print nom
            print verbe
            print adjectif
            print l
# pas fini
            self.parent.updateAT(listeDictionnaires)
            
#remplissage du champ texte analyse a l'ouverture...avec la liste de dictionnaires recu du controleur
#---------------------------------------------------------------------------            
class ListeProjets(object):
    def __init__(self,data,parent):
        self.fen=Tk()
        self.fen.title("Projets")
        self.parent = parent
        self.data = data
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
           self.fen.destroy()
        
#----------------------------------------------------------------------------
class Liste(Listbox):
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
        
        
