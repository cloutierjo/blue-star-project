#-*- coding: iso-8859-1 -*-
'''
Created on 8 mai 2009

@author: djo
'''

class DictDonne:
    VARIABLE="variable"
    FONCTION="fonction"
    
    def __init__(self):
        self.variable = []
        self.fonction = []
    
    def unicodize(self):
        for row in self.variable:
            row = unicode(row)
        for row in self.fonction:
            row = unicode(row)
            
    def serialize(self):
        self.unicodize()
        return {self.VARIABLE:self.variable,self.FONCTION:self.fonction}
    
    def deserialize(self, serializedScenario):
        self.variable=serializedScenario[self.VARIABLE]
        self.fonction=serializedScenario[self.FONCTION]

if __name__ == '__main__':
    dd=DictDonne()