#-*- coding: iso-8859-1 -*-
'''
Created on 9 mai 2009

@author: Jonatan Cloutier
'''

class LstCrc:
    def __init__(self):
        self.crcs=[]
        
### à voir avec Jonatan C   ####################    
    def addCrc(self,nom):
        if self.getClass(nom)==None:
            crc=Crc()
            crc.nomClasse=nom
            self.crcs.append(crc)
            return 0
        else:
            return 1
        
    def updateCrc(self,crc):
        for i in self.crcs:
            if(i.nomClasse==crc.nomClasse):
                self.crcs.remove(i)
        self.crcs.append(crc)
################################################
        
    def getClassName(self):
        name=[]
        for i in self.crcs:
            name.append(i.nomClasse)
        return name
    
    def getClass(self,className):
        for i in self.crcs:
            if(i.nomClasse==className):
                return i
        return None                
        
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
        self.responsabilite = []    # Liste de liste [String, Handled]
        self.collaboration = []     
        self.handled = 0
        
    def unicodize(self):
        self.nomClasse=unicode(self.nomClasse)
        self.proprio=unicode(self.proprio)
        for row in self.responsabilite:
            row[0] = unicode(row[0])
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
    crc.responsabilite.append(["fisrtResp", 0])
    crc.responsabilite.append(["secResp", 1])
    crc.collaboration.append("firstColl")
    crc.collaboration.append("secColl")
    
    crcs.crcs.append(crc)
    
    crc=Crc()
    crc.nomClasse="uneAutreClasse"
    crc.proprio="quelqu'un d'autre"
    crc.responsabilite.append(["fisrtResp", 0])
    crc.responsabilite.append(["secResp", 1])
    crc.collaboration.append("firstColl")
    crc.collaboration.append("secColl")
    
    crcs.crcs.append(crc)
    
    print crcs.serialize()
    crcs.deserialize(crcs.serialize())
    print crcs.serialize()
    
    print crcs.getClassName()
    print crcs.getClass("uneAutreClasse").serialize()
    
    crc=crcs.getClass("uneAutreClasse")
    crc.proprio="un nouveau"
    
    print crcs.getClass("uneAutreClasse").serialize()
    