'''
- If we write method in the both classes parent and child class then the parent class method is not available to the child class.
- In this case only child class's method is accessible which means child class's method is replacing parent class's method.
- Method overriding is used when programmer want to modify the existing behavior of a method.

'''

'''
# Method with super() Method.
- If we write method in the both classes, parent class and child class then the parent class method is not available to the child class.
- In this case only child class method is accessible which means child class's method is replacing parent class's method.
- super() method is used to call parent class's constructor or methods from the child class.

'''
class Add:
    def result(self, x, y):
        print("Add: ", x+y)

class Multi(Add):
    def result(self, a, b):
        super().result(a, b)                # calling the Parent class result()cl method.
        print("Multiplication: ", a*b)

obj = Multi()
obj.result(10, 20)  # By default kei nagarni ho vani child class ko method call huncha.