
# Creating the Class named 'Mobile'
class Mobile:
    
    # Initializing the member variable. This is self calling constructor whenever the object is created this constructor is self called.
    def __init__(self):
        self.model = 'Redmi Note 5 Pro'
    
    
    # Defining the member function/method 
    def show_model(self):
        print('Model Name: ', self.model)
        
obj_1 = Mobile()                # Creating the object named as obj_1 for class Mobile.
obj_1.show_model()              # Accessing  the method using the object which is inside the 'Mobile' class.

obj_1.model                     # Accessing the member variable using object.