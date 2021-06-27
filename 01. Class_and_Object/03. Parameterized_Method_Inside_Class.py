
# Creating the Class named 'Mobile'
class Mobile:
    
    # Initializing the member variable. This is self calling constructor whenever the object is created this constructor is self called.
    def __init__(self, m):      # Parameterized self constructor.
        self.model = m
    
    
    # Defining the member function/method 
    def show_model(self, p):
        price = p
        print('Model Name: ', self.model, '\nPrice: ', p)
        
        
        
obj_1 = Mobile('Redmi Note 5 Pro')                # Creating the object named as obj_1 for class Mobile.
                                                  # self constructor takes the parameter so we need to pass the parameter while instatiating the object.
obj_1.show_model(10000)              # Accessing  the method using the object which is inside the 'Mobile' class.


# Creating multiple object for same class and checking the memory address for each object.

obj_2 = Mobile('Samsung')
obj_2.show_model(2000)


obj_3 = Mobile("Oppo")
obj_3.show_model(3000)


# Checking Memory address of each object.. Each object is instantiated with different memory address space.
print('obj_1 Memory address: ', id(obj_1))
print('obj_2 Memory address: ', id(obj_2))
print('obj_3 Memory address: ', id(obj_3))
