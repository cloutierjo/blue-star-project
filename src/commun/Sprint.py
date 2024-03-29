#-*- coding: iso-8859-1 -*-
'''
Created on 19 mai 2009

@author: Jonatan Cloutier
'''
import TaskList
import time

class LstSprint:
    def __init__(self):
        self.sprints=[]              
        
    def unicodize(self):
        for i in self.sprints:
            i.unicodize()
    
    def serialize(self):
        self.unicodize()
        serSprint=[]
        for i in self.sprints:
            serSprint.append(i.serialize())
        return serSprint
    
    def deserialize(self, serSprint):
        self.sprints=[]
        for i in serSprint:
            sprint=Sprint()
            sprint.deserialize(i)
            self.sprints.append(sprint)
    
    def getSprint(self,date):
        dte=time.strptime(date, "%Y-%m-%d")
        retSprint=None
        for i in self.sprints:
            spDte=time.strptime(i.dateFin, "%Y-%m-%d")
            if dte<spDte:
                retSprint=i
        return retSprint

    
class Sprint:
    DATEFIN="dateFin"
    TASKGEN="taskGen"
    TASKFULL="taskFull"
    
    def __init__(self):
        self.dateFin = ""
        self.taskGeneral = []       # doit etre de format ["name",handled]
        self.taskFull = TaskList.TaskList()   
        
    def unicodize(self):
        self.dateFin=unicode(self.dateFin)
        for i in self.taskGeneral:
            i[0]=unicode(i[0])
        
            
    def serialize(self):
        self.unicodize()
        return {self.DATEFIN:self.dateFin,self.TASKGEN:self.taskGeneral,self.TASKFULL:self.taskFull.serialize()}
    
    def deserialize(self, serializedSprint):
        self.dateFin=serializedSprint[self.DATEFIN]
        self.taskGeneral=serializedSprint[self.TASKGEN]
        self.taskFull.deserialize(serializedSprint[self.TASKFULL])
        
                    
if __name__ == '__main__':
    lsp=LstSprint()
    
    sp=Sprint()
    sp.dateFin="2009-05-20"
    
    sp.taskGeneral.append(["gentask1",0])
    sp.taskGeneral.append(["gentask2",1])
        
    tlf=TaskList.TaskList()
    
    tb=TaskList.Task()
    tb.name="task1b"
    tb.priorite=1
    tb.user = "moib"
    tlf.tasklist.append(tb)
    
    tb=TaskList.Task()
    tb.name="task2b"
    tb.priorite=2
    tb.user = "301b"
    tlf.tasklist.append(tb)
    
    sp.taskFull=tlf
    
    lsp.sprints.append(sp)
    
    sp=Sprint()
    sp.dateFin="2009-06-20"
    
    sp.taskGeneral.append(["gentask1",0])
    sp.taskGeneral.append(["gentask2",1])
        
    tlf=TaskList.TaskList()
    
    tb=TaskList.Task()
    tb.name="task1b"
    tb.priorite=1
    tb.user = "moib"
    tlf.tasklist.append(tb)
    
    tb=TaskList.Task()
    tb.name="task2b"
    tb.priorite=2
    tb.user = "301b"
    tlf.tasklist.append(tb)
    
    sp.taskFull=tlf
    
    lsp.sprints.append(sp)
    
    print lsp.serialize()
    lsp.deserialize(lsp.serialize())
    print lsp.serialize()    
                
    print lsp.getSprint("2009-06-10").dateFin