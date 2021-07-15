from abc import ABC, abstractmethod

class Father(ABC):          # To define Interface there must be only abstract methods within the class. There shouldn't be any concrete method.
    @abstractmethod
    def disp(self):
        pass

class Child(Father):
    def disp(self):
        print('Defining Abstract Method')
        
c = Child()
c.disp()