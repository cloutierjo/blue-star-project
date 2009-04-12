#-*- coding: iso-8859-1 -*-

# Classe : ControleurServeur
# Projet : blue-star-project
# Auteur : Jonathan  allée


from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ModeleServeur import *

class ControleurServeur:
    #initialisation du serveur
    def __init__(self):
        server = SimpleXMLRPCServer(("localhost", 8000),
                                requestHandler=SimpleXMLRPCRequestHandler)
        server.register_introspection_functions()
    
    #méthode qui retourne la liste des projets existants    
    def getListeProjets(self):
        ModeleServeur.getListeProjet()
    
    #méthode qui sauvegarde un projet
    def sauvegarderProjet(self):
        ModeleServeur.saveProject(projet)
    
    #méthode qui retourne un projet via son ID
    def getProjet(idProjet):
        ModeleServeur.getProject(idProjet)
    
    #enregistrement des fonctions au serveur, obligé de mettre un alias???
    server.register_function(getProjet, 'getProjet')
    server.register_function(sauvegarderProjet, 'sauvegarderProjet')
    server.register_function(getListeProjets, 'getListeProjets')
        
    #tests
if __name__ == '__main__':
    pass
        