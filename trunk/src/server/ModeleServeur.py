#-*- coding: iso-8859-1 -*-

# Classe : ModeleServeur
# Projet : blue-star-project
# Auteur : François Lahey

import sqlite3
from Projet import *

class ModeleServeur:

    # Constructeur
    def __init__(self):
        
        self.projetTemp = None                  # Tampon pour un projet
        self.db = ':memory:'                    # cheminFichierDB
        self.con = sqlite3.connect(self.db)     # Connecteur
    
    # Initialisation de premier demarrage (Creation BD/Tables)
    def initDB(self):
    
        cur = self.con.cursor()     # Curseur
        
        cur.execute('''create table Projets(nom VARCHAR2(30), mandat text)''')
        cur.execute('''create table Analyses(projet text, nom text, verbe text, adjectif text)''')
    
        cur.close()
        
    # Lecture d'un projet dans la BD et affectation dans les variables.
    def getProjet(self, nomProjet):
        
        # To be implemented...
        
        return self.projet 
    
    # Retourne la liste des projets existant dans la BD
    def getListeProjet(self):
        
        pass
    
    # Sauvegarde les donnees d'un projet dans la BD
    def sauvegardeProjet(self, projet):
        
        cur = self.con.cursor()     # Curseur
        entryTableProjets = (unicode(projet.nom), unicode(projet.mandat))
        cur.execute('insert into Projets values(?, ?)', entryTableProjets)
        for row in projet.getAnaliseExpliciteTuple():
            # Ajout du nom du projet pour la sauvegarde dans la BD
            toSave = (unicode(projet.nom), unicode(row[0]), unicode(row[1]), unicode(row[2]))
            cur.execute('insert into Analyses values(?, ?, ?, ?)', toSave)
            
        cur.close()
    
    # Methode de DEBUGAGE
    def test(self):
        
        cur = self.con.cursor()    # Curseur
        
        # Affichage dela table test
        print "Table Projets :"
        cur.execute('''Select * from Projets''')
        for row in cur:
            ligne1 = row[0]
            ligne2 = row[1]
            print ligne1+" : "+ligne2
            
        print ""
        print "Table Analyses : "
        cur.execute('''Select * from Analyses''')
        for row in cur:
            champ1 = row[0]
            champ2 = row[1]
            champ3 = row[2]
            champ4 = row[3]
            ligne = champ1+", "+champ2+", "+champ3+", "+champ4
            print ligne
            
        cur.close()
            
# DEBUGAGE
if __name__ == "__main__":
    
    ms = ModeleServeur()        # Creation du ModeleServeur
    ms.initDB()                 # To be changed (RAM DEBUG)
    
    # Creation d'un Projet    
    p=Projet()                  
    p.nom="Projet d'études"
    p.mandat="Utiliser les caractères spéciaux pour tester la classe ModeleServeur"
    p.addItemAnaliseExplicite("des moules","mangé","juteuses")
    p.addItemAnaliseExplicite("une huitre","grignoté","baveuse")
    p.addItemAnaliseExplicite("une cerise","maché","rouge")
    p.addItemAnaliseExplicite("roger","sucoté","inconsciemment")
       
    ms.sauvegardeProjet(p)      # Test de sauvegarde d'un projet
    ms.test()                   # Check DB integrity
     