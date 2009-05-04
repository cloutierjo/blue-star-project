#-*- coding: iso-8859-1 -*-
import sys
sys.path.append("../commun")
sys.path.append("Vue")
import Projet
from ModeleClient import *
import xmlrpclib
from vue import *
import operator

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
             
    def afficherInterface(self):
        self.i.menuPrincipal()
        self.i.root.mainloop()
       
    def quitter(self):
        sys.exit(0) 
     
     
        
    def getListeProjets(self):
        return  self.server.getListeProjets()
        
    def ouvrirProjet(self, projetId):
        self.m.projet = Projet.Projet()
        self.m.projet.deserialize(self.server.getProjet(projetId))
   
    def creerProjet(self, nom):
        self.m.creerProjet(nom)
        self.i.chargerEnMemoireProjet()
        self.m.projet.num = self.sauvegarder()
        
    
    
    def sauvegarder(self):
        self.i.mandat.updateMandat()
        self.i.ATExplicite.updateAnalyse()
        self.i.ATImplicite.updateAnalyse()
        self.m.projet.unicodize()
        return self.server.sauvegarderProjet(self.m.projet.serialize())
    
    
    
    def creerMandat(self, mandat):
        self.m.projet.mandat = mandat
        
        
    def ouvrirMandat(self):
        return self.m.projet.mandat
    
    
       
    def creerATImplicite(self, dictATImplicite):
        self.m.projet.analyseImplicite.analyse = []
        for i in dictATImplicite:
            self.m.projet.analyseImplicite.addItem(i['nom'], i['verbe'], i['adjectif'], i['handled'])
        
        
    def ouvrirATImplicite(self):
        return self.m.projet.analyseImplicite.analyse
    
    
    def creerATExplicite(self, dictATExplicite):
        self.m.projet.analyseExplicite.analyse = []
        for i in dictATExplicite:
            self.m.projet.analyseExplicite.addItem(i['nom'], i['verbe'], i['adjectif'], i['handled'])
    def ouvrirATExplicite(self):
        return self.m.projet.analyseExplicite.analyse
    
    
    
    
    def ouvrirCasUsages(self): # Retourne une liste de cas d'usage avec leur prioritié
        lesCasEtPriorite = []
        for unCas in self.m.projet.casEtScenario.items:
            lesCasEtPriorite.append([unCas.priorite, unCas.nom])
        lesCasEtPriorite = sorted(lesCasEtPriorite, key=operator.itemgetter(0))
        return lesCasEtPriorite
    
    def ouvrirScenario(self,strCasUsage): # retourne une liste de scenario d'utilisation avec leur priorité en fonction du cas d'usage entrée
        return
        
    def monterPrioriteCas(self,nomCas):
         for unCas in self.m.projet.casEtScenario.items:
            if unCas.nom == nomCas:
                unCas.priorite -=1
                break
         else:
             print nomCas," non-trouvé"
    
    def descendrePrioriteCas(self,nomCas):
         for unCas in self.m.projet.casEtScenario.items:
            if unCas.nom == nomCas:
                unCas.priorite +=1
                break
         else:
             print nomCas," non-trouvé"
    
    def renommerCasUsage(self,ancienNom,nouveauNom):
        for unCas in self.m.projet.casEtScenario.items:
            if unCas.nom == ancienNom:
                unCas.nom = nouveauNom
    
if __name__ == '__main__':
    c = ControleurClient()
