#-*- coding: iso-8859-1 -*-

# Classe : ControleurServeur
# Projet : blue-star-project
# Auteur : Jonathan Hall�e

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ModeleServeur import *

server = SimpleXMLRPCServer(("localhost", 8000), 
                            requestHandler=SimpleXMLRPCRequestHandler)
server.register_introspection_functions()
        
print "Serveur cr�e"

ms = ModeleServeur()# instance du modele c�t� serveur

print "Modele serveur cr�e"
    
#m�thode qui retourne la liste des projets existants    
def getListeProjets(self):
    getListeProjet()
    
#m�thode qui sauvegarde un projet
def sauvegarderProjet(self):
    saveProject(projet)
    
#m�thode qui retourne un projet via son ID
def getProjet(idProjet):
    getProject(idProjet)
    
print "Methodes cr�es"
    
#enregistrement des fonctions au serveur, oblig� de mettre un alias???
server.register_function(getProjet, 'getProjet')
server.register_function(sauvegarderProjet, 'sauvegarderProjet')
server.register_function(getListeProjets, 'getListeProjets')

print "Main m�thodes enr"

#M�THODE DE TEST PAS TOUCHE
def additionner_tout(x,y):
    return x + y
    
server.register_function(additionner_tout, 'additionne')

print "Test m�thodes enr"

print "Serveur demarr�"

if __name__ == '__main__':
    s = xmlrpclib.ServerProxy("http://localhost:8000/")
    
    print s.additionne(2,3)
    a = raw_input()
    
server.serve_forever()# la main loop du serveur
    
        