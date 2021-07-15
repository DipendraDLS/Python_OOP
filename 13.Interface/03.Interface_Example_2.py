from abc import ABC, abstractmethod

class Father(ABC):          # To define Interface there must be only abstract methods within the class. There shouldn't be any concrete method.
    @abstractmethod
    def disp1(self):
        pass
    
    @abstractmethod
    def disp2(self):
        pass

class Child(Father):
    def disp1(self):
        print('Child Class')
        print('Defining 1st abstract method')
    
class GrandChild(Child):
    def disp2(self):
        print('GrandChild Class')
        print('Defining 2nd abstract method')
            
# We can't make the object of Child class becz all the abstract method (i.e disp1() and disp2()) must be defined first and then only we can make object.
gc = GrandChild()
gc.disp1()
gc.disp2()
