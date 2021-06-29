'''
- Static Methods are used when some processing is related to the class but doesn't need the class or its instance to perform any work.
- We use static method when we want to pass some alues from outside and perform some action in the method.
- Decorator @staticmethod need to write above the static method.
'''
# Syntax
'''
@staticmethod
def method_name():          # static method without formal arguments
    method body
    
    
@staticmethod
def method_name(f1,f2):      # static method with formal arguments... static method ko actual use vaneko with prameter nai huncha 
    method body
'''

class Mobile:
    fp ='yes'
    @staticmethod
    def show_model():
        print('Finger Print : ', Mobile.fp)

obj_1 = Mobile
Mobile.show_model()
    
    
    
    
class MyMobile:
    @staticmethod
    def show_model(f1, f2):     # static method with formal argument.
        model = f1
        price = f2
        print('Model: ', model, 'Price: ', price)
        
obj_1 = MyMobile
obj_1.show_model('Redmi', 2000)