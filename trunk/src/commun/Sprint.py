#-*- coding: iso-8859-1 -*-
'''
Created on 9 mai 2009

@author: Jonatan Cloutier
'''
import TaskList
class Sprint:
    DATEFIN="nomClasse"
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
        return {self.DATEFIN:self.nomClasse,self.TASKGEN:self.taskGeneral.serialize,self.TASKFULL:self.taskFull.serialize}
    
    def deserialize(self, serializedSprint):
        self.dateFin=serializedSprint[self.TASKGEN]
        self.taskGeneral.deserialize(serializedSprint[self.TASKGEN])
        self.taskFull.deserialize(serializedSprint[self.TASKFULL])