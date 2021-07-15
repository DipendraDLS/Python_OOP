from abc import ABC, abstractmethod        # abc inbuilt module ho for abstract class ko lagi

class Father(ABC): # Abstract class banauna ABC lai Inherit gareko
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print('concrete method')


class Child(Father):
    def disp(self):
        print('Child Class')
        print('Defining Abstract method')

# Father() class ko object create garna mildaina becz it's abstract class

obj1 = Child()
obj1.disp()
obj1.show()