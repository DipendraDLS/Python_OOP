'''
If a class is derived from more than one parent class, then it is called multiple inheritance.

'''

# Syntax

'''
class ParentClassName1(object):
    # members of Parent Class

class ParentClassName2(object):
    # member of Parent Class 
    
class ChildClassName(ParentClassName1, ParentClassName2):
    # member of Parent
    
'''

class Father:
    def __init__(self):
        super().__init__()
        print("Father Class Constructor")
        
    def showF(self):
        print("Father Class Method")

class Mother:
    def __init__(self): 
        super().__init__()                    # Calling Parent Class Constructor
        print("Mother Class Constructor")   
    def showM(self):
        print("Mother Class Method")

class Son(Father, Mother):
    def __init__(self):
        super().__init__()                  # Calling Parent Class Constructor
        print("Son Class Constructor")
    
    def showS(self):
        print("Son Class Method")

s = Son()

#### Method Resolution Order(MRO)####################
'''

- The search will start from Son. As the object of Son is created, the constructor of Son is called.

- Son has super().__init__() inside his constructor so its parent class, the one in the left side 'Father' Class constructor is called.

- Father class also has super().__init__() inside his constructor so its parent object class's constructor is called.

- Object doesn't have any constructor so the search will continue down to right hand side class (Mother) of object class so Mother class's constructor is called.

- As Mother class has super().__init__() so its parent class object constructor is called but as object class already visited the search will stop here.

'''