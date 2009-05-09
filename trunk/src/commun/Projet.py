#-*- coding: iso-8859-1 -*-
'''
Created on 8 avr. 2009

@author: Jonatan Cloutier
'''
import Analyse
import CasUsage
import DictDonne
import Crc
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
    CASETSCENARIO="casEtScenario"
    DICTDONNE="dictDonne"
    CRC="CRC"
    
    def __init__(self):
        '''
        Constructor
        '''
        self.nom = "" # Sinon j'ai plein d'erreur de Allow None en XMLRPC...(Mathieu)
        self.num = 0    # Vaut 0 pour nouveau projet et ID du projet lorsque loadé
        self.mandat = ""# Sinon j'ai plein d'erreur de Allow None en XMLRPC... (Mathieu)
        self.analyseExplicite = Analyse.Analyse(self)
        self.analyseImplicite = Analyse.Analyse(self)
        self.casEtScenario=CasUsage.CasUsage()
        self.dictDonne=DictDonne.DictDonne()
        self.crc=Crc.Crc()
        
    def serialize(self):
        self.unicodize()  #néscéssaire pour que les char unicode passe sur le réseau
        return {self.NOMPJ:self.nom,self.NUMPJ:self.num,self.MANDAT:self.mandat,self.analyseEXPLICITE:self.analyseExplicite.analyse,self.analyseIMPLICITE:self.analyseImplicite.analyse,self.CASETSCENARIO:self.casEtScenario.serialize(),self.DICTDONNE:self.dictDonne.serialize(),self.CRC:self.crc.serialize()}
    
    def deserialize(self, serializedProject):
        self.nom=serializedProject[self.NOMPJ]
        self.num=serializedProject[self.NUMPJ]
        self.mandat=serializedProject[self.MANDAT]
        self.analyseExplicite.analyse=serializedProject[self.analyseEXPLICITE]
        self.analyseImplicite.analyse=serializedProject[self.analyseIMPLICITE]
        self.casEtScenario.deserialize(serializedProject[self.CASETSCENARIO])
        self.dictDonne.deserialize(serializedProject[self.DICTDONNE])
        self.crc.deserialize(serializedProject[self.CRC])
        
    def unicodize(self):
        if self.nom != None:
            self.nom = unicode(self.nom)
        if self.mandat != None:
            self.mandat = unicode(self.mandat)
        self.analyseExplicite.unicodize()
        self.analyseImplicite.unicodize()
        


if __name__ == '__main__':
    pj=Projet()
    pj.nom="project Name"
    pj.mandat="ceci est un tres tres grand projet comprenant beaucoup d'idée... encore incomplete"
    pj.analyseExplicite.addItem("projet", "faire", "tres long")
    pj.analyseExplicite.addItem("idée","comprant","beaucoup")
    pj.analyseImplicite.addItem("l'analyse", "tester", "implicite")
    pj.unicodize()
    pj.analyseExplicite.getForDB()
    pj.unicodize()
    pj.analyseExplicite.getForDB()
    pj.analyseImplicite.getForDB()
    
    cu=pj.casEtScenario
    su=cu.addCasUsage("first cas", 1).scenario
    su.addEtapeScenario("a first step", 1)
    su.addEtapeScenario("a second step")
    
    su=cu.addCasUsage("second cas").scenario
    su.addEtapeScenario("b first step", 1)
    su.addEtapeScenario("b second step")
    
    dd=pj.dictDonne
    dd.variable.append("fisrtVar")
    dd.variable.append("secvar")
    dd.fonction.append("firstFonct")
    dd.fonction.append("secFonct")
    
    crc=pj.crc
    crc.nomClasse="uneClasse"
    crc.proprio="quelqu'un"
    crc.responsabilite.append("fisrtResp")
    crc.responsabilite.append("secResp")
    crc.collaboration.append("firstColl")
    crc.collaboration.append("secColl")
    
    print pj.serialize()
    pj.deserialize(pj.serialize())
    print pj.serialize()