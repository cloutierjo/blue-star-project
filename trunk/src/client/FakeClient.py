#-*- coding: iso-8859-1 -*-

# Classe : FakeClient
# Projet : blue-star-project
# Auteur : François Lahey

import xmlrpclib
from xml.parsers.expat import ExpatError

import sys
sys.path.append( "../server" )
import Projet

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
    p.addItemAnaliseExplicite("des moules","mangé","juteuses")
    p.addItemAnaliseExplicite("une huitre","grignoté","baveuse")
    p.addItemAnaliseExplicite("une cerise","maché","rouge")
    p.addItemAnaliseExplicite("un bourgeon","sucoté","tranquillement")
    print "Projet crée"
    
    ###################################WORKING###################################
    #print fc.s.additionne(4,5)
    #print fc.s.getListeProjets()
    #print fc.s.getProjet(2)
    ############################################################################# 

    #################################NOT WORKING#################################
    print p.serialize()
    try:
        fc.s.sauvegarderProjet(p.serialize())
    except ExpatError:
        print "A la ligne", ExpatError.lineno
    #############################################################################
        
    #print fc.s.getProjet(11)
