#-*- coding: iso-8859-1 -*-

# Classe : ModeleServeur
# Projet : blue-star-project
# Auteur : François Lahey

import sqlite3
from Projet import *

class ModeleServeur:

    # Constructeur
    def __init__(self):
        
        self.db = ':memory:'                    # cheminFichierDB
        self.con = sqlite3.connect(self.db)     # Connecteur
    
    # Initialisation de premier demarrage (Creation BD/Tables)
    def initDB(self):
    
        cur = self.con.cursor()     # Curseur
        
        cur.execute('''CREATE TABLE Projets(ID NUMBER(6) PRIMARY KEY, Nom VARCHAR2(50), Mandat LONG)''')
        cur.execute('''CREATE TABLE Analyses(ID NUMBER(6) REFERENCES Projets, nom VARCHAR2(30), verbe VARCHAR2(30), adjectif VARCHAR2(30))''')
        # En attendant de trouver comment créer une séquence, cette table sert de sauvegarde pour une séquence pour les ID
        cur.execute('''CREATE TABLE Seq(Val NUMBER(6))''')
        cur.execute('insert into Seq values(?)', (1,))
        
        cur.close()
        
    # Lecture d'un projet dans la BD et affectation dans les variables.
    def getProjet(self, nomProjet):
        
        # To be implemented...
        
        return self.projet 
    
    # Retourne la liste des projets existant dans la BD
    def getListeProjet(self):
        
        pass
    
    # Sauvegarde les donnees d'un projet dans la BD, renvoie True si réussi sinon renvoie false
    def saveProject(self, projet):
        
        saved = False
        projet.unicodize()          # Unicodize le projet
        
        # Si c'est un nouveau projet... on le cré
        if projet.num == 0:
            
            cur = self.con.cursor()     # Curseur
            
            projet.num = self.getNewID()
            
            # Ajout du projet dans la table Projets
            entryTableProjets = (projet.num, projet.nom, projet.mandat) # Nouvelle entrée
            cur.execute('insert into Projets values(?, ?, ?)', entryTableProjets)
            
            # Update table Analyses 
            for row in projet.getAnaliseExpliciteTuple():
                # Ajout du nom du projet pour la sauvegarde dans la BD
                toSave = (projet.num, row[0], row[1], row[2])
                cur.execute('insert into Analyses values(?, ?, ?, ?)', toSave)
                
            cur.close()
            saved = True
            
        # Sinon... on update les tables nécéssaire. 
        else:
            
            cur = self.con.cursor()     # Curseur
            
            # Update table Projets
            #entryTableProjets = (projet.num, projet.nom, projet.mandat) # Nouvelle entrée
            #cur.execute('insert into Projets values(?, ?, ?)', entryTableProjets)
            
            # Update table Analyses 
            cur.execute('DELETE FROM Analyses WHERE ID = (?)', (projet.num,))
            for row in projet.getAnaliseExpliciteTuple():
                # Ajout du nom du projet pour la sauvegarde dans la BD
                toSave = (projet.num, row[0], row[1], row[2])
                cur.execute('insert into Analyses values(?, ?, ?, ?)', toSave)
                
            cur.close()
            saved = True
            
        return saved
        
    # Sert de séquence de nombre pour l'ID des projet en attendant de trouver comment faire une séquence
    def getNewID(self):
        
        cur = self.con.cursor()    # Curseur
        
        cur.execute('''Select Val from Seq''')
        for row in cur:
            val = row[0]
        cur.execute('UPDATE Seq SET Val = (?)', (val+1,))
    
        cur.close()
        return val
    
    # Methode de DEBUGAGE
    def test(self):
        
        cur = self.con.cursor()    # Curseur
        
        # Affichage dela table test
        print "Table Projets :"
        cur.execute('''Select * from Projets''')
        for row in cur:
            id = row[0]
            nom = row[1]
            mandat = row[2]
            print str(id)+" : "+nom+" : "+mandat
            
        print ""
        print "Table Analyses : "
        cur.execute('''Select * from Analyses''')
        for row in cur:
            id = row[0]
            champ2 = row[1]
            champ3 = row[2]
            champ4 = row[3]
            ligne = str(id)+", "+champ2+", "+champ3+", "+champ4
            print ligne
            
        cur.close()
            
# DEBUGAGE
if __name__ == "__main__":
    
    ms = ModeleServeur()        # Creation du ModeleServeur
    ms.initDB()                 # TO BE CALLED FOR FIRST USE ON A SERVER (CREATE TABLES)
    
    # Creation d'un Projet    
    p=Projet()                  
    p.nom="Projet d'études"
    p.mandat="Utiliser les caractères spéciaux pour tester la classe ModeleServeur"
    p.addItemAnaliseExplicite("des moules","mangé","juteuses")
    p.addItemAnaliseExplicite("une huitre","grignoté","baveuse")
    p.addItemAnaliseExplicite("une cerise","maché","rouge")
    p.addItemAnaliseExplicite("roger","sucoté","inconsciemment")
       
    print ms.saveProject(p)    # Test de sauvegarde d'un projet
    ms.test()                       # Check DB integrity
    p.num = 0
    print ms.saveProject(p)    # Test de sauvegarde d'un projet
    ms.test()                       # Check DB integrity
     