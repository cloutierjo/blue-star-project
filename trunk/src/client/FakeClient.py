#-*- coding: iso-8859-1 -*-

# Classe : FakeClient
# Projet : blue-star-project
# Auteur : Fran�ois Lahey

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
    p.mandat="Utiliser les caract�res sp�ciaux pour tester la classe ModeleServeur"
    p.addItemAnaliseExplicite("des moules","mang�","juteuses")
    p.addItemAnaliseExplicite("une huitre","grignot�","baveuse")
    p.addItemAnaliseExplicite("une cerise","mach�","rouge")
    p.addItemAnaliseExplicite("un bourgeon","sucot�","tranquillement")
    p.addItemAnaliseImplicite("un bourgeon","sucot�","tranquillement")
    print "Projet cr�e"
    
    ###################################WORKING###################################
    #print fc.s.additionne(4,5)
    #print fc.s.getListeProjets()
    #serie = fc.s.getProjet(2)
    #p2 = Projet()
    try:
        p.unicodize()   # Sert a xmlrpc (n�c�ssaire)
        print fc.s.sauvegarderProjet(p.serialize())
    except ExpatError:
        print "A la ligne", ExpatError.lineno
        
    #################################NOT WORKING#################################
    
    #############################################################################
