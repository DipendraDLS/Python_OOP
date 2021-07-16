'''
- When multiple tasks are executed at a time, then it is called Multi-tasking. For this purpose we need more than one thread and when we use more than one thread, it is called multi-threading.

'''
from threading import Thread
import threading

class Hotel:
    def __init__(self, t):
        self.t = t
        
    
    def food(self):
        for i in range(1,6):
            print(self.t, i)
    
h1 = Hotel('Take Order From Table ')
h2 = Hotel('Serve Order to Table ')

t1 = Thread(target=h1.food)
t2 = Thread(target=h2.food)

t1.start()
t2.start()


#NOTE: Above example is of Multithreading ani yesma ma problem vaneko thread execution hunda kun thread pahel execution huni fix hunna.. yedi 't1' execute navaye 't2' execute vayo vani ta order nai naliii food serve huni task execute huncha.. so this is the problem and these problem in execution sequence of thread is known as Race Condition.
# There are various technique to solve these Race conditions.