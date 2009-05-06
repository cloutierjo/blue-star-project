#-*- coding: iso-8859-1 -*-
'''
Created on 23 avr. 2009

@author: Jonatan Cloutier
'''

import ScenarioUtilisation

class CasUsage:
    def __init__(self):
        self.items=[]
        
    def addCasUsage(self,nom,priorite=0):
        if priorite==0:
            priorite=len(self.items)+1
        self.items.append(CasUsageItem(nom,int(priorite)))
        return self.items[len(self.items)-1]
        
    def unicodize(self):
        for i in self.items:
            i.unicodize()
    
    def serialize(self):
        self.unicodize()
        serItem=[]
        for i in self.items:
            serItem.append(i.serialize())
        return serItem
    
    def deserialize(self, serializedCasUsage):
        self.items=[]
        for i in serializedCasUsage:
            item=CasUsageItem()
            item.deserialize(i)
            self.items.append(item)
    
class CasUsageItem:
    NOM="nom"
    PRIORITE="priorite"
    SCENARIO="scenario"
    
    def __init__(self,nom="",priorite=0):
        self.nom = nom
        self.priorite=priorite
        self.scenario = ScenarioUtilisation.ScenarioUtilisation()
        
    def unicodize(self):
        self.nom = unicode(self.nom)
        self.priorite = unicode(self.priorite)
        self.scenario.unicodize()
        
    def serialize(self):
        self.unicodize()
        return {self.NOM:self.nom,self.PRIORITE:self.priorite,self.SCENARIO:self.scenario.serialize()}
    
    def deserialize(self, serializedCasUsageItem):
        self.nom=serializedCasUsageItem[self.NOM]
        self.priorite=int(serializedCasUsageItem[self.PRIORITE]) #La priorité est une string apres le deserialize sinon
        self.scenario=ScenarioUtilisation.ScenarioUtilisation()
        self.scenario.deserialize(serializedCasUsageItem[self.SCENARIO])
    
    
if __name__ == '__main__':
    cu=CasUsage()
    su=cu.addCasUsage("first cas", 1).scenario
    su.addEtapeScenario("a first step", 1)
    su.addEtapeScenario("a second step")
    
    su=cu.addCasUsage("second cas").scenario
    su.addEtapeScenario("b first step", 1)
    su.addEtapeScenario("b second step")
    
    print cu.serialize()
    cu.deserialize(cu.serialize())
    print cu.serialize()
    