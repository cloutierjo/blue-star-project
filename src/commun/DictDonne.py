#-*- coding: iso-8859-1 -*-
'''
Created on 8 mai 2009

@author: Jonatan Cloutier
'''

class DictDonne:
    VARIABLE="variable"
    FONCTION="fonction"
    
    def __init__(self):
        self.variable = []
        self.fonction = []
        
    def updateDictionnaire(self,variables,fonctions):
        self.variable = []
        self.fonction = []
        self.variable=variables
        self.fonction=fonctions
    
    def unicodize(self):
        for row in self.variable:
            row[0] = unicode(row[0])
        for row in self.fonction:
            row[0] = unicode(row[0])
            
    def serialize(self):
        self.unicodize()
        return {self.VARIABLE:self.variable,self.FONCTION:self.fonction}
    
    def deserialize(self, serializedDict):
        self.variable=serializedDict[self.VARIABLE]
        self.fonction=serializedDict[self.FONCTION]
        
    
if __name__ == '__main__':
    dd=DictDonne()
    dd.variable.append(["fisrtVar", 0])
    dd.variable.append(["secvar", 1])
    dd.fonction.append(["firstFonct", 0])
    dd.fonction.append(["secFonct", 1])
    
    print dd.serialize()
    dd.deserialize(dd.serialize())
    print dd.serialize()
    