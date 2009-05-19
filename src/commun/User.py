#-*- coding: iso-8859-1 -*-
'''
Created on 20 avr. 2009

@author: Jonatan Cloutier
'''

class User:
    
    def __init__(self):
        self.user = []
          
    def unicodize(self):
        for row in self.user:
            row=unicode(row)
            
    def serialize(self):
        self.unicodize()  #néscéssaire pour que les char unicode passe sur le réseau
        return self.user
    
    def deserialize(self, serializedUser):
        self.user=serializedUser
    
            
if __name__ == '__main__':
    pass