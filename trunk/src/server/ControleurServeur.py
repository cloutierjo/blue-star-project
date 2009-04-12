#-*- coding: iso-8859-1 -*-

# Classe : ControleurServeur
# Projet : blue-star-project
# Auteur : Jonathan Hallée


from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ModeleServeur import *

class ControleurServeur:
    #initialisation du serveur
    def __init__(self):
        self.server = SimpleXMLRPCServer(("192.168.1.40", 8000), requestHandler=SimpleXMLRPCRequestHandler)
        self.server.register_introspection_functions()
        
        self.server.serve_forever()# la main loop du serveur
        self.ms = ModeleServeur()# instance du modele côté serveur
    
    #méthode qui retourne la liste des projets existants    
    def getListeProjets(self):
        return ms.getListeProjet()
    
    #méthode qui sauvegarde un projet
    def sauvegarderProjet(self):
        return ms.saveProject(projet)
    
    #méthode qui retourne un projet via son ID
    def getProjet(idProjet):
        return ms.getProject(idProjet)
    
    #enregistrement des fonctions au serveur, obligé de mettre un alias???
    self.server.register_function(getProjet, 'getProjet')
    self.server.register_function(sauvegarderProjet, 'sauvegarderProjet')
    self.server.register_function(getListeProjets, 'getListeProjets')
        
    #tests
if __name__ == '__main__':
    pass
        