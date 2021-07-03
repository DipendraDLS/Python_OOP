# In Multi-Level inheritance, the class inherits the feature of another derived class.

# Syntax:
'''
class ParentClassName(object):
    members of Parent Class

class ChildClassName(ParentClassName):
    memeber of Child Class
    
class GrandChildClass(ChildClassName):
    members of Grand Child Class
    
'''

# Class harulai serially inherit gardai janu 

class Father:
    def __init__(self):
        print("Father Class Constructor")
        
    def showF(self):
        print("Father Class Method")


class Son(Father):
    def __init__(self):
        print("Son Class Constructor")
    
    def showS(self):
        print("Son Class Method")
        
        
        
class GrandSon(Son):
    def __init__(self):
        print("GrandSon Class Constructor")
    
    def showG(self):
        print("GrandSon Class Method")


g= GrandSon()
g.showG()
g.showF()
g.showS()