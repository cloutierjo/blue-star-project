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
        
    def getVarDict(self):
        varRet=[]
        for elem in self.variable:
            varRet.append({"name":elem[0],"handled":elem[1]})
        return varRet
        
    def getFonctDict(self):
        fonctRet=[]
        for elem in self.fonction:
            varRet.append({"name":elem[0],"handled":elem[1]})
        return fonctRet
    
    def setVarDict(self,varDict):
        self.variable=[]
        for elem in self.variable:
            self.variable.append([varDict["name"],varDict["handled"]])
    
    def setFonctDict(self,fonctDict):
        self.fonction=[]
        for elem in self.fonction:
            self.variable.append([fonctDict["name"],fonctDict["handled"]])

if __name__ == '__main__':
    dd=DictDonne()
    dd.variable.append(["fisrtVar", 0])
    dd.variable.append(["secvar", 1])
    dd.fonction.append(["firstFonct", 0])
    dd.fonction.append(["secFonct", 1])
    
    print dd.serialize()
    dd.deserialize(dd.serialize())
    print dd.serialize()
    