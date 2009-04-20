#-*- coding: iso-8859-1 -*-

# Classe : FakeClient
# Projet : blue-star-project
# Auteur : François Lahey

import xmlrpclib
from xml.parsers.expat import ExpatError

import sys
sys.path.append( "../server" )
from Projet import *

class FakeClient:
    
    def __init__(self):
        self.s = xmlrpclib.ServerProxy('http://localhost:8000/')

    
if __name__ == "__main__":
    
    fc = FakeClient()
    print "Fake client"
    # Creation d'un Projet    
    p=Projet()
    p.nom="Test project"
    p.mandat="Utiliser les caractères spéciaux pour tester la classe ModeleServeur"
    p.addItemAnalyseExplicite("des moules","mangé","juteuses")
    p.addItemAnalyseExplicite("une huitre","grignoté","baveuse")
    p.addItemAnalyseExplicite("une cerise","maché","rouge")
    p.addItemAnalyseExplicite("un bourgeon","sucoté","tranquillement")
    p.addItemAnalyseImplicite("un bourgeon","sucoté","tranquillement")
    print "Projet crée"
    
    ###################################WORKING###################################
    print fc.s.system.listMethods()
    #print fc.s.additionne(2,4)
    print fc.s.additionne(4,5)
    print fc.s.getListeProjets()
    print fc.s.getProjet(2)
    #p2 = Projet()
    print fc.s.sauvegarderProjet(p.serialize())
   
    #################################NOT WORKING#################################
    #############################################################################
