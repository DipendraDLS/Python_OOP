'''
- If a class is derived from one base class(Parent Class), it is called single Inheritance.



Declaration of Parent and Child Class

class ParentClassName:              
    member varaible and member function

class ChildClassName(ParentClassName):
    member varaible and member function of Parent Class and Child Class

'''

class Father:
    money = 1000
    def show(self):
        print("Parent Class Instance Method.")
    
    @classmethod
    def show_money(cls):
        print("Parent Class, Class Method: ", cls.money)
    

class Son(Father):  # Parent class lai inherit gareko
    
    def disp(self):
        print("Print Child Class Instance Method")


s = Son()
# s.disp()

#Accessing member of Parent Class
print(s.money)
s.show()
s.disp()