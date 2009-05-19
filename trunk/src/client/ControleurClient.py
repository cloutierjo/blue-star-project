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
        self.i.crc.updateCRC()
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
    
    def ouvrirScenario(self, strCasUsage = ""): # retourne une liste de scenario d'utilisation avec leur priorité en fonction du cas d'usage entrée
            if strCasUsage =="":
                strCasUsage = self.getCurrentNomCasUsage()
            for unCas in self.m.projet.casEtScenario.items:
                if unCas.nom == strCasUsage:
                    lesEtapes = []
                    for uneEtape in unCas.scenario.etapes:
                        lesEtapes.append(uneEtape.etapes)
                    return lesEtapes
                
    def monterEtapeScenario(self,indexAMonter):
        if self.getCurrentNomCasUsage() != None:
            self.getCurrentCasUsage().scenario.etapes[indexAMonter].ordre -=1
            self.getCurrentCasUsage().scenario.etapes[indexAMonter-1].ordre +=1
            self.getCurrentCasUsage().scenario.refaireOrdreNumerique()
        else:
            self.i.afficherUnMessage("Veuillez svp Selectionner un cas d'usage")
            
    def descendreEtapeScenario(self,indexADescendre):
        if self.getCurrentNomCasUsage() != None:
            self.getCurrentCasUsage().scenario.etapes[indexADescendre].ordre +=1
            self.getCurrentCasUsage().scenario.etapes[indexADescendre+1].ordre -=1
            self.getCurrentCasUsage().scenario.refaireOrdreNumerique()
        else:
            self.i.afficherUnMessage("Veuillez svp Selectionner un cas d'usage")
    
    def supprimerEtapsScenario(self,indexASupprimer):
        if self.getCurrentNomCasUsage() != None:
            lesEtapes = self.getCurrentCasUsage().scenario.etapes
            lesEtapes.remove(lesEtapes[indexASupprimer])
            self.getCurrentCasUsage().scenario.refaireOrdreNumerique()
        else:
            self.i.afficherUnMessage("Veuillez svp Selectionner un cas d'usage")  
              
    def renommerEtapsScenario(self,indexARenommer,nouveauNom):
        if self.getCurrentNomCasUsage() != None:
            lesEtapes = self.getCurrentCasUsage().scenario.etapes
            lesEtapes[indexARenommer].etapes = nouveauNom
            self.getCurrentCasUsage().scenario.refaireOrdreNumerique()
        else:
            self.i.afficherUnMessage("Veuillez svp Selectionner un cas d'usage")
    
    def ajouterEtapeScenario(self,nomNouveau):
        if self.getCurrentNomCasUsage() != None:
            self.getCurrentCasUsage().scenario.addEtapeScenario(nomNouveau)
            self.getCurrentCasUsage().scenario.refaireOrdreNumerique()
        else:
            self.i.afficherUnMessage("Veuillez svp Selectionner un cas d'usage")    
    
    def getCurrentNomCasUsage(self):
        if self.i.casUsage !=None:  
            return self.i.casUsage.DerniereSelection
        
        return ""
        
    def getCurrentCasUsage(self):
        for unCas in self.m.projet.casEtScenario.items:
            if unCas.nom == self.getCurrentNomCasUsage():
                return unCas
            
    def ouvrirCasUsages(self): # Retourne une liste de cas d'usage avec leur prioritié
        lesCasEtPriorite = []
        for unCas in self.m.projet.casEtScenario.items:
            lesCasEtPriorite.append([unCas.priorite, unCas.nom])
        lesCasEtPriorite = sorted(lesCasEtPriorite, key=operator.itemgetter(0))
        return lesCasEtPriorite
        
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
                
    def supprimerCasUsage(self,nomSuppression):
        for unCas in self.m.projet.casEtScenario.items:
            if unCas.nom == nomSuppression:
                self.m.projet.casEtScenario.items.remove(unCas)
                self.i.scenario.remplirListe()
                
    def ajouterCasUsage(self,nomNouveau):     
        for unCas in self.m.projet.casEtScenario.items:
            if unCas.nom == nomNouveau:
                return False;
        else:
            self.m.projet.casEtScenario.addCasUsage(nomNouveau)
            return True;
        
    def ouvrirDicDonneeVar(self):
        return self.m.projet.dictDonne.variable
    
    def ouvrirDicDonneeFonc(self):
        return self.m.projet.dictDonne.fonction
    
    def createNewCrc(self,nom):
        if self.m.projet.crc.addCrc(nom):
            return 0
        else:
            return 1
    def updateCrc(self,crc):
        self.m.projet.crc.updateCrc(crc)
    
    def getListeCRC(self):
        return self.m.projet.crc.getClassName()
    
    def getCRC(self,nom):
        return self.m.projet.crc.getClass(nom)
    
    def createNewUser(self,nom):
        self.m.projet.user.user.append(nom)
                 
if __name__ == '__main__':
    c = ControleurClient()
