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
        
        self.projet = None                      # Tampon pour un projet
        self.db = ':memory:'                    # Chemin du fichier de DB
        
        # Initialisation sqlite3
        self.con = sqlite3.connect(self.db)     # Connecteur
    
    # Initialisation de premier demarrage (Creation BD/Tables)
    def initDB(self):
        
        pass 
    
    # Lecture d'un projet dans la BD et affectation dans les variables.
    def getProjet(self, nomProjet):
        
        # To be implemented...
        
        return self.projet 
    
    # Retourne la liste des projets existant dans la BD
    def getListeProjet(self):
        
        pass
    
    # Sauvegarde les donnees d'un projet dans la BD
    def sauvegardeProjet(self, projet):
        
        pass
    
    # Transforme une liste de dictionnaire en liste de tuples
    def dictListToTuplesList(self, dict):
        
        pass
    
    # Methode de DEBUGAGE
    def test(self):
        
        cur = self.con.cursor()    # Curseur
        
        tuple = ('Projet 2', 'Macher sqlite3', 'complement sujet conjonction')  # Tuple
        
        cur.execute('''create table tabletest(nom text, mandat text, at text)''')
        cur.execute('''insert into tabletest values('Projet 1', 'Tester sqlite3', 'nom verbe adjectif')''')
        cur.execute('insert into tabletest values(?, ?, ?)', tuple)             # Test d'insertion d'un tuple
        cur.execute('''Select * from tabletest''')
        for row in cur:
            print row
        cur.execute('''Select * from tabletest where nom = 'Projet 2' ''')
        for row in cur:
            print row
        cur.close()
            
# DEBUGAGE
if __name__ == "__main__":
    
    ms = ModeleServeur()
    # ms.test()
    prj = DummyProjet()
    print "Nom : "+prj.nom
    print "Mandat : "+prj.mandat
    print "Analyse : "
    for row in prj.analyse:
        print row