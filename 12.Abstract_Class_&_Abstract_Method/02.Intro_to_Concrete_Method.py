'''
A Concrete method is a method whose action is defined in the abstract class itself.
Eg:

from abc import ABC, abstractmetho
class Father(ABC):
    
    @abstractmethod 
    def disp(self):         #Abstract method as there is only declaration of method but not the definition
        pass
        
    def show(self):         #Concrete/normal method.
        print("Concrete Class")
'''