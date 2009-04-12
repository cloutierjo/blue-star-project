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
        self.NOM="nom"
        self.VERBE="verbe"
        self.ADJECTIF="adjectif"
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
            anExpTup.append((self.num,item[self.NOM],item[self.VERBE],item[self.ADJECTIF]))
        return anExpTup
    
    def addItemAnaliseExplicite(self, nom, verbe, adjectif):
        self.analyseExplicite.append({self.NOM:nom,self.VERBE:verbe,self.ADJECTIF:adjectif})
        
    def unicodize(self):
        if self.nom != None:
            self.nom = unicode(self.nom)
        if self.mandat != None:
            self.mandat = unicode(self.mandat)
        if len(self.analyseExplicite) > 0:
            for row in self.analyseExplicite:
                row[self.NOM] = unicode(row[self.NOM])
                row[self.VERBE] = unicode(row[self.VERBE])
                row[self.ADJECTIF] = unicode(row[self.ADJECTIF])
                
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
    