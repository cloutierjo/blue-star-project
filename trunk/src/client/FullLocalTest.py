#-*- coding: iso-8859-1 -*-
import sys
sys.path.append("../server")

import ControleurClient
import ServerMethods
import ModeleServeur
import sqlite3


'''
fichier starter qui permet de tout tester sans XMLRPC et donc 
d'avoir les message d'erreur et les exceptions lancé coté serveur. 
il n'y a qu'a lancé ce fichier pour cela. 
FAIRE ATTENTION, LE LOGICIEL N'EST PAS SENCÉ ETRE UTILISÉ DE CETTE MANIÈRE LA,
CE N'EST DONC QU'A DES FIN DE TESTS
'''
def localConnect(self):
    self.server = ServerMethods.ServerMethods()
    

def bdinit(self):    
    self.db = '../server/test1.db'                    # cheminFichierDB
    self.con = sqlite3.connect(self.db)     # Connecteur

if __name__ == '__main__':
    ControleurClient.ControleurClient.connecter=localConnect
    ModeleServeur.ModeleServeur.__init__=bdinit
    ServerMethods.ms=ModeleServeur.ModeleServeur()
    print "ATTENTION logiciel partie sans module réseau (RPC)"
    cc=ControleurClient.ControleurClient()