class ScenarioUtilisation:
    def __init__(self):
        self.etapes = []
        
    def ajouterEtape(self,lesEtapes):
        self.etapes = [] # vider la liste
        for i in range(len(lesEtapes)): # ajouter toutes les etape sous forme     1, etape1       2,Etape2 ....
            self.etapes.append([i+1,lesEtapes[i]])
        