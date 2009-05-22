#-*- coding: iso-8859-1 -*-
'''
classe vue
auteur: Pascal Lemay
            '''
from Tkinter import *
import tkFont
import tkMessageBox, tkSimpleDialog
import sys
sys.path.append( "../../commun" )
import Projet
from Mandat import *
from AnalyseTextuelle import *
from CasUsageVue import *
from ScenarioVue import *
from DictionnaireDonnee import *
from CRCVue import *
from Liste import *
from ScrumView import *
import Tix

class Vue(object):
#initialisation
    def __init__(self,parent):
        self.parent=parent
        #0:Aucun Project loade,    1:Projet Loade
        self.etat=0

        self.root=Tix.Tk()
        self.root.title("Blue Star")
        self.root.geometry("1024x768")
        
        
#Onglet pour affichage
        self.onglets=Onglets(self)
        
# toute les composantes graphiques
        self.graphItems=[]
        
#L'objet graphique Mandat
        self.mandat = None
        
#L'objet graphique des  AT
        self.ATImplicite = None
        self.ATExplicite = None
#L'objet graphique cas d'usage
        self.casUsage = None
        self.scenario = None
#L'objet graphique dictionnaire de données
        self.dictionnaireDonnee = None
#Objets graphiques CRC
        self.crc = None
        self.crc2=None
#Lobjet graphique scrum
        self.scrum = None
#Haut    
    def menuPrincipal(self):
        #cree une barre de menu (qui est aussi un objet Menu)
        menu = Menu(self.root)
        #assigne cette barre a la fenetre
        self.root.config(menu=menu)
        
        self.filemenu = Menu(menu)
        #menu 
        menu.add_cascade(label="Fichier", menu=self.filemenu)
        #Nouveau projet
        self.filemenu.add_command(label="Nouveau projet", command=self.NouveauProjet)
        #projet
        self.filemenu.add_command(label="Ouvrir Projet", command=self.OuvrirProjet)
        
        self.filemenu.add_command(label="Sauvegarder", command=self.save)
        
        self.filemenu.add_command(label="Fermer le projet", command=self.fermerProjet)
        self.filemenu.add_separator()
        
        self.filemenu.add_command(label="Nouvel utilisateur", command=self.users)
        
        self.filemenu.entryconfig(6,state=DISABLED)
        
        self.filemenu.add_separator()
        #quitter
        self.filemenu.add_command(label="Quitter", command=self.parent.quitter)
        
        
        #commandes de l'affichage
        displaymenu=Menu(menu)
        menu.add_cascade(label="Affichage",menu=displaymenu)
        #displaymenu.add_command(label="Afficher le mandat / analyse explicite",command=self.afficherFenMandat)
        #displaymenu.add_command(label="Afficher analyse explicite / implicite",command=self.afficherLesAnalyses)
        #...
        
        #Aide
        helpmenu = Menu(menu)
        menu.add_cascade(label="Aide", menu=helpmenu)
        helpmenu.add_command(label="À propos de ...", command = self.propos)
        

#fonction sur l'ouverture projet
    def OuvrirProjet(self):
        if self.etat==0:
            projets=ListeProjets(self.parent.getListeProjets(),self)

    def chargerEnMemoireProjet(self):
        self.mandat=Mandat(self,self.parent.ouvrirMandat())
        self.ATExplicite = AnalyseTextuelle(self,self.parent.ouvrirATExplicite(),explicite=True)
        self.ATImplicite = AnalyseTextuelle(self,self.parent.ouvrirATImplicite(),implicite=True)
        self.scenario = ScenarioVue(self)
        self.casUsage = CasUsageVue(self)
        self.dictionnaireDonnee = DictionnaireDonnee(self, self.parent.ouvrirDicDonneeVar(), self.parent.ouvrirDicDonneeFonc())
        self.crc = CrcVUE(self,self.parent.getListeCRC())
        self.crc2 = CrcVUE(self,self.parent.getListeCRC())
        #self.scrum = ScrumView(self,self.parent.getListeCRC())
#####charger autres objets graphiques ici...

        
        #reference a chaque objets graphiques ajoutes ici pour faciliter
        #la permutation entre les affichages (voir methode effacerFenetre())
        self.graphItems.append(self.mandat)
        self.graphItems.append(self.ATExplicite)
        self.graphItems.append(self.ATImplicite)
        self.graphItems.append(self.casUsage)
        self.graphItems.append(self.scenario)
        self.graphItems.append(self.dictionnaireDonnee)
        self.graphItems.append(self.crc)
        self.graphItems.append(self.crc2)
        #self.graphItems.append(self.scrum)
        
#####ajouter autres widgets dans graphItems ici...
        
    def NouveauProjet(self):
         if self.etat==0:
            nom=tkSimpleDialog.askstring('Nom de projet',
                                         'Entrez un nom pour le projet:', 
                                                    parent=self.root)
            if nom:
                self.parent.creerProjet(nom)
                self.root.title("Blue Star        "+nom)
                self.etat=1
                #affichage des onglets
                self.onglets.frame.pack()
                self.filemenu.entryconfig(6,state=NORMAL)
                
    def users(self):
        nom=tkSimpleDialog.askstring('Nouvel utilisateur',
                                     'Entrez le nom:',parent=self.root)
        if nom:
            self.parent.createNewUser(nom)
            self.crc.updateListeUser()
    
    def propos(self):
        self.fen = Toplevel()
        self.fen.title("This is :")
        self.fen.resizable(False,False)
        
        self.fen.grab_set()
        self.fen.focus_set()
        
        self.frame2 = Frame(self.fen);
        txtFont = tkFont.Font(size=25)
        titre = Label(self.frame2, 
                      text="Blue Star Project",
                      font=txtFont)
        titre.pack()
        doByPeople = Label(self.frame2, text= "\nFait par:\nJonathan Hallée,\nFrançois Lahey,\nJonatan Cloutier St-Jean,\nMathieu Lavoie,\nPascal Lemay,\nJean-Philippe Chan")
        doByPeople.pack()
        texteCours = Label(self.frame2, text="\nPour le cours B41")
        texteCours.pack()
        self.frame2.pack()
    
    def effacerFenetre(self):
        for item in self.graphItems:
            item.frame.pack_forget()
                
    def fermerProjet(self):
        self.effacerFenetre()
        self.onglets.v.set(0)
        self.onglets.frame.pack_forget()
        self.root.title("Blue Star")
        self.etat=0
        self.filemenu.entryconfig(6,state=DISABLED)
    
    def save(self):
        #si projet ouvert
        if self.etat !=0:
            self.parent.sauvegarder()
            
#affichages

    #mandat et analyse explicite
    def afficherFenMandat(self):
        if self.etat==1:
            #efface la fenetre avant affichage desiree
            self.effacerFenetre()
                
            self.mandat.frame.pack(side=LEFT,fill=Y)
            self.ATExplicite.frame.pack(side=LEFT,fill=Y)
        else:
            tkMessageBox.showinfo("Message","Aucun projet n'est ouvert")
            
    #analyse explicite et implicite       
    def afficherLesAnalyses(self):
        if self.etat==1:
            #efface la fenetre avant affichage desiree
            self.effacerFenetre()
            self.ATExplicite.frame.pack(padx=50,pady=10,side=LEFT,fill=Y)
                                        #was right
            self.ATImplicite.frame.pack(side=LEFT,padx=50,pady=10,fill=Y)
        else:
            tkMessageBox.showinfo("Message","Aucun projet n'est ouvert")
            
    #analyse implicite/cas d'usage
    def afficherCasUsage(self):
        if self.etat==1:
            #efface la fenetre avant affichage desiree
            self.effacerFenetre()
            self.ATImplicite.frame.pack(padx=50,pady=10,side=LEFT,fill=Y)
            #code affichage cas usage a venir ici
            self.casUsage.frame.pack(side=LEFT,padx=50,fill=Y)
        else:
            tkMessageBox.showinfo("Message","Aucun projet n'est ouvert")
    
    #cas d'usage et scenario...        
    def afficherScenario(self):
        if self.etat==1:
            #efface la fenetre avant affichage desiree
            self.effacerFenetre()
            self.casUsage.frame.pack(side=LEFT,padx=50,fill=Y)
            self.scenario.frame.pack(side=LEFT,padx=50,fill=Y)
        else:
            tkMessageBox.showinfo("Message","Aucun projet n'est ouvert")
    
    #dictionnaire de données
    #cas d'usage et scenario...        
    def afficherDictionnaire(self):
        if self.etat==1:
            #efface la fenetre avant affichage desiree
            self.effacerFenetre()
            self.scenario.frame.pack(side=LEFT,padx=50,fill=Y)
            self.dictionnaireDonnee.frame.pack(side=LEFT, pady=30)
        else:
            tkMessageBox.showinfo("Message","Aucun projet n'est ouvert")
            
    def afficherCRC(self):
        if self.etat==1:
            self.effacerFenetre()
            #self.crc.frame.pack(side=LEFT,padx=30)
            self.crc.frame.pack(anchor=W,padx=30,pady=10)
            self.crc2.frame.pack(anchor=W,padx=30,pady=10)
        else:
            tkMessageBox.showinfo("Message","Aucun projet n'est ouvert")

    def afficherScrum(self):
        pass
    '''
        if self.etat==1:
            self.effacerFenetre()
            self.Scrum.frame.pack(side=LEFT,padx=30)
        else:
            tkMessageBox.showinfo("Message","Aucun projet n'est ouvert")
            '''

    def afficherUnMessage(self,Texte,erreur="ERREUR!!!"):
        tkMessageBox.showerror(erreur, Texte)
#---------------------------------------------------------------------------
#classe Onglet 
#auteur Pascal Lemay
#p.s. Laissez cette classe ici (elle fait partie de la fenetre principale)

class Onglets(object):
    def __init__(self,vueParent):
        self.vueParent=vueParent
        
        self.frame=Frame()
        
        self.v = IntVar()
        r=Radiobutton(self.frame, text="Mandat/Analyse Explicite",variable=self.v, value=1,command=self.vueParent.afficherFenMandat)
                        # config + indicatoron=0 (a determiner)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        r=Radiobutton(self.frame, text="Analyse Explicite/Implicite", variable=self.v, value=2,command=self.vueParent.afficherLesAnalyses)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        r=Radiobutton(self.frame, text="Analyse Explicite/Cas d'usage", variable=self.v, value=3,command=self.vueParent.afficherCasUsage)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        r=Radiobutton(self.frame, text="Cas d'usage/Scenario d'utilisation", variable=self.v, value=4,command=self.vueParent.afficherScenario)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        r=Radiobutton(self.frame, text="Dictionnaire de donnée", variable=self.v, value=5,command=self.vueParent.afficherDictionnaire)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        
        r=Radiobutton(self.frame, text="CRC", variable=self.v, value=7,command=self.vueParent.afficherCRC)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        
        
        r=Radiobutton(self.frame, text="Scrum", variable=self.v, value=9,command=self.vueParent.afficherScrum)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        
        #autres onglets...
        self.v.set(0)

        
