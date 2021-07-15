# Abstract Class
'''
- A class derived from ABC class which belongs to abc module (pre-defined module) is known as abstract class in python.

- ABC class is known as Meta class which means a class that defines the behaviour of other classes.

- So we can say, Meta class ABC defines that the class which is derived from it becomes an abstract class.

- Abstract class can have abstract method and concrete methods.
- Abstract class needs to be executed and its method implemented.
- PVM (Python Virtual Machine) can't create objects of an abstract class.

Eg:

from abc import ABC, abstractmethod

class Father(ABC):          # yo Abstract class ho 


'''

# Abstract Method
'''
- An abstract method is a method whose action is redefined in the child classes as per the requirement of the object.
- We cab declare a method as abstract method by using @abstractmethod decorator.

Eg:

from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):         #Abstract Method ko declaration matrai huncha definition (body) hundaina
        pass 
'''