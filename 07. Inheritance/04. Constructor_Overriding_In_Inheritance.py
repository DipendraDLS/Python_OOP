'''
What will happen if we define constructor in both class?
=> If we write constructor in the both classes, parent class and child class then the parent class constructor is not available to the child class.
=> In this case only the child class constructor is accessible which means child class constructor is replacing parent class constructor.
=> Constructor overriding is used when programmer want to modify the existing behavior of constructor.
'''


class Father:
    def __init__(self):
        self.money = 1000
        print("Father Class Constructor Called.")
    
    def show(self):
        print("Father Class Instance Method Called.")

class Son(Father):  # Parent class lai inherit gareko
    
    def __init__(self):         # child class constructo is overriding the parent class constructor.
        self.money = 5000
        self.car = 'BMW'
        print("Son Class Constructor.") 
        
    def disp(self):
        print("Son Class Instance Method Called.")
        
        

s = Son()       # object create garda child class ko def __init__(self) constructor call huncha. overriding vako ho

print(s.money)
print(s.car)

s.show()
s.disp()

