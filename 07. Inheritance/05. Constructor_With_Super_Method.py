'''
How can we call parent class constructor if child class overrides the parent class constructor.
=> If you want to access the parent class constructor then you need to create the object of parent class or you can use super() method.

1. Using the parent class object

f = Father()

2. Using the super() method.
'''

class Father:
    def __init__(self):
        self.money = 1000
        print("Father Class Constructor Called.")
    
    def show(self):
        print("Father Class Instance Method Called.")

class Son(Father):  # Parent class lai inherit gareko
    
    def __init__(self):         # child class constructo is overriding the parent class constructor.
        super().__init__()
        self.money = 5000
        self.car = 'BMW'
        print("Son Class Constructor.") 
        
    def disp(self):
        print("Son Class Instance Method Called.")
        
        

s = Son()       # object create garda at  child class ko def __init__(self) constructor matrai call hunthyo tara super() method use gareko vayera aba parent class ko pani constructor call huncha . overriding vako ho and overriding huna bata chai super() method le bachayeko ho

print(s.money)
print(s.car)

s.show()
s.disp()

