#-*- coding: iso-8859-1 -*-
'''
Created on 19 mai 2009

@author: Jonatan Cloutier
'''

class ScrumList:
    def __init__(self):
        self.scrums=[]              
        
    def unicodize(self):
        for i in self.scrums:
            i.unicodize()
    
    def serialize(self):
        self.unicodize()
        serScrums=[]
        for i in self.scrums:
            serScrums.append(i.serialize())
        return serScrums
    
    def deserialize(self, serScrums):
        self.scrums=[]
        for i in serScrums:
            scrum=Scrum()
            scrum.deserialize(i)
            self.scrums.append(scrum)
            
    def getDateLst(self):
        datelst=[]
        for i in self.scrums:
            if not i.date in datelst:
                datelst.append(i.date) 
        return datelst
    def getScrum(self,date,user):
        for i in self.scrums:
            if date==i.date and user==i.user:
                return i
            
class Scrum:
    DATE="date"
    DONE="done"
    USER="user"
    TODO="todo"
    PROBLEME="probleme"
    
    def __init__(self):
        self.date = ""
        self.user=""
        self.done = []
        self.todo=[]
        self.probleme=[]
        
    def unicodize(self):
        self.date = unicode(self.date)
        self.user = unicode(self.user)
        for row in self.done:
            row[0] = unicode(row[0])
        for row in self.todo:
            row[0] = unicode(row[0])
        for row in self.probleme:
            row[0] = unicode(row[0])
        
    def serialize(self):
        self.unicodize()
        return {self.DATE:self.date,self.USER:self.user,self.DONE:self.done,self.TODO:self.todo,self.PROBLEME:self.probleme}
    
    def deserialize(self, serializedTask):
        self.date=serializedTask[self.DATE]
        self.user=serializedTask[self.USER]
        self.done=serializedTask[self.DONE]
        self.todo=serializedTask[self.TODO]
        self.probleme=serializedTask[self.PROBLEME]
                
if __name__ == '__main__':

    scl=ScrumList()
    
    sc=Scrum()
    
    sc.date="19 mai"
    sc.user="moi"
    sc.done.append(["fais1",0])
    sc.done.append(["fais2",0])
    sc.todo.append(["afaire1",0])
    sc.todo.append(["afaire2",0])
    sc.probleme.append(["prob1",0])
    sc.probleme.append(["prob2",0])
    
    scl.scrums.append(sc)
    
    sc=Scrum()
    
    sc.date="20 mai"
    sc.user="s01"
    sc.done.append(["fais1",0])
    sc.done.append(["fais2",0])
    sc.todo.append(["afaire1",0])
    sc.todo.append(["afaire2",0])
    sc.probleme.append(["prob1",0])
    sc.probleme.append(["prob2",0])
    
    scl.scrums.append(sc)
    
    print scl.serialize()
    scl.deserialize(scl.serialize())
    print scl.serialize()    
    
    print scl.getDateLst()
                