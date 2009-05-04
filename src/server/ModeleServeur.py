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
        cur.execute('''CREATE TABLE CasUsages(ID NUMBER(6) PRIMARY KEY, IDPROJ NUMBER(6) REFERENCES Projets, cas LONG, priorite NUMBER(6))''')
        cur.execute('''CREATE TABLE Senarios(IDCAS NUMBER(6) REFERENCES Projets, senario LONG, ordreexec NUMBER(6))''')
        # Générateur d'ID unique dans la méthode getNewID() (bonne pour 999 999 projets 
        cur.execute('''CREATE TABLE SeqProj(Val NUMBER(6))''')
        cur.execute('insert into SeqProj values(?)', (1,))
        # Générateur d'ID unique dans la méthode getNewID() (bonne pour 999 999 projets 
        cur.execute('''CREATE TABLE SeqCasUsages(Val NUMBER(6))''')
        cur.execute('insert into SeqCasUsages values(?)', (1,))
        self.con.commit()
        cur.close()
        
    # Lecture d'un projet dans la BD et affectation dans les variables.
    def getProject(self, projectID):
        
        p = Projet()
        cur = self.con.cursor()     # Curseur
        cur2 = self.con.cursor()
        
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
            
        cur.execute('''SELECT * FROM CasUsages WHERE IDPROJ = (?)''', (projectID,))
        for row in cur:
            cas = p.casEtScenario.addCasUsage(row[2], row[3])
            cur2.execute('''SELECT * FROM Senarios WHERE IDCAS = (?)''', (row[0],))
            for row in cur2:
                cas.scenario.addEtapeScenario(row[1], row[2])
            
                        
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
        cur = self.con.cursor()             # Curseur
        cur2 = self.con.cursor()
        projet.num = self.getNewIDProj()    # Get a Unique ID for the project
            
        # Ajout du projet dans la table Projets
        entryTableProjets = (projet.num, projet.nom, projet.mandat) # Nouvelle entrée
        cur.execute('insert into Projets values(?, ?, ?)', entryTableProjets)
        cur.executemany('insert into AnalysesExp values(?, ?, ?, ?, ?)', projet.analyseExplicite.getForDB())
        cur.executemany('insert into AnalysesImp values(?, ?, ?, ?, ?)', projet.analyseImplicite.getForDB())
        
        projet.casEtScenario.unicodize()
        for cas in projet.casEtScenario.items:
            idCasUsage = self.getNewIDCasUsages()
            cur.execute('insert into CasUsages values(?, ?, ?, ?)', (idCasUsage, projet.num, cas.nom, cas.priorite))
            for scen in cas.scenario.etapes:
                cur2.execute('insert into Senarios values(?, ?, ?)', (idCasUsage, scen.etapes, scen.ordre,))
        
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
        # Update table CasUsages et Senarios
        
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
    def getNewIDProj(self):
        
        cur = self.con.cursor()    # Curseur
        
        cur.execute('''Select Val from SeqProj''')
        row = cur.fetchone()
        val = row[0]
        cur.execute('UPDATE SeqProj SET Val = (?)', (val+1,))
        
        self.con.commit()
        cur.close()
        return val

    # Sert de séquence de nombre pour l'ID des projet en attendant de trouver comment faire une séquence
    def getNewIDCasUsages(self):
        
        cur = self.con.cursor()    # Curseur
        
        cur.execute('''Select Val from SeqCasUsages''')
        row = cur.fetchone()
        val = row[0]
        cur.execute('UPDATE SeqCasUsages SET Val = (?)', (val+1,))
        
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
        
        p.casEtScenario.addCasUsage("Je suis un cas éé")
        p.casEtScenario.addCasUsage("Je suis un autre cas éé")
        
        for cas in p.casEtScenario.items:
            cas.scenario.addEtapeScenario("Je suis une étape tape tape")
            cas.scenario.addEtapeScenario("Je suis une autre étape")
            
        ms.saveProject(p)
        
    for cas in p.casEtScenario.items:
        print "Je suis le cas : "+cas.nom+" "+str(cas.priorite)
        for scenario in cas.scenario.etapes:
            print scenario.etapes+" "+str(scenario.ordre)

    p2=ms.getProject(9)
    
    print p2.analyseExplicite.getForDB()
    for cas in p2.casEtScenario.items:
        print "Je suis le cas : "+cas.nom+" "+str(cas.priorite)
        for scenario in cas.scenario.etapes:
            print scenario.etapes+" "+str(scenario.ordre)
        
    print "Création DB DONE !!!"
        