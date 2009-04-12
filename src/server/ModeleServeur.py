#-*- coding: iso-8859-1 -*-

# Classe : ModeleServeur
# Projet : blue-star-project
# Auteur : François Lahey

import sqlite3
from Projet import *

class ModeleServeur:

    # Constructeur
    def __init__(self):    
        self.db = 'test1.db'                    # cheminFichierDB
        self.con = sqlite3.connect(self.db)     # Connecteur
    
    # Initialisation de premier demarrage (Creation BD/Tables)
    def initDB(self):
    
        cur = self.con.cursor()     # Curseur
        
        cur.execute('''CREATE TABLE Projets(ID NUMBER(6) PRIMARY KEY, Nom VARCHAR2(50), Mandat LONG)''')
        cur.execute('''CREATE TABLE Analyses(ID NUMBER(6) REFERENCES Projets, nom VARCHAR2(30), verbe VARCHAR2(30), adjectif VARCHAR2(30))''')
        # En attendant de trouver comment créer une séquence, cette table sert de
        # Générateur d'ID unique dans la méthode getNewID() (bonne pour 999 999 projets 
        cur.execute('''CREATE TABLE Seq(Val NUMBER(6))''')
        cur.execute('insert into Seq values(?)', (1,))
        
        self.con.commit()
        cur.close()
        
    # Lecture d'un projet dans la BD et affectation dans les variables.
    def getProject(self, projectID):
        
        p = Projet()
        cur = self.con.cursor()     # Curseur
        
        cur.execute('''SELECT * FROM Projets WHERE ID = (?)''', (projectID,))
        row = cur.fetchone()
        p.num = row[0]
        p.nom = row[1]
        p.mandat = row[2]
        
        cur.execute('''SELECT * FROM Analyses WHERE ID = (?)''', (projectID,))
        for row in cur:
            p.addItemAnaliseExplicite(row[1], row[2], row[3])
                    
        cur.close()  
        return p 
    
    # Retourne la liste des projets existant dans la BD [ID, Nom][] 
    def getListeProjet(self):
        
        cur = self.con.cursor()     # Curseur
        projets=[]
        
        cur.execute('''SELECT ID, Nom FROM Projets''')
        for projet in cur:
            projets.append([projet[0], projet[1]])
            
        cur.close()
            
        return projets
    
    # Sauvegarde les donnees d'un projet dans la BD, renvoie True si réussi sinon renvoie false
    def saveProject(self, projet):
        
        saved = 0
        projet.unicodize()          # Unicodize le projet pour les accents dans la BD
        
        # Si c'est un nouveau projet... on le cré
        if projet.num == 0:
            saved = self.saveNewProject(projet)
        # Sinon... on update les tables nécéssaire. 
        else:
            saved = self.updateProject(projet)
              
        return saved
    
    def saveNewProject(self, projet):
        
        cur = self.con.cursor()         # Curseur
        projet.num = self.getNewID()    # Get a Unique ID for the project
            
        # Ajout du projet dans la table Projets
        entryTableProjets = (projet.num, projet.nom, projet.mandat) # Nouvelle entrée
        cur.execute('insert into Projets values(?, ?, ?)', entryTableProjets)
        cur.executemany('insert into Analyses values(?, ?, ?, ?)', projet.getAnaliseExpliciteForDB())
        
        self.con.commit()        
        cur.close()
        return projet.num # To be modified for errors handlings
     
    def updateProject(self, projet):
        
        cur = self.con.cursor()     # Curseur
            
        # Update table Projets
        entryTableProjets = (projet.num, projet.nom, projet.mandat) # Nouvelle entrée
        cur.execute('DELETE FROM Projets WHERE ID = (?)', (projet.num,))
        cur.execute('insert into Projets values(?, ?, ?)', entryTableProjets)
        # Update table Analyses 
        cur.execute('DELETE FROM Analyses WHERE ID = (?)', (projet.num,))
        cur.executemany('insert into Analyses values(?, ?, ?, ?)', projet.getAnaliseExpliciteForDB())
        
        self.con.commit()    
        cur.close()
        return projet.num # To be modified for errors handlings
     
    def deleteProject(self, projetID):
        
        cur = self.con.cursor()     # Curseur
        
        cur.execute('DELETE FROM Projets WHERE ID = (?)', (projetID,))
        cur.execute('DELETE FROM Analyses WHERE ID = (?)', (projetID,))
        
        self.con.commit()
        cur.close()
        return True # To be modified for errors handlings
        
    # Sert de séquence de nombre pour l'ID des projet en attendant de trouver comment faire une séquence
    def getNewID(self):
        
        cur = self.con.cursor()    # Curseur
        
        cur.execute('''Select Val from Seq''')
        row = cur.fetchone()
        val = row[0]
        cur.execute('UPDATE Seq SET Val = (?)', (val+1,))
        
        self.con.commit()
        cur.close()
        return val
 
# Fin de ModeleServeur
# Ne pas effacer la suite qui sert a tester la classe
#############################################################################
    
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
    #ms.initDB()                 # TO BE CALLED FOR FIRST USE ON A SERVER (CREATE TABLES)
    
    # Creation d'un Projet    
    p=Projet()
    p.nom="Projet d'études"
    p.mandat="Utiliser les caractères spéciaux pour tester la classe ModeleServeur"
    p.addItemAnaliseExplicite("des moules","mangé","juteuses")
    p.addItemAnaliseExplicite("une huitre","grignoté","baveuse")
    p.addItemAnaliseExplicite("une cerise","maché","rouge")
    p.addItemAnaliseExplicite("un bourgeon","sucoté","tranquillement")
       
    print ms.saveProject(p)         # Test de sauvegarde d'un projet
    ms.test()                       # Check DB integrity
    p.num = 0
    print ms.saveProject(p)         # Test de sauvegarde d'un projet
    ms.test()                       # Check DB integrity
    p.mandat = "Vérifier que la base de données s'est bien updaté."
    print ms.saveProject(p)         # Test de sauvegarde d'un projet
    ms.test()                       # Check DB integrity
    listePJ = ms.getListeProjet()   # Test getListeProjet
    print listePJ
    p2 = ms.getProject(3)           # Test de récupération d'un projet dans la BD
    print p2.num
    print p2.nom
    print p2.mandat
    print p2.getAnaliseExpliciteForDB()
    print "deleting"
    ms.deleteProject(1)             # Test de suppression de projet
    ms.deleteProject(2)             # Test de suppression de projet
    ms.test()                       # Check DB integrity
    print "done"

     