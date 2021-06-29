# Constructor in Inhertance

class Father:
    def __init__(self):
        self.money = 1000
        print("Father Class Constructor Called.")
    
    def show(self):
        print("Father Class Instance Method Called.")

class Son(Father):  # Parent class lai inherit gareko
    def disp(self):
        print("Son Class Instance Method Called.")

s = Son()       # object create garda nai def __init__(self) constructor call huncha.
print(s.money)
s.show()
s.disp()