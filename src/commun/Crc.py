#-*- coding: iso-8859-1 -*-
'''
Created on 9 mai 2009

@author: Jonatan Cloutier
'''

class Crc:
    NOMCLASS="nomClasse"
    PROPRIO="proprio"
    RESPONSABILITE="responsabilite"
    COLLABORATION="collaboration"
    
    def __init__(self):
        self.nomClasse = ""
        self.proprio = ""
        self.responsabilite = []
        self.collaboration = []
    
    def unicodize(self):
        self.nomClasse=unicode(self.nomClasse)
        self.proprio=unicode(self.proprio)
        for row in self.responsabilite:
            row = unicode(row)
        for row in self.collaboration:
            row = unicode(row)
            
    def serialize(self):
        self.unicodize()
        return {self.NOMCLASS:self.nomClasse,self.PROPRIO:self.proprio,self.RESPONSABILITE:self.responsabilite,self.COLLABORATION:self.collaboration}
    
    def deserialize(self, serializedDict):
        self.nomClasse=serializedDict[self.NOMCLASS]
        self.proprio=serializedDict[self.PROPRIO]
        self.responsabilite=serializedDict[self.RESPONSABILITE]
        self.collaboration=serializedDict[self.COLLABORATION]

if __name__ == '__main__':
    crc=Crc()
    crc.nomClasse="uneClasse"
    crc.proprio="quelqu'un"
    crc.responsabilite.append("fisrtResp")
    crc.responsabilite.append("secResp")
    crc.collaboration.append("firstColl")
    crc.collaboration.append("secColl")
    
    print crc.serialize()
    crc.deserialize(crc.serialize())
    print crc.serialize()
    