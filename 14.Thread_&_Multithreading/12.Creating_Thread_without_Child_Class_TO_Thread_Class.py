'''
We can create an independent thread child class that doesn't inherit from Thread class from threading module.

syntax:
class ClassName:
    statements
object_name = ClassName()
Thread_object = Thread(target=object_name.function_name, args=(args1, args2 ....))

'''

from threading import Thread

class MyThread:
    def disp(self, a, b):
        print(a,b)
    
myt = MyThread()
t = Thread(target=myt.disp, args=(10,20))       # class ko object.func_name() garera target ma pass garna parcha
t.start()