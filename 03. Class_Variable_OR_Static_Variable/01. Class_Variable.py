'''
Class variables are the variables whose single copy is available to all the instance of the class.
If we modify the copy of the class variable in an instance, it will effect all the copies in the other instance.

'''

class Mobile:
    fp = 'Yes'
    def __init__(self) -> None:
        self.model = 'Redmi Note 5'
    
    def show_model(self):
        print(self.model)
    
    @classmethod        # yo classmethod decorator rakhna parcha if you want to make classmethod.
    def is_fp(cls):     # yo class method ho
        print('Finger Print: ', cls.fp)          # class variable ho .... Accessing class variable inside class method
    
    
    
# No matter how many objects are created but class variable shares single copy for all the objects (i.e fp vanni class varaible single copy available huncha.)
obj_1 = Mobile()
obj_2 = Mobile()
obj_3 = Mobile()



# Accessing class variable outside the class

print(Mobile.fp)        # Accessing the class variable outside the class 
Mobile.is_fp()          # Accessing the class method outside the class



# if single copy for class variable is changed then it will also change for all the objects 
Mobile.fp = 'No'

print('obj_1: ', obj_1.fp)
print('obj_2: ', obj_2.fp)