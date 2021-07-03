'''
class ParentClassName(object):
    members of Parent Class 
    
    
    
class ChildClassName(ParentClassName):
    members of Child Class 2


class ChildClassName2(ParentClassName):
    members of Child Class 2
    
'''

class Father:
    def showF(self):
        print("Father Class Method")
    
    
class Son(Father):
    def showS(self):
        print("Son Class Method")
        
class Daughter(Father):
    def showD(self):
        print("Daughter Class Method")


obj_1 = Daughter()
obj_1.showD() 

obj_2 = Son()
obj_2.showS()