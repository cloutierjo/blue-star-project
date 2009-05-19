#-*- coding: iso-8859-1 -*-
'''
Created on 9 mai 2009

@author: Jonatan Cloutier
'''

class TaskList:
    def __init__(self):
        self.tasklist=[]              
        
    def unicodize(self):
        for i in self.tasklist:
            i.unicodize()
    
    def serialize(self):
        self.unicodize()
        sertasklist=[]
        for i in self.tasklist:
            sertasklist.append(i.serialize())
        return sertasklist
    
    def deserialize(self, sertasklist):
        self.tasklist=[]
        for i in sertasklist:
            tasklist=Planing()
            tasklist.deserialize(i)
            self.tasklist.append(tasklist)
            
class Task:
    NAME="name"
    PRIORITE="priorite"
    USER="user"
    HANDLED="handled"
    
    def __init__(self):
        self.name = ""
        self.priorite=0
        self.user = ""
        self.handled=0
        
    def unicodize(self):
        self.name = unicode(self.name)
        self.user = unicode(self.user)
        
    def serialize(self):
        self.unicodize()
        return {self.NAME:self.name,self.PRIORITE:self.priorite,self.USER:self.user,self.HANDLED:self.handled}
    
    def deserialize(self, serializedCasUsageItem):
        self.nom=serializedCasUsageItem[self.NAME]
        self.priorite=serializedCasUsageItem[self.PRIORITE]
        self.user=serializedCasUsageItem[self.USER]
        self.handled=serializedCasUsageItem[self.HANDLED]
                
if __name__ == '__main__':
    tl=TaskList()
    
    ta=Task()
    ta.name="task1"
    ta.priorite=1
    ta.user = "moi"
    tl.tasklist.append(ta)
    
    ta=Task()
    ta.name="task2"
    ta.priorite=2
    ta.user = "301"
    tl.tasklist.append(ta)
    
    print tl.serialize()
    tl.deserialize(tl.serialize())
    print tl.serialize()    
                