'''
A class within a class is called nested class or nesting of a class.


'''


class Army:
    def __init__(self):
        self.name = 'Raju'
        self.gn = self.Gun()            # Creating Inner class 'GUN' object
    
    def show(self):
        print('Name: ', self.name)
    
    
    class Gun:
        def __init__(self) -> None:
            self.name = 'AK 47'
            self.capacity = '75 Rounds'
            self.size = '34.3 inch'
            
        def disp(self):
            print("Gun Name : ", self.name)
            print("Gun Capacity: ", self.capacity)
            print("Gun Size : ", self.size)
        
a = Army()
print(a.name)
a.show()


# Inner class ko object directly use garna paundaina step wise jana parcha at first the outer class object and only then the inner class object.
print(a.gn.name)
print(a.gn.capacity)
print(a.gn.size)

a.gn.disp()