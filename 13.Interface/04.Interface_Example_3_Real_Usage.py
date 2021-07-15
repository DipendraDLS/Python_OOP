# When to use Interface
'''
- We use interface when all the features need to be implemented differently for different objects.

- In given example different classes (Army, AirForce, Navy) has different features for gun and area for this purpose we use Interface.
'''


from abc import ABC, abstractmethod

# Interface as there are only abstract methods within the class
class DefenseForce(ABC):
    @abstractmethod
    def gun(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Army(DefenseForce):
    def gun(self):
        print('Army Gun: AK47')
    
    def area(self):
        print('Army Area: Land')
        
class AirForce(DefenseForce):
    def gun(self):
        print('AirForce Gun: Launcher')
    
    def area(self):
        print('AirForce Area: Air')

class Navy(DefenseForce):
    def gun(self):
        print('Navy Gun: Snipper')
    
    def area(self):
        print('Navy Area: Ocean')


a = Army()
a.gun()
a.area()

af = AirForce()
af.gun()
af.area()

n=Navy()
n.gun()
n.area()