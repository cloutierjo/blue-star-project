from Projet import *
from modelClient import *

class ControleurClient:
    def __init__(self):
        self.m = ModeleClient()
        self.i = Interface()
        self.server
        self.url = "http://localhost:8000/"
        self.connecter()
        self.afficherInterface()
        
    def connecter(self):
        self.server = xmlrpclib.ServerProxy(self.url)
        
        
    def ouvrirProjet(self,nom):
        self.m.projet = self.server.getProjet(nom).deserialize()
    
    
    def afficherInterface(self):
        i.root.mainloop()
        
        
    def creerProjet(self,nom):
        self.m.creerProjet(nom)
    
    
    def getListeProjets(self):
        return  self.server.getListeProjets()
    
    
    def sauvegarder(self):
        self.server.sauvegarderProjet(self.m.projet)
    
    
    def creerMandat(self,mandat):
        self.m.projet.mandat = mandat
        
        
    def ouvrirMandat(self):
        return m.projet.mandat
    
    if __name__ == '__main__':
        pass
        