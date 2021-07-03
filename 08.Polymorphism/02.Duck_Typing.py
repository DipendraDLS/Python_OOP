#Duck Typing
'''
In Python, we follow a principle- If 'it walks like a duck and talks like a duck, it must be a duck' 
which means python doesn't care about which class of object it is, if it is an object and required behavior is present 
fot that object then it will work. The type of object is distinguished only at runtime.This is called duck typing.

'''
class Duck:
    def walk(self):
        print("Duck walk slowly")
    
class Horse:
    def walk(self):
        print("Horse walk fast")


class Cat:
    def talk(self):
        print("Mewooooo")


def myFuction(obj):     # function call hunda kun object ayera cha matlab hundaina if tyo class bhitra method available cha vani object.attribute() garera tyo attribute  call huncha
    obj.walk()

d = Duck()
myFuction(d)

h = Horse()
myFuction(h)


# yo garda chai error auncha becz Cat() class ma method/attribute walk() vanni chaina so..
# c= Cat()
# myFuction(c)
