# Classe : ModeleServeur
# Projet : blue-star-project
# Auteur : Francois Lahey


import sqlite3

class ModeleServeur:

    # Constructeur
    def __init__(self):
        
        self.projet = None                      # Tampon pour un projet
        
        # Initialisation sqlite3
        self.con = sqlite3.connect(':memory:')  # Connecteur
    
    # Initialisation de premier demarrage (Creation BD/Tables)
    def initServeur(self):
        
        pass 
    
    # Lecture d'un projet dans la BD et affectation dans les variables.
    def getProjet(self, nomProjet):
        
        # To be implemented...
        
        return self.projet 
    
    # Retourne la liste des projets existant dans la BD
    def getListeProjet(self):
        
        pass
    
    # Sauvegarde les donnees d'un projet dans la BD
    def sauvegardeProjet(self):
        
        pass
    
    # Methode de debugage
    def test(self):
        
        cur = self.con.cursor()    # Curseur
        
        liste = ('Projet 2', 'Macher sqlite3', 'complement sujet conjonction')  # Test d'insertion de variables
        
        cur.execute('''create table tabletest(nom text, mandat text, at text)''')
        cur.execute('''insert into tabletest values('Projet 1', 'Tester sqlite3', 'nom verbe adjectif')''')
        cur.execute('insert into tabletest values(?, ?, ?)', liste)
        cur.execute('''Select * from tabletest''')
        
        for row in cur:
            print row
            
        cur.close()
            
# DEBUGAGE

if __name__ == "__main__":
    
    ms = ModeleServeur()
    ms.test()