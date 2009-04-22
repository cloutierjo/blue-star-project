#-*- coding: iso-8859-1 -*-

# Classe : ServerMethods
# Projet : blue-star-project
# Auteur : Jonathan Hallée

from ModeleServeur import *

ms = ModeleServeur()# instance du modele côté serveur

class ServerMethods:
    #méthode qui retourne la liste des projets sous forme d'un liste  
    def getListeProjets(self):
        return ms.getListeProjet()
        
    #méthode qui sauvegarde un projet
    def sauvegarderProjet(self, serializedProjet):
        
        p = Projet()
        p.deserialize(serializedProjet) #on retourne le projet désérializé a francois pour le save
                                        #dans la db
        return ms.saveProject(p)
    
    #méthode qui retourne un projet via son ID
    def getProjet(self, idProjet):
        return ms.getProject(idProjet).serialize()#on prend un projet serializé pour le passer sur le web ou en local
                                                  #on peut pas passer une instance de clase sur le web
    
    #méthode qui retourne un boolean dépendamment si le projet a bien été supprimé
    def deleteProjet(self, idProjet):
        return ms.deleteProject(idProjet)