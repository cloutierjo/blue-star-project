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
def getListeProjets():
    return ms.getListeProjet()
    
#m�thode qui sauvegarde un projet
def sauvegarderProjet(self, projetSerial):
    p = Projet()
    p.deserialize(projetSerial)#on retourne le projet d�s�rializ� a francois pour le save
                               #dans la db
    
    return ms.saveProject(p) 

#m�thode qui retourne un projet via son ID
def getProjet(idProjet):
    return ms.getProject(idProjet).serialize()#on prend un projet serializ� pour le passer sur le web ou en local
                                              #on peut pas passer une instance de clase sur le web
    
print "Methodes cr�es"

#enregistrement des fonctions au serveur, oblig� de mettre un alias???
server.register_function(getProjet, 'getProjet')
server.register_function(sauvegarderProjet, 'sauvegarderProjet')
server.register_function(getListeProjets, 'getListeProjets')

print "Main m�thodes enr"



##########################################################
#M�THODE DE TEST PAS TOUCHE
def additionner_tout(x,y):
    return x+y
    
server.register_function(additionner_tout, 'additionne')
##########################################################



print "Test m�thodes enr"

print "Serveur demarr�"
    
server.serve_forever()# la main loop du serveur
print "Serveur down"

#UTILISER LE FAKE CLIENT POUR FAIRE LES TESTS
    
        