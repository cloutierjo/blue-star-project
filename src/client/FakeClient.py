#-*- coding: iso-8859-1 -*-

# Classe : FakeClient
# Projet : blue-star-project
# Auteur : François Lahey

import xmlrpclib
from Projet import * 

class FakeClient:
    
    def __init__(self):
        s = xmlrpclib.ServerProxy('http://manage.borealistechnologies.net:8000/')

    
if __name__ == "__main__":
    
    # Creation d'un Projet    
    p=Projet()
    p.nom="Projet d'études"
    p.mandat="Utiliser les caractères spéciaux pour tester la classe ModeleServeur"
    p.addItemAnaliseExplicite("des moules","mangé","juteuses")
    p.addItemAnaliseExplicite("une huitre","grignoté","baveuse")
    p.addItemAnaliseExplicite("une cerise","maché","rouge")
    p.addItemAnaliseExplicite("un bourgeon","sucoté","tranquillement")
    
    print s.sauvegarderProjet(p)