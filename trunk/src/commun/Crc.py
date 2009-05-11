#-*- coding: iso-8859-1 -*-
'''
Created on 9 mai 2009

@author: Jonatan Cloutier
'''

class LstCrc:
    def __init__(self):
        self.crcs=[]
        
    def unicodize(self):
        for i in self.crcs:
            i.unicodize()
    
    def serialize(self):
        self.unicodize()
        serCrc=[]
        for i in self.crcs:
            serCrc.append(i.serialize())
        return serCrc
    
    def deserialize(self, serializedCrcs):
        self.crcs=[]
        for i in serializedCrcs:
            crc=Crc()
            crc.deserialize(i)
            self.crcs.append(crc)
    
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
    
    def deserialize(self, serializedCrc):
        self.nomClasse=serializedCrc[self.NOMCLASS]
        self.proprio=serializedCrc[self.PROPRIO]
        self.responsabilite=serializedCrc[self.RESPONSABILITE]
        self.collaboration=serializedCrc[self.COLLABORATION]

if __name__ == '__main__':
    crcs=LstCrc()
    
    crc=Crc()
    crc.nomClasse="uneClasse"
    crc.proprio="quelqu'un"
    crc.responsabilite.append("fisrtResp")
    crc.responsabilite.append("secResp")
    crc.collaboration.append("firstColl")
    crc.collaboration.append("secColl")
    
    crcs.crcs.append(crc)
    
    crc=Crc()
    crc.nomClasse="uneAutreClasse"
    crc.proprio="quelqu'un d'autre"
    crc.responsabilite.append("fisrtResp")
    crc.responsabilite.append("secResp")
    crc.collaboration.append("firstColl")
    crc.collaboration.append("secColl")
    
    crcs.crcs.append(crc)
    
    print crcs.serialize()
    crcs.deserialize(crcs.serialize())
    print crcs.serialize()
    