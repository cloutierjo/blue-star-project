#-*- coding: iso-8859-1 -*-

# Classe : ControleurServeur
# Projet : blue-star-project
# Auteur : Jonathan Hall�e

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ServerMethods import *

#serveur localhost sur le port 8000 (bidon le num�ro de port)
server = SimpleXMLRPCServer(("localhost", 8000), 
                            requestHandler=SimpleXMLRPCRequestHandler)
        
print "Serveur cr�e"

#Enregistrement des m�thodes du serveur a partir de ma classe externe
server.register_instance(ServerMethods())

print "M�thodes enregistr�e"
print "Serveur demarr�"
    
server.serve_forever()# la main loop du serveur

print "Serveur down"    