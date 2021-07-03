class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def __str__(self):          # yedi yo method narakhi simply Employee class ko object i.e 'emp' lai print garyo vani <__main__.Employee object at 0x0000013CE00DBFD0> non readable form ma auncha so pbject print garda readable form ma aawos vanera yo __str__(self) dunder method use garincha.
        
        return self.firstname
        # yesari ni return garna milcha duita kura return garna cha vani
        # return '{} {}'.format(self.firstname, self.lastname)

emp = Employee("Dipendra", "Shrestha")

print(emp)      