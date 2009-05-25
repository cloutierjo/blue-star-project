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
from Planning import *

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
#L'objet graphique CRC
        self.crc = None
        self.crc2 = None
#L'objet graphique scrum
        self.scrum = None
        
#L'objet graphique planning
        self.planning = None
#Haut    
    def menuPrincipal(self):
        #cree une barre de menu (qui est aussi un objet Menu)
        menu = Menu(self.root)
        #assigne cette barre a la fenetre
        self.root.config(menu=menu)
        
        self.filemenu = Menu(menu)
        #menu 
        menu.add_cascade(label=u"Fichier", menu=self.filemenu)
        #Nouveau projet
        self.filemenu.add_command(label=u"Nouveau projet", command=self.NouveauProjet)
        #projet
        self.filemenu.add_command(label=u"Ouvrir Projet", command=self.OuvrirProjet)
        
        self.filemenu.add_command(label=u"Sauvegarder", command=self.save)
        
        self.filemenu.add_command(label=u"Fermer le projet", command=self.fermerProjet)
        self.filemenu.add_separator()
        
        self.filemenu.add_command(label=u"Nouvel utilisateur", command=self.users)
        
        self.filemenu.entryconfig(6,state=DISABLED)
        
        self.filemenu.add_separator()
        #quitter
        self.filemenu.add_command(label=u"Quitter", command=self.parent.quitter)
        
        
        #Aide
        helpmenu = Menu(menu)
        menu.add_cascade(label=u"Aide", menu=helpmenu)
        helpmenu.add_command(label=u"À propos de ...", command = self.propos)
        

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
        self.planning = Planning(self,self.crc,self.parent.getListeSprints())
        self.scrum = ScrumView(self,self.parent.getLstScrum())
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
        #self.graphItems.append(self.planning)  # a voir avec mathieu et pascal
        self.graphItems.append(self.scrum)
        
#####ajouter autres widgets dans graphItems ici...
        
    def NouveauProjet(self):
         if self.etat==0:
            nom=tkSimpleDialog.askstring(u'Nom de projet',
                                         u'Entrez un nom pour le projet:', 
                                                    parent=self.root)
            if nom:
                self.parent.creerProjet(nom)
                self.root.title(u"Blue Star        "+nom)
                self.etat=1
                #affichage des onglets
                self.onglets.frame.pack()
                self.filemenu.entryconfig(6,state=NORMAL)
                
    def users(self):
        nom=tkSimpleDialog.askstring(u'Nouvel utilisateur',
                                     u'Entrez le nom:',parent=self.root)
        if nom:
            self.parent.createNewUser(nom)
            self.crc.updateListeUser()
            self.crc2.updateListeUser()
            self.scrum.updateListeUser()
    
    def propos(self):
        self.fen = Toplevel()
        self.fen.title(u"This is...")
        
        self.fen.grab_set()
        self.fen.focus_set()
        
        self.frame2 = Frame(self.fen);
        txtFont = tkFont.Font(size=25)
        titre = Label(self.frame2, 
                      text=u"Blue Star Project",
                      font=txtFont)
        titre.pack()
        doByPeople = Label(self.frame2, text=u"\nFait par:   Jonathan Hallée\n\tFrançois Lahey\n\t               Jonatan Cloutier St-Jean\n\t Mathieu Lavoie\n\tPascal Lemay\n\t   Jean-Philippe Chan")
        doByPeople.pack()
        texteCours = Label(self.frame2, text=u"\nPour le cours B41")
        texteCours.pack()
        self.frame2.pack()
    
    def effacerFenetre(self):
        for item in self.graphItems:
            item.frame.pack_forget()
        self.planning.cacher()  # a voir avec mathieu et pascal ??
                
    def fermerProjet(self):
        self.effacerFenetre()
        self.onglets.v.set(0)
        self.onglets.frame.pack_forget()
        self.root.title(u"Blue Star")
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
            tkMessageBox.showinfo(u"Message",u"Aucun projet n'est ouvert")
            
    #analyse explicite et implicite       
    def afficherLesAnalyses(self):
        if self.etat==1:
            #efface la fenetre avant affichage desiree
            self.effacerFenetre()
            self.ATExplicite.frame.pack(padx=50,side=LEFT,fill=Y)
                                        #was right
            self.ATImplicite.frame.pack(side=LEFT,padx=50,fill=Y)
        else:
            tkMessageBox.showinfo(u"Message",u"Aucun projet n'est ouvert")
            
    #analyse implicite/cas d'usage
    def afficherCasUsage(self):
        if self.etat==1:
            #efface la fenetre avant affichage desiree
            self.effacerFenetre()
            self.ATImplicite.frame.pack(padx=50,side=LEFT,fill=Y)
            #code affichage cas usage a venir ici
            self.casUsage.frame.pack(side=LEFT,padx=50,fill=Y)
        else:
            tkMessageBox.showinfo(u"Message",u"Aucun projet n'est ouvert")
    
    #cas d'usage et scenario...        
    def afficherScenario(self):
        if self.etat==1:
            #efface la fenetre avant affichage desiree
            self.effacerFenetre()
            self.casUsage.frame.pack(side=LEFT,padx=50,fill=Y)
            self.scenario.frame.pack(side=LEFT,padx=50,fill=Y)
        else:
            tkMessageBox.showinfo(u"Message",u"Aucun projet n'est ouvert")
    
    #dictionnaire de données
    #cas d'usage et scenario...        
    def afficherDictionnaire(self):
        if self.etat==1:
            #efface la fenetre avant affichage desiree
            self.effacerFenetre()
            self.scenario.frame.pack(side=LEFT,padx=50,fill=Y)
            self.dictionnaireDonnee.frame.pack(side=LEFT, pady=30)
        else:
            tkMessageBox.showinfo(u"Message",u"Aucun projet n'est ouvert")
            
    def afficherCRC(self):
        if self.etat==1:
            self.effacerFenetre()
            #self.crc.frame.pack(side=LEFT,padx=30)
            self.dictionnaireDonnee.frame.pack(side=LEFT, pady=30)
            self.crc.frame.pack(anchor=W,padx=30,pady=15)
            self.crc2.frame.pack(anchor=W,padx=30,pady=15)
        else:
            tkMessageBox.showinfo(u"Message",u"Aucun projet n'est ouvert")
            
    def afficherPlanning(self):
        if self.etat==1:
            self.effacerFenetre()
            self.planning.afficher()
        else:
            tkMessageBox.showinfo(u"Message",u"Aucun projet n'est ouvert")

    def afficherScrum(self):
        if self.etat==1:
            self.effacerFenetre()
            self.scrum.frame.pack(side=LEFT,padx=30)
        else:
            tkMessageBox.showinfo(u"Message",u"Aucun projet n'est ouvert")

    def afficherUnMessage(self,Texte,erreur=u"ERREUR!!!"):
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
        r=Radiobutton(self.frame, text=u"Mandat/Analyse Explicite",variable=self.v, value=1,command=self.vueParent.afficherFenMandat)
                        # config + indicatoron=0 (a determiner)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        r=Radiobutton(self.frame, text=u"Analyse Explicite/Implicite", variable=self.v, value=2,command=self.vueParent.afficherLesAnalyses)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        r=Radiobutton(self.frame, text=u"Analyse Explicite/Cas d'usage", variable=self.v, value=3,command=self.vueParent.afficherCasUsage)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        r=Radiobutton(self.frame, text=u"Cas d'usage/Scenario d'utilisation", variable=self.v, value=4,command=self.vueParent.afficherScenario)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        r=Radiobutton(self.frame, text=u"Dictionnaire de donnée", variable=self.v, value=5,command=self.vueParent.afficherDictionnaire)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        
        #tempo
        r=Radiobutton(self.frame, text=u"CRC", variable=self.v, value=7,command=self.vueParent.afficherCRC)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        
        r=Radiobutton(self.frame, text=u"Planning", variable=self.v, value=8,command=self.vueParent.afficherPlanning)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        
        r=Radiobutton(self.frame, text=u"Scrum", variable=self.v, value=9,command=self.vueParent.afficherScrum)
        r.config(activeforeground="blue",relief=RIDGE)
        r.pack(side=LEFT)
        
        #autres onglets a suivre...
        self.v.set(0)

        
