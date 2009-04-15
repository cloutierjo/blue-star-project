#-*- coding: iso-8859-1 -*-

# Classe : ControleurServeur
# Projet : blue-star-project
# Auteur : Jonathan Hallée

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ModeleServeur import *

import sys
sys.path.append( "../server" )
from Projet import *

server = SimpleXMLRPCServer(("localhost", 8000), 
                            requestHandler=SimpleXMLRPCRequestHandler)
server.register_introspection_functions()
        
print "Serveur crée"

ms = ModeleServeur()# instance du modele côté serveur

print "Modele serveur crée"

#méthode qui retourne la liste des projets existants    
def getListeProjets():
    return ms.getListeProjet()
    
#méthode qui sauvegarde un projet
def sauvegarderProjet(serializedProjet):
    
    p = Projet()
    p.deserialize(serializedProjet) #on retourne le projet désérializé a francois pour le save
                                    #dans la db
    
    return ms.saveProject(p)

#méthode qui retourne un projet via son ID
def getProjet(idProjet):
    return ms.getProject(idProjet).serialize()#on prend un projet serializé pour le passer sur le web ou en local
                                              #on peut pas passer une instance de clase sur le web
    
print "Methodes crées"

#enregistrement des fonctions au serveur, obligé de mettre un alias???
server.register_function(getProjet, 'getProjet')
server.register_function(sauvegarderProjet, 'sauvegarderProjet')
server.register_function(getListeProjets, 'getListeProjets')

print "Main méthodes enr"



##########################################################
#MÉTHODE DE TEST PAS TOUCHE
def additionner_tout(x,y):
    return x+y
    
server.register_function(additionner_tout, 'additionne')
##########################################################



print "Test méthodes enr"

print "Serveur demarré"
    
server.serve_forever()# la main loop du serveur
print "Serveur down"

#UTILISER LE FAKE CLIENT POUR FAIRE LES TESTS
    
        