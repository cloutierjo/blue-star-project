#-*- coding: iso-8859-1 -*-
'''
Created on 8 avr. 2009

@author: Jonatan Cloutier
'''
import Analyse
import CasUsage
import DictDonne
import Crc
import User
import Sprint
import Scrum
import TaskList

class Projet(object):
    '''
    contient tout les informations d'un projet ainsi que des méthode 
    utilitaire pour en simplifier l'accès
    '''

    NOMPJ="nompj"
    NUMPJ="numpj"
    MANDAT="mandat"
    analyseIMPLICITE="analyseImplicite"
    analyseEXPLICITE="analyseExplicite"
    CASETSCENARIO="casEtScenario"
    DICTDONNE="dictDonne"
    CRC="CRC"
    USER="User"
    SPRINT="sprint"
    SCRUM="scrum"
    
    def __init__(self):
        '''
        Constructor
        '''
        self.nom = "" # Sinon j'ai plein d'erreur de Allow None en XMLRPC...(Mathieu)
        self.num = 0    # Vaut 0 pour nouveau projet et ID du projet lorsque loadé
        self.mandat = ""# Sinon j'ai plein d'erreur de Allow None en XMLRPC... (Mathieu)
        self.analyseExplicite = Analyse.Analyse(self)
        self.analyseImplicite = Analyse.Analyse(self)
        self.casEtScenario=CasUsage.CasUsage()
        self.dictDonne=DictDonne.DictDonne()
        self.crc=Crc.LstCrc()
        self.user=User.User()
        self.sprint=Sprint.LstSprint()
        self.scrum=Scrum.ScrumList()
        
    def serialize(self):
        self.unicodize()  #néscéssaire pour que les char unicode passe sur le réseau
        return {self.NOMPJ:self.nom,self.NUMPJ:self.num,self.USER:self.user.serialize(),self.MANDAT:self.mandat,self.analyseEXPLICITE:self.analyseExplicite.analyse,self.analyseIMPLICITE:self.analyseImplicite.analyse,self.CASETSCENARIO:self.casEtScenario.serialize(),self.DICTDONNE:self.dictDonne.serialize(),self.CRC:self.crc.serialize(),self.SPRINT:self.sprint.serialize(),self.SCRUM:self.scrum.serialize()}
    
    def deserialize(self, serializedProject):
        self.nom=serializedProject[self.NOMPJ]
        self.num=serializedProject[self.NUMPJ]
        self.mandat=serializedProject[self.MANDAT]
        self.analyseExplicite.analyse=serializedProject[self.analyseEXPLICITE]
        self.analyseImplicite.analyse=serializedProject[self.analyseIMPLICITE]
        self.casEtScenario.deserialize(serializedProject[self.CASETSCENARIO])
        self.dictDonne.deserialize(serializedProject[self.DICTDONNE])
        self.crc.deserialize(serializedProject[self.CRC])
        self.user.deserialize(serializedProject[self.USER])
        self.sprint.deserialize(serializedProject[self.SPRINT])
        self.scrum.deserialize(serializedProject[self.SCRUM])
        
    def unicodize(self):
        if self.nom != None:
            self.nom = unicode(self.nom)
        if self.mandat != None:
            self.mandat = unicode(self.mandat)
        self.analyseExplicite.unicodize()
        self.analyseImplicite.unicodize()
        


if __name__ == '__main__':
    pj=Projet()
    pj.nom="project Name"
    pj.mandat="ceci est un tres tres grand projet comprenant beaucoup d'idée... encore incomplete"
    pj.analyseExplicite.addItem("projet", "faire", "tres long")
    pj.analyseExplicite.addItem("idée","comprant","beaucoup")
    pj.analyseImplicite.addItem("l'analyse", "tester", "implicite")
    pj.unicodize()
    pj.analyseExplicite.getForDB()
    pj.unicodize()
    pj.analyseExplicite.getForDB()
    pj.analyseImplicite.getForDB()
    
    pj.user.user.append("user1")
    
    cu=pj.casEtScenario
    su=cu.addCasUsage("first cas", 1).scenario
    su.addEtapeScenario("a first step", 1)
    su.addEtapeScenario("a second step")
    
    su=cu.addCasUsage("second cas").scenario
    su.addEtapeScenario("b first step", 1)
    su.addEtapeScenario("b second step")
    
    dd=pj.dictDonne   
    dd.variable.append(["fisrtVar", 0])
    dd.variable.append(["secvar", 1])
    dd.fonction.append(["firstFonct", 0])
    dd.fonction.append(["secFonct", 1])
    
    crcs=pj.crc
    
    crc=Crc.Crc()
    crc.nomClasse="uneClasse"
    crc.proprio="quelqu'un"
    crc.responsabilite.append(["fisrtResp", 0])
    crc.responsabilite.append(["secResp", 1])
    crc.collaboration.append(["firstColl", 1])
    crc.collaboration.append(["secColl", 1])
    crc.handled=0
    
    crcs.crcs.append(crc)
    
    crc=Crc.Crc()
    crc.nomClasse="uneAutreClasse"
    crc.proprio="quelqu'un d'autre"
    crc.responsabilite.append(["fisrtResp", 0])
    crc.responsabilite.append(["secResp", 1])
    crc.collaboration.append(["firstColl", 0])
    crc.collaboration.append(["secColl", 1])
    crc.handled=1
    
    crcs.crcs.append(crc)
    
    lsp=Sprint.LstSprint()
    
    sp=Sprint.Sprint()
    sp.dateFin="29 avr"
    
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
    
    pj.sprint=lsp
    
    scl=Scrum.ScrumList()
    
    sc=Scrum.Scrum()
    
    sc.date="19 mai"
    sc.user="moi"
    sc.done.append(["fais1",0])
    sc.done.append(["fais2",0])
    sc.todo.append(["afaire1",0])
    sc.todo.append(["afaire2",0])
    sc.probleme.append(["prob1",0])
    sc.probleme.append(["prob2",0])
    
    scl.scrums.append(sc)
    
    sc=Scrum.Scrum()
    
    sc.date="20 mai"
    sc.user="s01"
    sc.done.append(["fais1",0])
    sc.done.append(["fais2",0])
    sc.todo.append(["afaire1",0])
    sc.todo.append(["afaire2",0])
    sc.probleme.append(["prob1",0])
    sc.probleme.append(["prob2",0])
    
    scl.scrums.append(sc)
    
    pj.scrum=scl
    
    print pj.serialize()
    pj.deserialize(pj.serialize())
    print pj.serialize()