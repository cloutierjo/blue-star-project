#-*- coding: iso-8859-1 -*-

# Classe : ControleurServeur
# Projet : blue-star-project
# Auteur : Jonathan Hallée

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ModeleServeur import *

server = SimpleXMLRPCServer(("localhost", 8000), 
                            requestHandler=SimpleXMLRPCRequestHandler)
server.register_introspection_functions()
        
print "Serveur crée"

ms = ModeleServeur()# instance du modele côté serveur

print "Modele serveur crée"
    
#méthode qui retourne la liste des projets existants    
def getListeProjets(self):
    getListeProjet()
    
#méthode qui sauvegarde un projet
def sauvegarderProjet(self):
    saveProject(projet)
    
#méthode qui retourne un projet via son ID
def getProjet(idProjet):
    getProject(idProjet)
    
print "Methodes crées"
    
#enregistrement des fonctions au serveur, obligé de mettre un alias???
server.register_function(getProjet, 'getProjet')
server.register_function(sauvegarderProjet, 'sauvegarderProjet')
server.register_function(getListeProjets, 'getListeProjets')

print "Main méthodes enr"

#MÉTHODE DE TEST PAS TOUCHE
def additionner_tout(x,y):
    return x + y
    
server.register_function(additionner_tout, 'additionne')

print "Test méthodes enr"

print "Serveur demarré"

if __name__ == '__main__':
    s = xmlrpclib.ServerProxy("http://localhost:8000/")
    
    print s.additionne(2,3)
    a = raw_input()
    
server.serve_forever()# la main loop du serveur
    
        