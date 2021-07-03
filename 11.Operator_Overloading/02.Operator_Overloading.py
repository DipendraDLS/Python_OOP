'''
If any Operator performs additional actions other than what it is meant for, it is called operator overloading.
'''

# Duita object lai add garna '+' operator lai overload garera hamiley object add huni banayeka chau

class A: 
    def __init__(self, x):
        self.x = x
        
    # yo tala ko method baanaunu vaneko '+' operator lai overload gardiyeko ho
    def __add__(self, other):       # '+' operator le ki ta string lai add garna sakcha ki na vaye integer haru lai tara object add garni method chaina. 
        return self.x + other.x     # '+' operator le ni aba object haru add garna sakos vanera hamiley __add__(self,other) lai override gardiyeko

class B:
    def __init__(self, x):
        self.x = x

a = A(100)
b = B(200)

# print(a+b)   # python ma duita object add garni testo magic method chaina.. 
             # '+' operator le ki ta string lai add garna sakcha ki na vaye integer haru lai tara object add garni method chaina.
             # Actually call huna parni duita object bich ko '+' operator le => class_name.__add__(self, other) => i.e A.__add__(self, other) yesari ho.
             # so ava hami '+' operator lai overload garchaum kei extra kam thapdiyera i.e duita object haru ko panni addition gardiyera
             
print("Two Object Addition : ", a+b)    # A.__add__(a,b) behind the scene run huncha.