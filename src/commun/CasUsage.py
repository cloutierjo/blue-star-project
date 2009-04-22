from ScenarioUtilisation import *

class CasUsage:
    def __init__(self,nom):
        self.nom = nom
        self.scenario = []
        
    def ajouterScenario(self,ScenarioUtilisation):
        self.scenario.append(ScenarioUtilisation)
        return len(self.scenario)-1 # retourne l'index de l'ajout
        