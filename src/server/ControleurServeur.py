#-*- coding: iso-8859-1 -*-

# Classe : ControleurServeur
# Projet : blue-star-project
# Auteur : Jonathan Hall�e

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
        
print "Serveur cr�e"

ms = ModeleServeur()# instance du modele c�t� serveur

print "Modele serveur cr�e"

#m�thode qui retourne la liste des projets existants
class ServerMethods:
        
    def getListeProjets(self):
        return ms.getListeProjet()
        
    #m�thode qui sauvegarde un projet
    def sauvegarderProjet(self, serializedProjet):
        
        p = Projet()
        p.deserialize(serializedProjet) #on retourne le projet d�s�rializ� a francois pour le save
                                        #dans la db
        
        return ms.saveProject(p)
    
    #m�thode qui retourne un projet via son ID
    def getProjet(self, idProjet):
        return ms.getProject(idProjet).serialize()#on prend un projet serializ� pour le passer sur le web ou en local
                                                  #on peut pas passer une instance de clase sur le web
                                                  
    def additionne(self, x,y):
        return x+y
    
server.register_instance(ServerMethods())

print "Serveur demarr�"
    
server.serve_forever()# la main loop du serveur

print "Serveur down"

       