#-*- coding: iso-8859-1 -*-

# Classe : ModeleServeur
# Projet : blue-star-project
# Auteur : Fran�ois Lahey

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
        # En attendant de trouver comment cr�er une s�quence, cette table sert de
        # G�n�rateur d'ID unique dans la m�thode getNewID (bonne pour 999 999 projets 
        cur.execute('''CREATE TABLE Seq(Val NUMBER(6))''')
        cur.execute('insert into Seq values(?)', (1,))
        
        cur.close()
        
    # Lecture d'un projet dans la BD et affectation dans les variables.
    def getProject(self, projectID):
        
        p = Projet()
        cur = self.con.cursor()     # Curseur
        
        cur.execute('''SELECT * FROM Projets WHERE ID = (?)''', (projectID,))
        for row in cur:
            p.num = row[0]
            p.nom = row[1]
            p.mandat = row[2]
        
        cur.execute('''SELECT * FROM Analyses WHERE ID = (?)''', (projectID,))
        for row in cur:
            p.addItemAnaliseExplicite(row[1], row[2], row[3])
                    
        cur.close()  
        return p 
    
    # Retourne la liste des projets existant dans la BD {ID, Nom}[] 
    def getListeProjet(self):
        
        cur = self.con.cursor()     # Curseur
        projets=[]
        
        cur.execute('''SELECT ID, Nom FROM Projets''')
        
        for projet in cur:
            projets.append([projet[0], projet[1]])
            
        cur.close()
            
        return projets
    
    # Sauvegarde les donnees d'un projet dans la BD, renvoie True si r�ussi sinon renvoie false
    def saveProject(self, projet):
        
        saved = False
        projet.unicodize()          # Unicodize le projet
        
        # Si c'est un nouveau projet... on le cr�
        if projet.num == 0:
            self.saveNewProject(projet)
            saved = True
        # Sinon... on update les tables n�c�ssaire. 
        else:
            self.updateProject(projet)
            saved = True
            
        return saved
    
    def saveNewProject(self, projet):
        
        cur = self.con.cursor()     # Curseur
            
        projet.num = self.getNewID()
            
        # Ajout du projet dans la table Projets
        entryTableProjets = (projet.num, projet.nom, projet.mandat) # Nouvelle entr�e
        cur.execute('insert into Projets values(?, ?, ?)', entryTableProjets)
            
        # Update table Analyses 
        for row in projet.getAnaliseExpliciteTuple():
            # Ajout du nom du projet pour la sauvegarde dans la BD
            toSave = (projet.num, row[0], row[1], row[2])
            cur.execute('insert into Analyses values(?, ?, ?, ?)', toSave)
                
        cur.close()
     
    def updateProject(self, projet):
        
        cur = self.con.cursor()     # Curseur
            
        # Update table Projets
        entryTableProjets = (projet.num, projet.nom, projet.mandat) # Nouvelle entr�e
        cur.execute('DELETE FROM Projets WHERE ID = (?)', (projet.num,))
        cur.execute('insert into Projets values(?, ?, ?)', entryTableProjets)
            
        # Update table Analyses 
        cur.execute('DELETE FROM Analyses WHERE ID = (?)', (projet.num,))
        for row in projet.getAnaliseExpliciteTuple():
            # Ajout du nom du projet pour la sauvegarde dans la BD
            toSave = (projet.num, row[0], row[1], row[2])
            cur.execute('insert into Analyses values(?, ?, ?, ?)', toSave)
                
        cur.close()
     
    def deleteProject(self, projet):
        
        cur = self.con.cursor()     # Curseur
        cur.execute('DELETE FROM Projets WHERE ID = (?)', (projet.num,))
        cur.execute('DELETE FROM Analyses WHERE ID = (?)', (projet.num,))
        
        return True
        
    # Sert de s�quence de nombre pour l'ID des projet en attendant de trouver comment faire une s�quence
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
    p.nom="Projet d'�tudes"
    p.mandat="Utiliser les caract�res sp�ciaux pour tester la classe ModeleServeur"
    p.addItemAnaliseExplicite("des moules","mang�","juteuses")
    p.addItemAnaliseExplicite("une huitre","grignot�","baveuse")
    p.addItemAnaliseExplicite("une cerise","mach�","rouge")
    p.addItemAnaliseExplicite("roger","sucot�","inconsciemment")
       
    print ms.saveProject(p)         # Test de sauvegarde d'un projet
    ms.test()                       # Check DB integrity
    p.num = 0
    print ms.saveProject(p)         # Test de sauvegarde d'un projet
    ms.test()                       # Check DB integrity
    p.mandat = "V�rifier que la base de donn�es s'est bien updat�."
    print ms.saveProject(p)         # Test de sauvegarde d'un projet
    ms.test()                       # Check DB integrity
    listePJ = ms.getListeProjet()   # Test getListeProjet
    print listePJ
    p2 = ms.getProject(2)           # Test de r�cup�ration d'un projet dans la BD
    print p2.num
    print p2.nom
    print p2.getAnaliseExpliciteTuple()
    ms.deleteProject(p)            # Test de suppression de projet
    ms.test()                      # Check DB integrity
     