'''
# In JAVA yesari yeutai class bhitra more than one  function with the same name banayera overloading garthyo
# BUT in Python testo JAVA ma jasto Overloading hundaina..

public class MethodOverloading
{
    public static void main(String[] args)
    {
        int sumInt = add(5,6); //return gareko value store gareko sumInt ma.
        double sumDouble = add (5.4, 6.6); //return gareko value store gareko sumDouble ma.

        System.out.println("SumInt = " + sumInt);
        System.out.println("SumDouble = " + sumDouble);
    }
    public static int add(int a , int b)
    {
        return (a+b);
    }
    public static double add(double a, double b)
    {
        return a+b;
    }
}
######## Note: Python ma method Overloading Vanni kurai hundaina tara acheive nai garna nasakni chai hoina. ###########

'''

# Method Overloading in Python

class MyClass:
    def sum(self, a=None,b=None,c=None):    # Function call bata kasto signature vako method auncha tha hunna so method overloading achieve garna yo None rakhera tala if else bata garna sakincha
        
        if a!=None and b!=None and c!=None:
            s = a+b+c
            return s
        
        elif a!=None and b!=None:
            s = a+b
            return s
        
        else:
            print("Atleast two number is required.")
    

obj = MyClass()
print("sum is: ", obj.sum(10,20,30))

# yesari duita matai actual argument send garera method overloading garna cha vani Python ma JAVA jasari arko def sum (self, a,b): vanni method banayera garni hoina,
# method overloading use garna cha Python ma vani tei same single function vitrai parameter aaye anusar if else lagayera achieve garna sakincha
# Note Actually Python ma method OVerloading vanni nai hundaina.
 
print("sum is: ", obj.sum(10,20))   



