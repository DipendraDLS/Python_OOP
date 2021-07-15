'''
- In python, the interface con cept isn't explicitly available like available in othe language e.g. Java.
- In pythonm an interface is an abstract class which contains only abstract method but not a single concrete method.

Eg:
from abc import ABC, abstractmethod
class Father(ABC):          #Inside this class there must be only abstractmethod not concrete method to make it as interface.
    @abstractmethod
    def disp(self):
        passs
'''

#Rules to be followed to create an Interface

'''
- All method of an interface is abstract.
- We can't create object of Interface
- If a class is implementing an interface it has to define all the methods given in that interface.
- If a class doesn't implement all the methods declared in the interface, the class must be declared abstract.

'''
# When to use Interface
'''
- We use interface when all the features need to be implemented differently for different objects.

'''