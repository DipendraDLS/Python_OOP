 # Accessor method lai getter method pani vancxha.
 # This method is used to access or read data of the variables. This method don't modify the data in the variable.
 # This is called as getter method.
 
class Mobile:
    def __init__(self):
        self.model = 'Redmi Note 5'
        
    def get_model(self):        # getter method ho jasle data haru get matrai garcha ra get gareko kura lai return gardincha    
        return self.model       


obj_1 = Mobile()
model = obj_1.get_model()   #Accessor method lai call gareko 

print("Model: ", model) 