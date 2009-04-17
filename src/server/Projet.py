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

    NOMPJ="nompj"
    NUMPJ="numpj"
    MANDAT="mandat"
    analyseIMPLICITE="analyseImplicite"
    analyseEXPLICITE="analyseExplicite"

    def __init__(self):
        '''
        Constructor
        '''
        self.nom = None
        self.num = 0    # Vaut 0 pour nouveau projet et ID du projet lorsque loadé
        self.mandat = None
        self.analyseExplicite = Analyse()
        self.analyseImplicite = Analyse()
        
    def serialize(self):
        self.unicodize()  #néscéssaire pour que les char unicode passe sur le réseau
        return {self.NOMPJ:self.nom,self.NUMPJ:self.num,self.MANDAT:self.mandat,self.analyseEXPLICITE:self.analyseExplicite.analyse,self.analyseIMPLICITE:self.analyseImplicite.analyse}
    
    def deserialize(self, serializedProject):
        self.nom=serializedProject[self.NOMPJ]
        self.num=serializedProject[self.NUMPJ]
        self.mandat=serializedProject[self.MANDAT]
        self.analyseExplicite=Analyse(serializedProject[self.analyseEXPLICITE])
        self.analyseImplicite=Analyse(serializedProject[self.analyseIMPLICITE])
        
    def getAnalyseExpliciteForDB(self):
        print "deprecate getanalyseExpliciteForDB"
        return self.analyseExplicite.getForDB(self.num)
    
    def addItemAnalyseExplicite(self, nom, verbe, adjectif):
        print "deprecate addItemanalyseExplicite"
        self.analyseExplicite.addItem(nom, verbe, adjectif)
        
    def getAnalyseImpliciteForDB(self):
        print "deprecate getanalyseImpliciteForDB"
        return self.analyseImplicite.getForDB(self.num)
    
    def addItemAnalyseImplicite(self, nom, verbe, adjectif):
        print "deprecate addItemanalyseImplicite"
        self.analyseImplicite.addItem(nom, verbe, adjectif)
        
    def unicodize(self):
        if self.nom != None:
            self.nom = unicode(self.nom)
        if self.mandat != None:
            self.mandat = unicode(self.mandat)
        self.analyseExplicite.unicodize()
        self.analyseImplicite.unicodize()
        
class Analyse:
    
    NOM="nom"
    VERBE="verbe"
    ADJECTIF="adjectif"
    
    def __init__(self,otherAnalyse=None):
        if otherAnalyse:
            self.analyse=otherAnalyse
        else:
            self.analyse = []
    
    def getForDB(self,pjID):
        anExpTup=[]
        for item in self.analyse:
            anExpTup.append((pjID,item[self.NOM],item[self.VERBE],item[self.ADJECTIF]))
        return anExpTup
    
    def addItem(self, nom, verbe, adjectif):
        self.analyse.append({self.NOM:nom,self.VERBE:verbe,self.ADJECTIF:adjectif})
        
    def unicodize(self):
        for row in self.analyse:
            row[self.NOM] = unicode(row[self.NOM])
            row[self.VERBE] = unicode(row[self.VERBE])
            row[self.ADJECTIF] = unicode(row[self.ADJECTIF])

if __name__ == '__main__':
    pj=Projet()
    pj.nom="project Name"
    pj.mandat="ceci est un tres tres grand projet comprenant beaucoup d'idée... encore incomplete"
    pj.analyseExplicite.addItem("projet", "faire", "tres long")
    pj.analyseExplicite.addItem("idée","comprant","beaucoup")
    pj.analyseImplicite.addItem("l'analyse", "tester", "implicite")
    pj.unicodize()
    pj.analyseExplicite.getForDB(pj.num)
    pj.unicodize()
    pj.analyseExplicite.getForDB(pj.num)
    pj.analyseImplicite.getForDB(pj.num)
    print pj.serialize()
    pj.deserialize(pj.serialize())
    print pj.serialize()