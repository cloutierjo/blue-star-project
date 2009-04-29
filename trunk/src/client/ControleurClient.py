#-*- coding: iso-8859-1 -*-
import sys
sys.path.append( "../commun" )
sys.path.append( "Vue" )
import Projet
from ModeleClient import *
import xmlrpclib
from vue import *

class ControleurClient:
    def __init__(self):
        self.m = ModeleClient()
        self.i = Vue(self)
        self.server = None
        self.url = "http://localhost:8000/"
        self.connecter()
        self.afficherInterface()
        
    def connecter(self):
        self.server = xmlrpclib.ServerProxy(self.url, allow_none=True) #allow none permet de passer des donnes nulle dans la serialisation
        
        
    def ouvrirProjet(self,projetId):
         self.m.projet = Projet.Projet()
         self.m.projet.deserialize(self.server.getProjet(projetId))
    
    
    def afficherInterface(self):
        self.i.menuPrincipal()
        self.i.root.mainloop()
        
        
        
    def creerProjet(self,nom):
        self.m.creerProjet(nom)
        self.i.chargerEnMemoireProjet()
        self.m.projet.num = self.sauvegarder()
        
    
    def getListeProjets(self):
        return  self.server.getListeProjets()
    
    
    def sauvegarder(self):
        self.i.mandat.updateMandat()
        self.i.ATExplicite.updateAnalyse()
        self.i.ATImplicite.updateAnalyse()
        self.m.projet.unicodize()
        return self.server.sauvegarderProjet(self.m.projet.serialize())
    
    
    def creerMandat(self,mandat):
        self.m.projet.mandat = mandat
        
        
    def ouvrirMandat(self):
        return self.m.projet.mandat
    
    def quitter(self):
        sys.exit(0)
        
        
    def creerATImplicite(self,dictATImplicite):
        self.m.projet.analyseImplicite.analyse = []
        for i in dictATImplicite:
            self.m.projet.addItemAnalyseImplicite(i['nom'],i['verbe'],i['adjectif'])
        
        
    def ouvrirATImplicite(self):
        return self.m.projet.analyseImplicite.analyse
    
    
    def creerATExplicite(self,dictATExplicite):
        self.m.projet.analyseExplicite.analyse = []
        for i in dictATExplicite:
            self.m.projet.addItemAnalyseExplicite(i['nom'],i['verbe'],i['adjectif'])
        
        
    def ouvrirATExplicite(self):
        return self.m.projet.analyseExplicite.analyse
    
    def afficherMenu(self):
        if c.m.projet == None:  
            print "1.Ouvrir Projet"
            print "2.Nouveau Projet"
        else:
            if c.m.projet.mandat == None:  
                print "3.Creer Mandat"
            else:
                print "3.Voir Mandat"
            
            if c.m.projet.analyseExplicite:
                print "4.Voir Analyse Explicite"
            else:
                print "4.Creer Analyse Explicite"
                
            if c.m.projet.analyseImplicite:
                print "5.Voir Analyse Implicite"
            else:
                print "5.Creer Analyse Implicite"
                
                
            print "6.Sauvegarder"
            print "7.Quitter"
            
        return raw_input("Entrer votre choix")
            
         
if __name__ == '__main__':
    c = ControleurClient()
''' choix = c.afficherMenu()
    while choix !="7":
        if choix =="1":
            print c.getListeProjets()
            c.ouvrirProjet(raw_input("Entrer id Projet"))
            
        elif choix =="2":
            c.creerProjet(raw_input("Entrer le Nom du Projet a creer"))
            
            
        elif choix =="3":
            if c.m.projet.mandat == None:  
                c.creerMandat(raw_input("Entrer le mandat"))
            else:
                print c.ouvrirMandat()
        
        
        elif choix =="4":
            if c.m.projet.analyseExplicite:
                print c.ouvrirATExplicite()
            else:
                c.creerATExplicite(raw_input("Entrer l'explicite"))
         
         
        elif choix =="5":
            if c.m.projet.analyseImplicite:
                print c.ouvrirATImplicite()
            else:
                c.creerATImplicite(raw_input("Entrer l'implicite"))
           
        elif choix =="6":
            c.sauvegarder()
            
        choix = c.afficherMenu()
 '''       