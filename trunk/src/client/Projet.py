#-*- coding: iso-8859-1 -*-
'''
Created on 8 avr. 2009

@author: Jonatan Cloutier
'''

class Projet(object):
    '''
    contient tout les informations d'un projet ainsi que des m�thode 
    utilitaire pour en simplifier l'acc�s
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.NOMPJ="nompj"
        self.NOM="nom"
        self.VERBE="verbe"
        self.ADJECTIF="adjectif"
        self.MANDAT="mandat"
      #  self.ANALISEIMPLICITE="analyseImplicite"
        self.ANALISEEXPLICITE="analyseExplicite"
        self.nom = None
        self.mandat = None
        self.analyseExplicite = []
        
    def serialize(self):
        return {self.NOMPJ:self.nom,self.MANDAT:self.mandat,self.ANALISEEXPLICITE:self.analyseExplicite}
    
    def deserialize(self, serializedProject):
        self.nom=serializedProject[self.NOMPJ]
        self.mandat=serializedProject[self.MANDAT]
        self.analyseExplicite=serializedProject[self.ANALISEEXPLICITE]
        
    def getAnaliseExpliciteTuple(self):
        anExpTup=[]
        for item in self.analyseExplicite:
            anExpTup.append((item[self.NOM],item[self.VERBE],item[self.ADJECTIF]))
        return anExpTup
    
    def addItemAnaliseExplicite(self, nom, verbe, adjectif):
        self.analyseExplicite.append({self.NOM:nom,self.VERBE:verbe,self.ADJECTIF:adjectif})
        
        
if __name__ == '__main__':
    pj=Projet()
    pj.nom="project Name"
    pj.mandat="ceci est un tres tres grand projet comprenant beaucoup d'id�e... encore incomplete"
    pj.addItemAnaliseExplicite("projet", "faire", "tres long")
    pj.addItemAnaliseExplicite("id�e","comprant","beaucoup")
    pj.getAnaliseExpliciteTuple()
    print pj.serialize()
    pj.deserialize(pj.serialize())
    print pj.serialize()
    
    
    