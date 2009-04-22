#-*- coding: iso-8859-1 -*-

# Classe : ControleurServeur
# Projet : blue-star-project
# Auteur : Jonathan Hallée

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ServerMethods import *

#serveur localhost sur le port 8000 (bidon le numéro de port)
server = SimpleXMLRPCServer(("localhost", 8000), 
                            requestHandler=SimpleXMLRPCRequestHandler)
        
print "Serveur crée"

#Enregistrement des méthodes du serveur a partir de ma classe externe
server.register_instance(ServerMethods())

print "Méthodes enregistrée"
print "Serveur demarré"
    
server.serve_forever()# la main loop du serveur

print "Serveur down"    