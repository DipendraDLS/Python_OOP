''' 
A Python class is group of attribute and methods.

What is attribute?
=> Attributes  are represented by variables that contains data.

What is Method?
=> Method performs an action or a task. It's is similar to function.

'''





############# Syntax For Class ##############################

'''
class Class_Name(object):
    
    #class member variable should be initialize in self calling constructor so that whenever the object is created variables get automatically initilization.
    
    def __init__(self):
        self.variable_name = 'value'
        self.variable_name = 'value'
    
    def method_name(self):
        # Body of Method
        pass

    

In Above Syntax:

- class => class is a keyword used to create a class.
- object => (object) represents the base class name from where all classes in Python are derived. This is optional one.
- __init__() => This method(actually constructor) is used to initialize variables. This is a special method. We don't have to call this method explicitly.
- self => self is a variable which refers to the current class instance/object.
 
'''





############################ Object #####################################

'''
- Object is a class type variable or class instance. To use a class, we should create an object to the class.
- Instance creation represents the alloting memory necessary to store the actual data of the variables.
- Each time you create an object of the class a copy of each variable is defined within a class.

'''
########################## Syntax For Creating Object #################################
'''
object_name = class_name()
object_name = class_name(args) #if you have arguments in class name.

'''



############################### Syntac For Accessing class member using object #######################
'''
We can access variable and method of class using class object or instance of class. 

object_name.variable_name       # For calling variable of class 
object_name.method_name()       # For calling method of class

'''








