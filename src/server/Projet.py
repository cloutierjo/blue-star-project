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
    
    class CST:
        '''
        Constant utiliser dans projet
        '''
        NOMPJ="nompj"
        NUMPJ="numpj"
        NOMANALISE="nom"
        VERBEANALISE="verbe"
        ADJECTIFANALISE="adjectif"
        MANDAT="mandat"
        ANALISEIMPLICITE="analyseImplicite"
        ANALISEEXPLICITE="analyseExplicite"

    def __init__(self):
        '''
        Constructor
        '''
        self.nom = None
        self.num = 0    # Vaut 0 pour nouveau projet et ID du projet lorsque loadé
        self.mandat = None
        self.analyseExplicite = []
        self.analyseImplicite = []
        
    def serialize(self):
        self.unicodize()  #néscéssaire pour que les char unicode passe sur le réseau
        return {self.CST.NOMPJ:self.nom,self.CST.NUMPJ:self.num,self.CST.MANDAT:self.mandat,self.CST.ANALISEEXPLICITE:self.analyseExplicite,self.CST.ANALISEIMPLICITE:self.analyseImplicite}
    
    def deserialize(self, serializedProject):
        self.nom=serializedProject[self.CST.NOMPJ]
        self.num=serializedProject[self.CST.NUMPJ]
        self.mandat=serializedProject[self.CST.MANDAT]
        self.analyseExplicite=serializedProject[self.CST.ANALISEEXPLICITE]
        self.analyseImplicite=serializedProject[self.CST.ANALISEIMPLICITE]
        
    def getAnaliseExpliciteForDB(self):
        anExpTup=[]
        for item in self.analyseExplicite:
            anExpTup.append((self.num,item[self.CST.NOMANALISE],item[self.CST.VERBEANALISE],item[self.CST.ADJECTIFANALISE]))
        return anExpTup
    
    def addItemAnaliseExplicite(self, nom, verbe, adjectif):
        self.analyseExplicite.append({self.CST.NOMANALISE:nom,self.CST.VERBEANALISE:verbe,self.CST.ADJECTIFANALISE:adjectif})
        
    def getAnaliseImpliciteForDB(self):
        anExpTup=[]
        for item in self.analyseImplicite:
            anExpTup.append((self.num,item[self.CST.NOMANALISE],item[self.CST.VERBEANALISE],item[self.CST.ADJECTIFANALISE]))
        return anExpTup
    
    def addItemAnaliseImplicite(self, nom, verbe, adjectif):
        self.analyseImplicite.append({self.CST.NOMANALISE:nom,self.CST.VERBEANALISE:verbe,self.CST.ADJECTIFANALISE:adjectif})
        
    def unicodize(self):
        if self.nom != None:
            self.nom = unicode(self.nom)
        if self.mandat != None:
            self.mandat = unicode(self.mandat)
        if len(self.analyseExplicite) > 0:
            for row in self.analyseExplicite:
                row[self.CST.NOMANALISE] = unicode(row[self.CST.NOMANALISE])
                row[self.CST.VERBEANALISE] = unicode(row[self.CST.VERBEANALISE])
                row[self.CST.ADJECTIFANALISE] = unicode(row[self.CST.ADJECTIFANALISE])
        if len(self.analyseImplicite) > 0:
            for row in self.analyseImplicite:
                row[self.CST.NOMANALISE] = unicode(row[self.CST.NOMANALISE])
                row[self.CST.VERBEANALISE] = unicode(row[self.CST.VERBEANALISE])
                row[self.CST.ADJECTIFANALISE] = unicode(row[self.CST.ADJECTIFANALISE])
                
if __name__ == '__main__':
    pj=Projet()
    pj.nom="project Name"
    pj.mandat="ceci est un tres tres grand projet comprenant beaucoup d'idée... encore incomplete"
    pj.addItemAnaliseExplicite("projet", "faire", "tres long")
    pj.addItemAnaliseExplicite("idée","comprant","beaucoup")
    pj.addItemAnaliseImplicite("l'analyse", "tester", "implicite")
    pj.unicodize()
    pj.getAnaliseExpliciteForDB()
    pj.unicodize()
    pj.getAnaliseExpliciteForDB()
    pj.getAnaliseImpliciteForDB()
    print pj.serialize()
    pj.deserialize(pj.serialize())
    print pj.serialize()