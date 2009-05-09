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
    
    def deserialize(self, serializedDict):
        self.variable=serializedDict[self.VARIABLE]
        self.fonction=serializedDict[self.FONCTION]

if __name__ == '__main__':
    dd=DictDonne()
    dd.variable.append("fisrtVar")
    dd.variable.append("secvar")
    dd.fonction.append("firstFonct")
    dd.fonction.append("secFonct")
    
    print dd.serialize()
    dd.deserialize(dd.serialize())
    print dd.serialize()
    