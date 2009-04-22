#-*- coding: iso-8859-1 -*-

# Classe : FakeClient
# Projet : blue-star-project
# Auteur : Fran�ois Lahey

import xmlrpclib
import sys

sys.path.append( "../commun" )#le path de ce qui est commun au serveur et au client
from Projet import *

class FakeClient:
    
    def __init__(self):
        self.s = xmlrpclib.ServerProxy('http://localhost:8000/')

#Testage du serveur
if __name__ == "__main__":
    
    fc = FakeClient()
    print "Fake client"
    # Creation d'un Projet    
    p=Projet()
    p.nom="Test project"
    p.mandat="Utiliser les caract�res sp�ciaux pour tester la classe ModeleServeur"
    p.analyseExplicite.addItem("SA CRAINT","mang�","juteuses")
    p.analyseExplicite.addItem("une huitre","grignot�","baveuse")
    p.analyseExplicite.addItem("une cerise","mach�","rouge")
    p.analyseExplicite.addItem("un bourgeon","sucot�","tranquillement")
    p.analyseImplicite.addItem("un bourgeon","sucot�","tranquillement")
    print "Projet cr�e"
    
    ###################################WORKING###################################
    #print fc.s.system.listMethods()
    #print fc.s.getListeProjets()
    #print fc.s.deleteProjet(4)
    #print fc.s.getListeProjets()
    #print fc.s.getProjet(8)
    #print fc.s.getProjet(20)
    #p2 = Projet()
    #print fc.s.sauvegarderProjet(p.serialize())
    print "Nothing to do left!"
    
    #################################NOT WORKING#################################
    #############################################################################
