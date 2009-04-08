class ControleurClient:
    def __init__(self):
        m = Modele()
        i = Interface()
    
    def connecter(self):
        pass
    def ouvrirProjet(self,nom):
        pass
    def afficherInterface(self):
        pass
    def creerProjet(self,nom):
        pass
    def getListeProjets(self):
        pass
    def sauvegarder(self):
        pass
    def creerMandat(self,mandat):
        m.projet.mandat = mandat
    def ouvrirMandat(self):
        return m.projet.mandat
    
    if __name__ == '__main__':
        pass
        