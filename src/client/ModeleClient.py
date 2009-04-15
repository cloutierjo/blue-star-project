#-*- coding: iso-8859-1 -*-
'''
Created on 14 avr. 2009

@author: djo
'''
import Projet

class ModeleClient(object):
    '''
    la base du model coté client
    '''


    def __init__(self):
        '''
        créé le modele
        '''
        self.projet=None
        
    def creerProjet(self,nom):
        self.projet=Projet.Projet()
        self.projet.nom=nom
        
if __name__ == '__main__':
    mod=ModeleClient()
    mod.creerProjet("testName")
    print mod.projet.serialize()
        