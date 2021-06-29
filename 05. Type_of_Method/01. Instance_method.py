'''
    Instance methods are the methods which act upon the instance variables of the class.
    Instance method need to know the memory address of the instance which is provided through self variable by default as first parameter for the instance method.
'''
# Syntax for Instance Method
'''
def method_name(self):     # Instance Method without parameter 
    # function body

def method_name(self, f1, f2):  # Instance Method with formal argument
    # function body
'''

# Instance Method without parameter 
class Mobile:
    def __init__(self):
        self.model = 'Redmi Note 5 Pro'
    
    def show_model(self):           
        print(self.model)


obj_1 = Mobile()
obj_1.show_model()        # calling Instance Method
                          # self ko lagi function call ma parameter chaindaina 
                          

# Instance Method with parameter 

class MyMobile:
    def __init__(self):
        self.model = 'Redmi Note 5 Pro'
    
    def show_model(self, p):        #self le currently working object ko address lai rakhna help garcha. yo java ma 'this' keyword vaney jastai ho
        self.price = p
        print("Model :", self.model, "\nPrice:", self.price)
  


obj_1 = MyMobile()
obj_1.show_model(1000)       # calling Instance Method which has parameter