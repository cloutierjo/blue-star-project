#-*- coding: iso-8859-1 -*-

# Classe : ModeleServeur
# Projet : blue-star-project
# Auteur : François Lahey

import sqlite3
import sys
sys.path.append( "../commun" )
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
        cur.execute('''CREATE TABLE AnalysesExp(ID NUMBER(6) REFERENCES Projets, nom VARCHAR2(30), verbe VARCHAR2(30), adjectif VARCHAR2(30), handled NUMBER(1))''')
        cur.execute('''CREATE TABLE AnalysesImp(ID NUMBER(6) REFERENCES Projets, nom VARCHAR2(30), verbe VARCHAR2(30), adjectif VARCHAR2(30), handled NUMBER(1))''')
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
        
        cur.execute('''SELECT * FROM AnalysesExp WHERE ID = (?)''', (projectID,))
        for row in cur:
            p.analyseExplicite.addItem(row[1], row[2], row[3], row[4])
        
        cur.execute('''SELECT * FROM AnalysesImp WHERE ID = (?)''', (projectID,))
        for row in cur:
            p.analyseImplicite.addItem(row[1], row[2], row[3], row[4])
                        
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
        cur.executemany('insert into AnalysesExp values(?, ?, ?, ?, ?)', projet.analyseExplicite.getForDB())
        cur.executemany('insert into AnalysesImp values(?, ?, ?, ?, ?)', projet.analyseImplicite.getForDB())
        
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
        cur.execute('DELETE FROM AnalysesExp WHERE ID = (?)', (projet.num,))
        cur.execute('DELETE FROM AnalysesImp WHERE ID = (?)', (projet.num,))
        cur.executemany('insert into AnalysesExp values(?, ?, ?, ?, ?)', projet.analyseExplicite.getForDB())
        cur.executemany('insert into AnalysesImp values(?, ?, ?, ?, ?)', projet.analyseImplicite.getForDB())
        
        self.con.commit()    
        cur.close()
        return projet.num # To be modified for errors handlin    
     
    def deleteProject(self, projetID):
        
        cur = self.con.cursor()     # Curseur
        
        cur.execute('DELETE FROM Projets WHERE ID = (?)', (projetID,))
        cur.execute('DELETE FROM AnalysesExp WHERE ID = (?)', (projetID,))
        cur.execute('DELETE FROM AnalysesImp WHERE ID = (?)', (projetID,))
        
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
# Ne pas effacer la suite qui sert à initialiser une BD
#############################################################################
    
    # Methode de DEBUGAGE
    def test(self):
        pass
            
# DEBUGAGE
if __name__ == "__main__":
    
    ms = ModeleServeur()        # Creation du ModeleServeur
    ms.initDB()                 # TO BE CALLED FOR FIRST USE ON A SERVER (CREATE TABLES)
    
    # Creation de 10 projets pour fin de tests

    for i in range(10):
        p=Projet()
        p.nom="Projet d'études "+str(i)
        p.mandat="Utiliser les caractères spéciaux pour tester la classe ModeleServeur"
        p.analyseExplicite.addItem("des moules","mangé","juteuses", 0)
        p.analyseExplicite.addItem("une huitre","grignoté","baveuse", 0)
        p.analyseExplicite.addItem("de la dentyne","maché","ice", 0)
        p.analyseExplicite.addItem("avec le feu","jongler","tranquillement", 0)
        p.analyseImplicite.addItem("l'analyse","tester","implicite", 0)
        p.analyseImplicite.addItem("le test","refaire","redondant", 0)
        ms.saveProject(p)
        
    p=ms.getProject(9)
    print p.analyseExplicite.getForDB()
        