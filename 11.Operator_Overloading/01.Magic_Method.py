
# Magic/Dunder Method Behind The Scene..

######################## For Integer=>  int.__add__(self, other) ##################################
print(10+20)       

# Jaba '+' operator duita integer bich garicha taba behind the scene tala ko method call huncha
''' 
int.__add__(self, other)            # 10 + 20 garda '+' operator le yo method call huncha

'''
print(int.__add__(10,20))           # duita number add hunda actually '+' operator le method call gareko huncha behind the scene ma.




####################################### For String => str.__add__(self, other) ################################

print("Hello " + "World")

# Jaba '+' operator duita string bich garicha taba behind the scene tala ko method call huncha
''' 
int.__add__(self, other)            # 10 + 20 garda '+' operator le yo method call huncha

'''
print(str.__add__("Hello ","World"))           # duita number add hunda actually '+' operator le method call gareko huncha behind the scene ma.


# Some commonly used Magic/Dunder Method are 

# __add__(self, other)
# __sub__(self, other)
# __mul__(self, other)
