#-*- coding: iso-8859-1 -*-

# Classe : FakeClient
# Projet : blue-star-project
# Auteur : Fran�ois Lahey

import xmlrpclib
from Projet import * 

class FakeClient:
    
    def __init__(self):
        self.s = xmlrpclib.ServerProxy('http://localhost:8000/')

    
if __name__ == "__main__":
    
    fc = FakeClient()
    print "Fake client"
    # Creation d'un Projet    
    p=Projet()
    p.nom="Projet d'�tudes"
    p.mandat="Utiliser les caract�res sp�ciaux pour tester la classe ModeleServeur"
    p.addItemAnaliseExplicite("des moules","mang�","juteuses")
    p.addItemAnaliseExplicite("une huitre","grignot�","baveuse")
    p.addItemAnaliseExplicite("une cerise","mach�","rouge")
    p.addItemAnaliseExplicite("un bourgeon","sucot�","tranquillement")
    print "Projet cr�e"
    
    print fc.s.additionne(4,5)
    print fc.s.getListeProjets()