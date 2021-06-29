# This method is used to access or read and modify data of the variables. This method modify the data in the variable.
# This is also called a setter method.
class Mobile:
       
    def set_model(self, m):     # setter method ho jasle value lai set garcha 
        self.model = m
        print('Model : ', m)
        
    
obj_1 = Mobile()
m = obj_1.set_model('Redmi Note 5 Pro')
