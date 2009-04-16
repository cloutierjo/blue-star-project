import sys
sys.path.append( "../server" )
import Projet
from ModeleClient import *
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class ControleurClient:
    def __init__(self):
        self.m = ModeleClient()
        #self.i = Interface()
        self.server = None
        self.url = "http://localhost:8000/"
        self.connecter()
        #self.afficherInterface()
        
    def connecter(self):
        self.server = xmlrpclib.ServerProxy(self.url)
        
        
    def ouvrirProjet(self,projetId):
         self.m.projet = Projet.Projet()
         self.m.projet.deserialize(self.server.getProjet(projetId))
    
    
    def afficherInterface(self):
        i.root.mainloop()
        
        
    def creerProjet(self,nom):
        self.m.creerProjet(nom)
        self.m.projet.num = self.sauvegarder()
        
    
    def getListeProjets(self):
        return  self.server.getListeProjets()
    
    
    def sauvegarder(self):
        self.m.projet.unicodize()
        return self.server.sauvegarderProjet(self.m.projet.serialize())
    
    
    def creerMandat(self,mandat):
        self.m.projet.mandat = mandat
        
        
    def ouvrirMandat(self):
        return self.m.projet.mandat
    
    
    def creerATImplicite(self,analyseImplicite):
        self.m.projet.analyseImplicite = analyseImplicite
        
        
    def ouvrirATImplicite(self):
        return self.m.projet.analyseImplicite
    
    
    def creerATExplicite(self,analyseExplicite):
        self.m.projet.analyseExplicite = analyseExplicite
        
        
    def ouvrirATExplicite(self):
        return self.m.projet.analyseExplicite
    
    
if __name__ == '__main__':
    c = ControleurClient()
    print c.getListeProjets()
    c.ouvrirProjet(raw_input("Entrer id Projet"))
    print "projet nomme ",c.m.projet.nom, "loadee"
    print c.ouvrirMandat()
    #print c.m.projet.analyseExplicite
    #print c.m.projet.analyseImplicite
    #c.creerMandat("Nouveau Mandat Joyeux")
    #print c.sauvegarder()
        