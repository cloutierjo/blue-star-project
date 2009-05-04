#-*- coding: iso-8859-1 -*-
'''
Created on 23 avr. 2009

@author: Jonatan Cloutier
'''
import operator

class ScenarioUtilisation:
    def __init__(self):
        self.etapes = []
        
    def addEtapeScenario(self,nom,ordre=0):
        if ordre==0:
            ordre=len(self.etapes)+1
        self.etapes.append(EtapeScenarioUtilisation(nom,ordre))
        return self.etapes[len(self.etapes)-1]
    
    
    def refaireOrdreNumerique(self):
        temp = []
        for uneEtape in self.etapes:
            temp.append([uneEtape.ordre,uneEtape])
        temp = sorted(temp, key=operator.itemgetter(0))
        
        self.etapes = []
        for tempEtape in temp:
            self.etapes.append(tempEtape[1])
    
    
        for i in range(len(self.etapes)):
            self.etapes[i].ordre = i+1
            
        
    def unicodize(self):
        for e in self.etapes:
            e.unicodize()
    
    def serialize(self):
        self.unicodize()
        serEtapes=[]
        for e in self.etapes:
            serEtapes.append(e.serialize())
        return serEtapes
    
    def deserialize(self, serializedScenario):
        self.etapes=[]
        for i in serializedScenario:
            etape=EtapeScenarioUtilisation()
            etape.deserialize(i)
            self.etapes.append(etape)
    
class EtapeScenarioUtilisation:
    ORDRE="ordre"
    ETAPE="etape"
    
    def __init__(self,nom="",ordre=0):
        self.ordre=ordre
        self.etapes=nom
    
    def unicodize(self):
        self.ordre=unicode(self.ordre)
        self.etapes=unicode(self.etapes)
    
    def serialize(self):
        self.unicodize()
        return {self.ORDRE:self.ordre,self.ETAPE:self.etapes}
    
    def deserialize(self, serializedEtapeScenario):
        self.ordre=serializedEtapeScenario[self.ORDRE]
        self.etapes=serializedEtapeScenario[self.ETAPE]
        
if __name__ == '__main__':
    su=ScenarioUtilisation()
    su.addEtapeScenario("first step", 1)
    su.addEtapeScenario("second step")
    print su.serialize()
    su.deserialize(su.serialize())
    print su.serialize()
    