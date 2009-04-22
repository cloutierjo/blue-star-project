#-*- coding: iso-8859-1 -*-
'''
Created on 20 avr. 2009

@author: Jonatan Cloutier
'''

class Analyse:
    
    NOM="nom"
    VERBE="verbe"
    ADJECTIF="adjectif"
    HANDLED="handled"
    
    def __init__(self,parent):
            
        self.analyse = []
        self.parent = parent
    
    def getForDB(self):
        anExpTup=[]
        for item in self.analyse:
            anExpTup.append((self.parent.num,item[self.NOM],item[self.VERBE],item[self.ADJECTIF],item[self.HANDLED]))
        return anExpTup
    
    def addItem(self, nom, verbe, adjectif):
        self.analyse.append({self.NOM:nom,self.VERBE:verbe,self.ADJECTIF:adjectif,self.HANDLED:0})
        
    def unicodize(self):
        for row in self.analyse:
            row[self.NOM] = unicode(row[self.NOM])
            row[self.VERBE] = unicode(row[self.VERBE])
            row[self.ADJECTIF] = unicode(row[self.ADJECTIF])