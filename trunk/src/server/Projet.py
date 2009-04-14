#-*- coding: iso-8859-1 -*-
'''
Created on 8 avr. 2009

@author: Jonatan Cloutier
'''

class Projet(object):
    '''
    contient tout les informations d'un projet ainsi que des méthode 
    utilitaire pour en simplifier l'accès
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.NOMPJ="nompj"
        self.NUMPJ="numpj"
        self.NOMANALISE="nom"
        self.VERBEANALISE="verbe"
        self.ADJECTIFANALISE="adjectif"
        self.MANDAT="mandat"
      #  self.ANALISEIMPLICITE="analyseImplicite"
        self.ANALISEEXPLICITE="analyseExplicite"
        self.nom = None
        self.num = 0    # Vaut 0 pour nouveau projet et ID du projet lorsque loadé
        self.mandat = None
        self.analyseExplicite = []
        
    def serialize(self):
        return {self.NOMPJ:self.nom,self.NUMPJ:self.num,self.MANDAT:self.mandat,self.ANALISEEXPLICITE:self.analyseExplicite}
    
    def deserialize(self, serializedProject):
        self.nom=serializedProject[self.NOMPJ]
        self.num=serializedProject[self.NUMPJ]
        self.mandat=serializedProject[self.MANDAT]
        self.analyseExplicite=serializedProject[self.ANALISEEXPLICITE]
        
    def getAnaliseExpliciteForDB(self):
        anExpTup=[]
        for item in self.analyseExplicite:
            anExpTup.append((self.num,item[self.NOMANALISE],item[self.VERBEANALISE],item[self.ADJECTIFANALISE]))
        return anExpTup
    
    def addItemAnaliseExplicite(self, nom, verbe, adjectif):
        self.analyseExplicite.append({self.NOMANALISE:nom,self.VERBEANALISE:verbe,self.ADJECTIFANALISE:adjectif})
        
    def unicodize(self):
        if self.nom != None:
            self.nom = unicode(self.nom)
        if self.mandat != None:
            self.mandat = unicode(self.mandat)
        if len(self.analyseExplicite) > 0:
            for row in self.analyseExplicite:
                row[self.NOMANALISE] = unicode(row[self.NOMANALISE])
                row[self.VERBEANALISE] = unicode(row[self.VERBEANALISE])
                row[self.ADJECTIFANALISE] = unicode(row[self.ADJECTIFANALISE])
                
if __name__ == '__main__':
    pj=Projet()
    pj.nom="project Name"
    pj.mandat="ceci est un tres tres grand projet comprenant beaucoup d'idée... encore incomplete"
    pj.addItemAnaliseExplicite("projet", "faire", "tres long")
    pj.addItemAnaliseExplicite("idée","comprant","beaucoup")
    # pj.unicodize()
    pj.getAnaliseExpliciteTuple()
    print pj.serialize()
    pj.deserialize(pj.serialize())
    print pj.serialize()