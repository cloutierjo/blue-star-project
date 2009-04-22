#-*- coding: iso-8859-1 -*-

# Classe : ServerMethods
# Projet : blue-star-project
# Auteur : Jonathan Hall�e

from ModeleServeur import *

ms = ModeleServeur()# instance du modele c�t� serveur

class ServerMethods:
    #m�thode qui retourne la liste des projets sous forme d'un liste  
    def getListeProjets(self):
        return ms.getListeProjet()
        
    #m�thode qui sauvegarde un projet
    def sauvegarderProjet(self, serializedProjet):
        
        p = Projet()
        p.deserialize(serializedProjet) #on retourne le projet d�s�rializ� a francois pour le save
                                        #dans la db
        return ms.saveProject(p)
    
    #m�thode qui retourne un projet via son ID
    def getProjet(self, idProjet):
        return ms.getProject(idProjet).serialize()#on prend un projet serializ� pour le passer sur le web ou en local
                                                  #on peut pas passer une instance de clase sur le web
    
    #m�thode qui retourne un boolean d�pendamment si le projet a bien �t� supprim�
    def deleteProjet(self, idProjet):
        return ms.deleteProject(idProjet)