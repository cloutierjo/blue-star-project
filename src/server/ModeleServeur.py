# Classe : ModeleServeur
# Projet : blue-star-project
# Auteur : Francois Lahey


import sqlite3

# Classe de DEBUGAGE
class DummyProjet:
    
    # Constructeur
    def __init__(self):
        
        self.nom = "DummyProject"
        self.mandat = "Utiliser la classe DummyProjet pour tester la classe ModeleServeur"
        self.analyse = [{"nom":"des moules","verbe":"manger", "adjectif":"juteuses"},
                        {"nom":"une huitre" ,"verbe":"grignoter" ,"adjectif":"baveuse"},
                        {"nom":"une cerise" ,"verbe":"macher" ,"adjectif":"rouge" },
                        {"nom":"roger" ,"verbe":"sucoter" ,"adjectif":"inconsciemment"}]
        
    def getAnaliseExplicite(self):
        
        return [("des moules","manger","juteuses"),
                ("une huitre","grignoter","baveuse"),
                ("une cerise","macher","rouge"),
                ("roger","sucoter","inconsciemment")]

class ModeleServeur:

    # Constructeur
    def __init__(self):
        
        self.projetTemp = None                  # Tampon pour un projet
        self.db = ':memory:'                    # cheminFichierDB
        self.con = sqlite3.connect(self.db)     # Connecteur
    
    # Initialisation de premier demarrage (Creation BD/Tables)
    def initDB(self):
    
        cur = self.con.cursor()     # Curseur
        
        cur.execute('''create table Projets(nom text, mandat text)''')
        cur.execute('''create table Analyses(nom text, verbe text, adjectif text)''')
    
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
        
        entryTableProjets = (projet.nom, projet.mandat)
        cur.execute('insert into Projets values(?, ?)', entryTableProjets)
        for row in projet.getAnaliseExplicite():
            cur.execute('insert into Analyses values(?, ?, ?)', row)
            
        cur.close()
    
    # Methode de DEBUGAGE
    def test(self):
        
        cur = self.con.cursor()    # Curseur
        
        # Affichage des 2 tables tests
        
        print "Table Projets :"
        cur.execute('''Select * from Projets''')
        for row in cur:
            print row
            
        print ""
        print "Table Analyses : "
        cur.execute('''Select * from Analyses''')
        for row in cur:
            print row
            
        cur.close()
            
# DEBUGAGE
if __name__ == "__main__":
    
    ms = ModeleServeur()        # Creation du ModeleServeur
    ms.initDB()                 # To be changed (RAM DEBUG)
    dp = DummyProjet()          # Creation d'un Projet
    ms.sauvegardeProjet(dp)     # Test de sauvegarde d'un projet
    ms.test()                   # Check DB integrity
     