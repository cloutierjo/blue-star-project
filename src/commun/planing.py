#-*- coding: iso-8859-1 -*-
'''
Created on 9 mai 2009

@author: Jonatan Cloutier
'''

class LstPlaning:
    def __init__(self):
        self.planing=[]              
        
    def unicodize(self):
        for i in self.planing:
            i.unicodize()
    
    def serialize(self):
        self.unicodize()
        serPlaning=[]
        for i in self.planing:
            serPlaning.append(i.serialize())
        return serPlaning
    
    def deserialize(self, serializedCrcs):
        self.planing=[]
        for i in serializedCrcs:
            planing=Planing()
            planing.deserialize(i)
            self.planing.append(planing)
    


if __name__ == '__main__':
    pass