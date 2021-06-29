'''
- Class methods are the methods which act upon the class variables or static variable of the class.
- @classmethod need to write above the class method.
- By default, the first parameter of class method is cls which regers to the class itself.
'''
 
# Syntax:-
'''
@classmethod
def method_name(self):
    function body
'''

#class method without arguments
class Mobile:
    fp = 'yes'          # class variable
    
    
    @classmethod                # Decorator halnai parcha 
    def show_model(cls):        # 'cls' vanni parameter by de fault dinai parcha for class method.
        print("Finger print: ", cls.fp)

obj_1 = Mobile()
Mobile.show_model()         # class method lai Class name batai call garni chalan cha..
#obj_1.show_model()          # yesari object name bata ni call garna ta milcha but class method ho vani class name batai call garincha.
                            # object name use garni ho vani ta Instance method use garni ho no necessary for class method.
                            

# class method with argument

class MyMobile:
    fp = 'yes'                          # class variable
    
    @classmethod    
    def show_version(cls, ver):         # class method with parameter 
        cls.ver = ver
        print('Finger Print:', cls.fp, '\nVersion: ', cls.ver)
    

obj_1 = MyMobile()
MyMobile.show_version("Android 9.0")
