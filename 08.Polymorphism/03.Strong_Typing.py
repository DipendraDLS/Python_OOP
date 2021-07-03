'''
We can check whether the object passed to the method has the method being invoked or not.
hasattr() Function is used to check whether object has a  method or not.
Syntax:- hasattr(object, attribute)
Where attribute can be method or varaible. If it is found in the object then this method returns True else False
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


def myFuction(obj):             # function call hunda kun object ayera cha matlab hundaina if tyo class bhitra method available cha vani object.attribute() garera tyo attribute  call huncha
    if hasattr(obj, 'walk'):    # strong typing gareko.. yedi ayerakheko class ko object ma tyo class vitra 'walk' 
                                # vanni attribute/method cha vani matrai call huncha natra vani obj.walk() run nai hundaina. Yo garda asure vayo ki method cha vani matrai call huni vanera yesailai strong typing vancha
        obj.walk()
     
    if hasattr(obj, 'talk'):   # strong typing gareko.. yedi ayerakheko class ko object ma tyo class vitra 'talk' 
                                # vanni attribute/method cha vani matrai call huncha natra vani obj.walk() run nai hundaina. Yo garda asure vayo ki method cha vani matrai call huni vanera yesailai strong typing vancha
        obj.talk()


d= Duck()
myFuction(d)

c= Cat()
myFuction(c)