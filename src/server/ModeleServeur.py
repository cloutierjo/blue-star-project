#-*- coding: iso-8859-1 -*-

# Classe : ModeleServeur
# Projet : blue-star-project
# Auteur : Fran�ois Lahey

import sqlite3
import sys
sys.path.append( "../commun" )
from Projet import *
# import os
# os.environ['PATH'] ="C:/Python26/instantclient_11_1" + os.pathsep + os.environ['PATH']
# import cx_Oracle

# cx_Oracle.connect([user, password, dsn, mode, handle, pool, threaded, twophase, events, cclass, purity, newpassword])

class ModeleServeur:

    # Constructeur
    def __init__(self):    
        self.db = 'test1.db'                    # cheminFichierDB
        self.con = sqlite3.connect(self.db)     # Connecteur
        #self.con = cx_Oracle.Connection("user/pass@serveur/instance")
        
    
    # Initialisation de premier demarrage (Creation BD/Tables)
    def initDB(self):
    
        cur = self.con.cursor()     # Curseur
        
        cur.execute('''CREATE TABLE Projets(ID NUMBER(6) PRIMARY KEY, Nom VARCHAR2(50), Mandat LONG)''')
        cur.execute('''CREATE TABLE AnalysesExp(ID NUMBER(6) REFERENCES Projets, nom VARCHAR2(30), verbe VARCHAR2(30), adjectif VARCHAR2(30), handled NUMBER(1))''')
        cur.execute('''CREATE TABLE AnalysesImp(ID NUMBER(6) REFERENCES Projets, nom VARCHAR2(30), verbe VARCHAR2(30), adjectif VARCHAR2(30), handled NUMBER(1))''')
        cur.execute('''CREATE TABLE CasUsages(IDCAS NUMBER(6) PRIMARY KEY, IDPROJ NUMBER(6) REFERENCES Projets, cas LONG, priorite NUMBER(6))''')
        cur.execute('''CREATE TABLE Senarios(IDCAS NUMBER(6) REFERENCES CasUsages, senario LONG, ordreexec NUMBER(6))''')
        cur.execute('''CREATE TABLE Variables(IDPROJ NUMBER(6) REFERENCES Projets, Var VARCHAR2(30), handled NUMBER(1))''')
        cur.execute('''CREATE TABLE Fonctions(IDPROJ NUMBER(6) REFERENCES Projets, Fon VARCHAR2(30), handled NUMBER(1))''')
        cur.execute('''CREATE TABLE Usagers(IDUSER NUMBER(9) PRIMARY KEY, IDPROJ NUMBER(6) REFERENCES Projets, Nom VARCHAR2(30))''')
        cur.execute('''CREATE TABLE CRC(IDPROJ NUMBER(6) REFERENCES Projets, IDCRC NUMBER(6) PRIMARY KEY, Nom VARCHAR2(50), Usager varchar2(30), Handle NUMBER(1))''')
        cur.execute('''CREATE TABLE Responsabilite(IDCRC NUMBER(6) REFERENCES CRC, Nom VARCHAR(50), Handle NUMBER(1))''')
        cur.execute('''CREATE TABLE Collaboration(IDCRC NUMBER(6) REFERENCES CRC, Nom VARCHAR(50))''')
        cur.execute('''CREATE TABLE Sprint(IDPROJ NUMBER(6) REFERENCES Projets, IDSPRINT NUMBER(6) PRIMARY KEY, DateFin DATE)''')
        cur.execute('''CREATE TABLE TaskGen(IDSPRINT NUMBER(6) REFERENCES Sprint, Nom VARCHAR(30), Handled NUMBER(1))''')
        cur.execute('''CREATE TABLE TaskFull(IDSPRINT NUMBER(6) REFERENCES Sprint, Nom VARCHAR(30), User VARCHAR(30), Priorite NUMBER(6), Handled NUMBER(1))''')
        cur.execute('''CREATE TABLE Scrums(IDPROJ NUMBER(6) REFERENCES Projets , IDSCRUM NUMBER(6) PRIMARY KEY , Date DATE , Usager varchar2(30))''')
        cur.execute('''CREATE TABLE ScrumDone(IDSCRUM NUMBER(6) REFERENCES Scrums , Detail VARCHAR2(50) , Handled NUMBER(1))''')
        cur.execute('''CREATE TABLE ScrumToDo(IDSCRUM NUMBER(6) REFERENCES Scrums , Detail VARCHAR2(50) , Handled NUMBER(1))''')
        cur.execute('''CREATE TABLE ScrumBug(IDSCRUM NUMBER(6) REFERENCES Scrums , Detail VARCHAR2(50) , Handled NUMBER(1))''')
        
        # G�n�rateur d'ID unique dans la m�thode getNewID() (bonne pour 999 999 projets 
        cur.execute('''CREATE TABLE SeqProj(Val NUMBER(6))''')
        cur.execute('insert into SeqProj values(?)', (1,))
        # G�n�rateur d'ID unique pour CasUsages 
        cur.execute('''CREATE TABLE SeqCasUsages(Val NUMBER(6))''')
        cur.execute('insert into SeqCasUsages values(?)', (1,))
        # G�n�rateur d'ID unique pour Usagers 
        cur.execute('''CREATE TABLE SeqUsagers(Val NUMBER(9))''')
        cur.execute('insert into SeqUsagers values(?)', (1,))
        # G�n�rateur d'ID unique pour CRC 
        cur.execute('''CREATE TABLE SeqCRC(Val NUMBER(9))''')
        cur.execute('insert into SeqCRC values(?)', (1,))
        # G�n�rateur d'ID unique pour Sprint 
        cur.execute('''CREATE TABLE SeqSprint(Val NUMBER(9))''')
        cur.execute('insert into SeqSprint values(?)', (1,))
        # G�n�rateur d'ID unique pour Scrum 
        cur.execute('''CREATE TABLE SeqScrum(Val NUMBER(9))''')
        cur.execute('insert into SeqScrum values(?)', (1,))
        
        self.con.commit()
        cur.close()
        
    # Lecture d'un projet dans la BD et affectation dans les variables.
    def getProject(self, projectID):
        
        p = Projet()
        
        cur = self.con.cursor()     # Curseur
        cur2 = self.con.cursor()    # Curseur 2 pour boucles
        
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
            for row2 in cur2:
                cas.scenario.addEtapeScenario(row2[1], row2[2])
               
        cur.execute('''SELECT * FROM Variables WHERE IDPROJ = (?)''', (projectID,))
        for row in cur:
            p.dictDonne.variable.append([row[1], row[2]])
            
        cur.execute('''SELECT * FROM Fonctions WHERE IDPROJ = (?)''', (projectID,))
        for row in cur:
            p.dictDonne.fonction.append([row[1], row[2]])
            
        cur.execute('''SELECT Nom FROM Usagers WHERE IDPROJ = (?)''', (projectID,))
        for row in cur:
            p.user.user.append(row[0])

        cur.execute('''SELECT * FROM CRC WHERE IDPROJ = (?)''', (projectID,))
        for row in cur:
            crc=Crc.Crc()
            crc.nomClasse=row[2]
            crc.proprio=row[3]
            crc.handled=row[4]
        
            cur2.execute('''SELECT * FROM Responsabilite WHERE IDCRC = (?)''', (row[1],))
            for row2 in cur2:
                crc.responsabilite.append([row2[1], row2[2]])
                
            cur2.execute('''SELECT * FROM Collaboration WHERE IDCRC = (?)''', (row[1],))
            for row2 in cur2:
                crc.collaboration.append(row2[1])
            p.crc.crcs.append(crc)
          
        # Loading Sprints
        cur.execute('''SELECT * FROM Sprint WHERE IDPROJ = (?)''', (projectID,))
        for row in cur:
            sprint=Sprint.Sprint()
            sprint.dateFin = row[2]
            
            cur2.execute('''SELECT * FROM TaskGen WHERE IDSPRINT = (?)''', (row[1],))
            for row2 in cur2:
                sprint.taskGeneral.append([row2[1], row2[2]])
                
            cur2.execute('''SELECT * FROM TaskFull WHERE IDSPRINT = (?)''', (row[1],))
            for row2 in cur2:
                task=TaskList.Task()
                task.name = row2[1]
                task.user = row2[2]
                task.priorite = row2[3]
                task.handled = row2[4]
                
                sprint.taskFull.tasklist.append(task)
                
            p.sprint.sprints.append(sprint)
            
        # Loading Scrums
        scl=Scrum.ScrumList()
        cur.execute('''SELECT * FROM Scrums WHERE IDPROJ = (?)''', (projectID,))
        for row in cur:    
            sc = Scrum.Scrum()
            sc.date = row[2]
            sc.user = row[3]
            
            cur2.execute('''SELECT * FROM ScrumDone WHERE IDSCRUM = (?)''', (row[1],))
            for row2 in cur2:
                sc.done.append([row2[1], row2[2]])
                
            cur2.execute('''SELECT * FROM ScrumToDo WHERE IDSCRUM = (?)''', (row[1],))
            for row2 in cur2:
                sc.todo.append([row2[1], row2[2]])
                
            cur2.execute('''SELECT * FROM ScrumBug WHERE IDSCRUM = (?)''', (row[1],))
            for row2 in cur2:
                sc.probleme.append([row2[1], row2[2]])
    
            scl.scrums.append(sc)
        
        p.scrum=scl
        
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
    
    # Nouvelle m�thode g�rant la sauvegarde de nouveaux projet ou l'update d'un projet existant 
    def saveProject(self, projet):

        cur = self.con.cursor()             # Curseur
        cur2 = self.con.cursor()
        
        if projet.num == 0:
            projet.num = self.getNewIDProj()    # Get a Unique ID for the project
        else:
            self.deleteProject(projet.num)
            
        # Ajout du projet dans la table Projets
        entryTableProjets = (projet.num, projet.nom, projet.mandat) # Nouvelle entr�e
        cur.execute('insert into Projets values(?, ?, ?)', entryTableProjets)
        cur.executemany('insert into AnalysesExp values(?, ?, ?, ?, ?)', projet.analyseExplicite.getForDB())
        cur.executemany('insert into AnalysesImp values(?, ?, ?, ?, ?)', projet.analyseImplicite.getForDB())
        
        projet.casEtScenario.unicodize()
        for cas in projet.casEtScenario.items:
            idCasUsage = self.getNewIDCasUsages()
            cur.execute('insert into CasUsages values(?, ?, ?, ?)', (idCasUsage, projet.num, cas.nom, cas.priorite))
            for scen in cas.scenario.etapes:
                cur2.execute('insert into Senarios values(?, ?, ?)', (idCasUsage, scen.etapes, scen.ordre,))
        
        for var in projet.dictDonne.variable:
            cur.execute('insert into Variables values(?, ?, ?)', (projet.num, var[0], var[1]))
            
        for fon in projet.dictDonne.fonction:
            cur.execute('insert into Fonctions values(?, ?, ?)', (projet.num, fon[0], fon[1]))
            
        for usager in projet.user.user:
            idUsager = self.getNewIDUsager()
            cur.execute('insert into Usagers values(?, ?, ?)', (idUsager, projet.num, usager))
        
        for eachcrc in projet.crc.crcs:
            idcrc = self.getNewIDCRC()
            cur.execute('insert into CRC values(?, ?, ?, ?, ?)', (projet.num, idcrc, eachcrc.nomClasse, eachcrc.proprio, eachcrc.handled))
            for eachResp in eachcrc.responsabilite:
                cur2.execute('insert into Responsabilite values(?, ?, ?)', (idcrc, eachResp[0], eachResp[1]))
            for eachCol in eachcrc.collaboration:
                cur2.execute('insert into Collaboration values(?, ?)', (idcrc, eachCol))
        
        # SAVE SPRINT    
        for eachsprint in projet.sprint.sprints:
            idSprint = self.getNewIDSprint()
            cur.execute('insert into Sprint values(?, ?, ?)', (projet.num, idSprint, eachsprint.dateFin))
            for eachtaskgen in eachsprint.taskGeneral:
                cur2.execute('insert into TaskGen values(?, ?, ?)', (idSprint, eachtaskgen[0], eachtaskgen[1]))
            for eachtaskfull in eachsprint.taskFull.tasklist:
                cur2.execute('insert into TaskFull values(?, ?, ?, ?, ?)',(idSprint, eachtaskfull.name, eachtaskfull.user, eachtaskfull.priorite, eachtaskfull.handled))
        
        # SAVE SCRUMS
        
        for eachscrum in projet.scrum.scrums:
            idScrum = self.getNewIDScrum()
            cur.execute('insert into Scrums values(?, ?, ?, ?)',(projet.num, idScrum, eachscrum.date, eachscrum.user))
            for eachDone in eachscrum.done:
                cur2.execute('insert into ScrumDone values(?, ?, ?)',(idScrum, eachDone[0], eachDone[1]))
            for eachToDo in eachscrum.todo:
                cur2.execute('insert into ScrumToDo values(?, ?, ?)',(idScrum, eachToDo[0], eachToDo[1]))
            for eachProblem in eachscrum.probleme:
                cur2.execute('insert into ScrumBug values(?, ?, ?)',(idScrum, eachProblem[0], eachProblem[1]))
                       
        self.con.commit()        
        cur.close()
        return projet.num # To be modified for errors handlings      
     
    def deleteProject(self, projetID):
        
        cur = self.con.cursor()     # Curseur
        cur2 = self.con.cursor()
        
        cur.execute('DELETE FROM Projets WHERE ID = (?)', (projetID,))
        cur.execute('DELETE FROM AnalysesExp WHERE ID = (?)', (projetID,))
        cur.execute('DELETE FROM AnalysesImp WHERE ID = (?)', (projetID,))
        
        # Deleting CasUsages
        cur.execute('''SELECT IDCAS FROM CasUsages WHERE IDPROJ = (?)''', (projetID,))
        for row in cur:
            cur2.execute('DELETE FROM Senarios WHERE IDCAS = (?)', (row[0],))
        cur.execute('DELETE FROM CasUsages WHERE IDPROJ = (?)', (projetID,))   
        
        # Deleting Dictionnaire de donn�es
        cur.execute('DELETE FROM Variables WHERE IDPROJ = (?)', (projetID,))
        cur.execute('DELETE FROM Fonctions WHERE IDPROJ = (?)', (projetID,))
        
        # Deleting Usagers
        cur.execute('DELETE FROM Usagers WHERE IDPROJ = (?)', (projetID,))
        
        # Deleting CRCs
        cur.execute('''SELECT IDCRC FROM CRC WHERE IDPROJ = (?)''', (projetID,))
        for row in cur:
            cur2.execute('DELETE FROM Responsabilite WHERE IDCRC = (?)', (row[0],))
            
        cur.execute('''SELECT IDCRC FROM CRC WHERE IDPROJ = (?)''', (projetID,))
        for row in cur:
            cur2.execute('DELETE FROM Collaboration WHERE IDCRC = (?)', (row[0],))
            
        cur.execute('DELETE FROM CRC WHERE IDPROJ = (?)', (projetID,))
            
        # Deleting Sprints
        cur.execute('''SELECT IDSPRINT FROM Sprint WHERE IDPROJ = (?)''', (projetID,))
        for row in cur:
            cur2.execute('DELETE FROM TaskGen WHERE IDSPRINT = (?)', (row[0],))
            
        cur.execute('''SELECT IDSPRINT FROM Sprint WHERE IDPROJ = (?)''', (projetID,))
        for row in cur:
            cur2.execute('DELETE FROM TaskFull WHERE IDSPRINT = (?)', (row[0],))
            
        cur.execute('DELETE FROM Sprint WHERE IDPROJ = (?)', (projetID,))
        
        # Deleting Scrums
        cur.execute('''SELECT IDSCRUM FROM Scrums WHERE IDPROJ =(?)''',(projetID,))
        for row in cur:
            cur2.execute('DELETE FROM ScrumDone WHERE IDSCRUM = (?)', (row[0],))
          
        cur.execute('''SELECT IDSCRUM FROM Scrums WHERE IDPROJ =(?)''',(projetID,))
        for row in cur:
            cur2.execute('DELETE FROM ScrumToDo WHERE IDSCRUM = (?)', (row[0],))
            
        cur.execute('''SELECT IDSCRUM FROM Scrums WHERE IDPROJ =(?)''',(projetID,))
        for row in cur:
            cur2.execute('DELETE FROM ScrumBug WHERE IDSCRUM = (?)', (row[0],))
            
        cur.execute('DELETE FROM Scrums WHERE IDPROJ = (?)', (projetID,))
            
        self.con.commit()
        cur.close()
        cur2.close()
        return True # To be modified for errors handlings
        
    # Sert de s�quence de nombre pour l'ID des projet en attendant de trouver comment faire une s�quence
    def getNewIDProj(self):
        
        cur = self.con.cursor()    # Curseur
        
        cur.execute('''Select Val from SeqProj''')
        row = cur.fetchone()
        val = row[0]
        cur.execute('UPDATE SeqProj SET Val = (?)', (val+1,))
        
        self.con.commit()
        cur.close()
        return val

    # Sert de s�quence de nombre pour l'ID des projet en attendant de trouver comment faire une s�quence
    def getNewIDCasUsages(self):
        
        cur = self.con.cursor()    # Curseur
        
        cur.execute('''Select Val from SeqCasUsages''')
        row = cur.fetchone()
        val = row[0]
        cur.execute('UPDATE SeqCasUsages SET Val = (?)', (val+1,))
        
        self.con.commit()
        cur.close()
        return val
    
    # Sert de s�quence de nombre pour l'ID des Usagers en attendant de trouver comment faire une s�quence
    def getNewIDUsager(self):
        
        cur = self.con.cursor()    # Curseur
        
        cur.execute('''Select Val from SeqUsagers''')
        row = cur.fetchone()
        val = row[0]
        cur.execute('UPDATE SeqUsagers SET Val = (?)', (val+1,))
        
        self.con.commit()
        cur.close()
        return val
    
    # Sert de s�quence de nombre pour l'ID des CRC en attendant de trouver comment faire une s�quence
    def getNewIDCRC(self):
        
        cur = self.con.cursor()    # Curseur
        
        cur.execute('''Select Val from SeqCRC''')
        row = cur.fetchone()
        val = row[0]
        cur.execute('UPDATE SeqCRC SET Val = (?)', (val+1,))
        
        self.con.commit()
        cur.close()
        return val
    
    # Sert de s�quence de nombre pour l'ID des Sprints en attendant de trouver comment faire une s�quence
    def getNewIDSprint(self):
        
        cur = self.con.cursor()    # Curseur
        
        cur.execute('''Select Val from SeqSprint''')
        row = cur.fetchone()
        val = row[0]
        cur.execute('UPDATE SeqSprint SET Val = (?)', (val+1,))
        
        self.con.commit()
        cur.close()
        return val
 
   # Sert de s�quence de nombre pour l'ID des Sprints en attendant de trouver comment faire une s�quence
    def getNewIDScrum(self):
        
        cur = self.con.cursor()    # Curseur
        
        cur.execute('''Select Val from SeqScrum''')
        row = cur.fetchone()
        val = row[0]
        cur.execute('UPDATE SeqScrum SET Val = (?)', (val+1,))
        
        self.con.commit()
        cur.close()
        return val
    
# Fin de ModeleServeur
# Ne pas effacer la suite qui sert � initialiser une BD
#############################################################################
    
    # Methode de DEBUGAGE
    def test(self):
        pass
            
# DEBUGAGE
if __name__ == "__main__":
    
    print "Cr�ation de la base de donn�es en cours...."
    ms = ModeleServeur()        # Creation du ModeleServeur
    ms.initDB()                 # TO BE CALLED FOR FIRST USE ON A SERVER (CREATE TABLES)
    print "Cr�ation DATABASE DONE !!!"
    
'''
    # Creation de 10 projets pour fin de tests

    for i in range(5):
        p=Projet()
        p.nom="Projet d'�tudes "+str(i)
        p.mandat="Utiliser les caract�res sp�ciaux pour tester la classe ModeleServeur"
        p.analyseExplicite.addItem("des moules","mang�","juteuses", 0)
        p.analyseExplicite.addItem("une huitre","grignot�","baveuse", 0)
        p.analyseExplicite.addItem("de la dentyne","mach�","ice", 0)
        p.analyseExplicite.addItem("avec le feu","jongler","tranquillement", 0)
        p.analyseImplicite.addItem("l'analyse","tester","implicite", 0)
        p.analyseImplicite.addItem("le test","refaire","redondant", 0)
        
        p.casEtScenario.addCasUsage("Je suis un cas ��")
        p.casEtScenario.addCasUsage("Je suis un autre cas ��")
        
        for cas in p.casEtScenario.items:
            cas.scenario.addEtapeScenario("Je suis une �tape tape tape")
            cas.scenario.addEtapeScenario("Je suis une autre �tape")
           
        p.dictDonne.variable.append(["fisrtVar", 0])
        p.dictDonne.variable.append(["fisrtVar", 1])
        p.dictDonne.fonction.append(["fisrtVar", 0])
        p.dictDonne.fonction.append(["fisrtVar", 1])
        
        p.user.user.append("Frank")
        p.user.user.append("Math")
        p.user.user.append("Jo")
        p.user.user.append("Kovy")
        p.user.user.append("Pascal")
        p.user.user.append("Chan")
        
        crc=Crc.Crc()
        crc.nomClasse="dummyClasse"
        crc.proprio="dummyquelqu'un"
        crc.responsabilite.append(["dummyfisrtResp", 0])
        crc.responsabilite.append(["dummysecResp", 1])
        crc.collaboration.append("dummyfirstColl")
        crc.collaboration.append("dummysecColl")   
        p.crc.crcs.append(crc)
        
        sprint=Sprint.Sprint()
        sprint.dateFin = "1979-05-25"
        sprint.taskGeneral.append(["dummyfisrttaskGen", 0])
        sprint.taskGeneral.append(["dummysectaskGen", 1])
        
        task=TaskList.Task()
        task.name="task1b"
        task.priorite=1
        task.user = "moib"
        sprint.taskFull.tasklist.append(task)
    
        task=TaskList.Task()
        task.name="task2b"
        task.priorite=2
        task.user = "301b"
        sprint.taskFull.tasklist.append(task)
        
        p.sprint.sprints.append(sprint)
        
        scl=Scrum.ScrumList()
    
        sc=Scrum.Scrum()
    
        sc.date="1990-06-20"
        sc.user="Frank"
        sc.done.append(["fais1",0])
        sc.done.append(["fais2",0])
        sc.todo.append(["afaire1",0])
        sc.todo.append(["afaire2",0])
        sc.probleme.append(["prob1",0])
        sc.probleme.append(["prob2",0])
    
        scl.scrums.append(sc)
    
        sc=Scrum.Scrum()
    
        sc.date="1995-03-05"
        sc.user="Frank"
        sc.done.append(["fais1",0])
        sc.done.append(["fais2",0])
        sc.todo.append(["afaire1",0])
        sc.todo.append(["afaire2",0])
        sc.probleme.append(["prob1",0])
        sc.probleme.append(["prob2",0])
    
        scl.scrums.append(sc)
    
        p.scrum=scl
    
        ms.saveProject(p)
    
    # Test de get projet...
    px=ms.getProject(3)
    px.scrum.scrums[0].done.append(["donetest", 0])
    for eachscrum in px.scrum.scrums:
        print eachscrum.date
        print eachscrum.user
        for eachtodo in eachscrum.done:
            print eachtodo[0]
        for eachtodo in eachscrum.todo:
            print eachtodo[0] 
        for eachtodo in eachscrum.probleme:
            print eachtodo[0]
    
    
    number = ms.saveProject(px)
    print "projet : "+str(number)
    p2=ms.getProject(number)
    print "projet : "+str(p2.num)
    
    print p2.analyseExplicite.getForDB()
    for cas in p2.casEtScenario.items:
        print "Je suis le cas : "+cas.nom+" "+str(cas.priorite)
        for scenario in cas.scenario.etapes:
            print scenario.etapes+" "+str(scenario.ordre)
            
    for var in p2.dictDonne.variable:
        print var[0]+" "+str(var[1])
        
    for fon in p2.dictDonne.fonction:
        print fon[0]+" "+str(fon[1])
        
    for usager in p2.user.user:
        print usager
        
    for eachcrc in p2.crc.crcs:
        print eachcrc.nomClasse
        print eachcrc.proprio
        for eachResp in eachcrc.responsabilite:
            print eachResp[0]+" "+str(eachResp[1])
        for eachCol in eachcrc.collaboration:
            print eachCol
    
    for eachsprint in p2.sprint.sprints:
        print eachsprint.dateFin
        for eachtaskgen in eachsprint.taskGeneral:
            print eachtaskgen[0]+" "+str(eachtaskgen[1])
        for eachtaskfull in eachsprint.taskFull.tasklist:
            print eachtaskfull.name
            print eachtaskfull.user
            print str(eachtaskfull.priorite)
            print str(eachtaskfull.handled) 
    
    for eachscrum in p2.scrum.scrums:
        print eachscrum.date
        print eachscrum.user
        for eachtodo in eachscrum.done:
            print eachtodo[0]
        for eachtodo in eachscrum.todo:
            print eachtodo[0] 
        for eachtodo in eachscrum.probleme:
            print eachtodo[0]
               
'''
        