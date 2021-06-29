'''
=> In python, Namespace represents a memory block where names are mapped to objects.
Class Namespace -  A class maintains it's own namespace known as class namespace. In the class namespace, the names are mapped to class variables.

Instance Namespace - Every instance have it's own namespace known as instance namespace. In the instance namespace, the names are mapped to instance variables.

'''


# class variable map hunu lai Class Namespace vanxa.

class Mobile:
    fp = 'yes'      # Class Namespace 
    
    
    @classmethod
    def is_fp(cls):
        print("Finger Print: ", cls.fp)
    
        

# 'fp' vanni class variable ko single copy sabai object sanga share huncha
Mobile.fp = 'No'       # yedi class name bata class variable lai modify gareko cha vani sabai object lai changes huncha 

obj_1 = Mobile()        # Instance Namespace
obj_2 = Mobile()        # Instance Namespace
obj_3 = Mobile()        # Instance Namespace

print('obj_1 ', obj_1.fp)
print('obj_2 ', obj_2.fp)
print('obj_3 ', obj_3.fp)

obj_1.is_fp()




# Accessing class variable with Instance Namespace

obj_1.fp = 'Not working' # yedi object name bata class variable lai change gardai cha vani only tyo object ma changes auncha 
print('obj_1 ', obj_1.fp)
print('obj_2 ', obj_2.fp)
print('obj_3 ', obj_3.fp)
