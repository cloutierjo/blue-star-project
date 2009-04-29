#-*- coding: iso-8859-1 -*-
'''
classe vue
auteur: Pascal Lemay
            '''
from Tkinter import*
import tkMessageBox, tkSimpleDialog
import sys
sys.path.append( "../../commun" )
import Projet
from Mandat import *
from AnalyseTextuelle import *
from Liste import *

class Vue(object):
#initialisation
    def __init__(self,parent):
        self.parent=parent
        #0:Aucun Project loade,    1:Projet Loade
        self.etat=0

        self.root=Tk()
        self.root.title("Blue Star")
        self.root.geometry("1024x768")
        
# toute les composantes graphiques
        self.graphItems=[]
        
#L'objet graphique Mandat
        self.mandat = None
        
#L'objet graphique des  AT
        self.ATImplicite = None
        self.ATExplicite = None
#L'objet graphique cas d'usage
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
        displaymenu.add_command(label="Afficher le mandat / analyse explicite",command=self.afficherFenMandat)
        displaymenu.add_command(label="Afficher analyse explicite / implicite",command=self.afficherLesAnalyses)
        #...
        
        #Aide
        helpmenu = Menu(menu)
        menu.add_cascade(label="Aide", menu=helpmenu)
        

#fonction sur l'ouverture projet
    def OuvrirProjet(self):
        if self.etat==0:
            projets=ListeProjets(self.parent.getListeProjets(),self)

    def chargerEnMemoireProjet(self):
        self.mandat=Mandat(self,self.parent.ouvrirMandat())
        self.ATExplicite = analyseTextuelle(self,self.parent.ouvrirATExplicite(),explicite=True)
        self.ATImplicite = analyseTextuelle(self,self.parent.ouvrirATImplicite(),implicite=True)
#####charger autres widjet ici...

        #reference a chaque objets graphiques ajoutes ici pour faciliter
        #la permutation entre les affichage (voir methode effacerFenetre())
        self.graphItems.append(self.mandat)
        self.graphItems.append(self.ATExplicite)
        self.graphItems.append(self.ATImplicite)
#####ajouter autres widgets dans graphItems ici...
        
    def NouveauProjet(self):
         if self.etat==0:
            nom=tkSimpleDialog.askstring('Nom de projet',
                                     'Entrez un nom pour le projet:', 
                                                    parent=self.root)
            if nom:
                self.parent.creerProjet(nom)
                self.etat=1
                
    def effacerFenetre(self):
        for item in self.graphItems:
                item.frame.pack_forget()
                
    def fermerProjet(self):
        self.effacerFenetre()
        self.etat=0
    
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
            self.ATExplicite.frame.pack(side=RIGHT,fill=Y)
        else:
            tkMessageBox.showinfo("Message","Aucun projet n'est ouvert")
            
    #analyse explicite et implicite       
    def afficherLesAnalyses(self):
        if self.etat==1:
            #efface la fenetre avant affichage desiree
            self.effacerFenetre()
                
            if self.ATExplicite != None:
                self.ATExplicite.frame.pack(padx=60,side=LEFT,fill=Y)
            if self.ATImplicite != None:
                self.ATImplicite.frame.pack(side=RIGHT,padx=60,fill=Y)
        else:
            tkMessageBox.showinfo("Message","Aucun projet n'est ouvert")

        
