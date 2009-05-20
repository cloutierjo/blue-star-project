#-*- coding: iso-8859-1 -*-
'''
Created on 9 mai 2009

@author: Jonatan Cloutier
'''
import TaskList


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
    
    
class Sprint:
    DATEFIN="dateFin"
    TASKGEN="proprio"
    TASKFULL="responsabilite"
    
    def __init__(self):
        self.dateFin = ""
        self.taskGeneral = TaskList.TaskList()
        self.taskFull = TaskList.TaskList()   
        
    def unicodize(self):
        self.dateFin=unicode(self.dateFin)
            
    def serialize(self):
        self.unicodize()
        return {self.DATEFIN:self.dateFin,self.TASKGEN:self.taskGeneral.serialize(),self.TASKFULL:self.taskFull.serialize()}
    
    def deserialize(self, serializedSprint):
        self.dateFin=serializedSprint[self.DATEFIN]
        self.taskGeneral.deserialize(serializedSprint[self.TASKGEN])
        self.taskFull.deserialize(serializedSprint[self.TASKFULL])
        
                    
if __name__ == '__main__':
    lsp=LstSprint()
    
    sp=Sprint()
    sp.dateFin="29 avr"
    
    tlg=TaskList.TaskList()
    
    ta=TaskList.Task()
    ta.name="task1"
    ta.priorite=1
    ta.user = "moi"
    tlg.tasklist.append(ta)
    
    ta=TaskList.Task()
    ta.name="task2"
    ta.priorite=2
    ta.user = "301"
    tlg.tasklist.append(ta)
    
    sp.taskGeneral=tlg
    
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
                