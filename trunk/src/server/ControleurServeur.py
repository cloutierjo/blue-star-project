#-*- coding: iso-8859-1 -*-

# Classe : ControleurServeur
# Projet : blue-star-project
# Auteur : Jonathan Hall�e


from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ModeleServeur import *

class ControleurServeur:
    #initialisation du serveur
    def __init__(self):
        server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=SimpleXMLRPCRequestHandler)
        server.register_introspection_functions()
        
        server.serve_forever()# la main loop du serveur
        ms = ModeleServeur()# instance du modele c�t� serveur
    
    #m�thode qui retourne la liste des projets existants    
    def getListeProjets(self):
        ms.getListeProjet()
    
    #m�thode qui sauvegarde un projet
    def sauvegarderProjet(self):
        ms.saveProject(projet)
    
    #m�thode qui retourne un projet via son ID
    def getProjet(idProjet):
        ms.getProject(idProjet)
    
    #enregistrement des fonctions au serveur, oblig� de mettre un alias???
    server.register_function(getProjet, 'getProjet')
    server.register_function(sauvegarderProjet, 'sauvegarderProjet')
    server.register_function(getListeProjets, 'getListeProjets')
        
    #tests
if __name__ == '__main__':
    pass
        