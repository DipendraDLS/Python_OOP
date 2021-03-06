'''
- Condition class is used to improve speed of communication between threads.
- The condition class object is called condition variable(Officially called).
- A condition variable is always associated with some kind of lock; this can be passed in or one will be created by default.
- Passing one in is useful when several condition variables must share the same lock. The lock is part of the condition object: 
  you don't have to track it separately.
- A condition is a more advanced version of the event object.


- Create Condition Object:

from threading import Condition
cv = Condition()

- Some Condition Method:
    => notify(n=1): This method is used to immediately wake up one thread waiting on the condition. Where 'n' is number of thread need to wake up.
    
    => notify_all(): This method is used to wake up all threads waiting on the condition.
    
    => wait(timeout=None): This method wait until notified or until a timeout occurs. If the calling thread has not acquired the lock when this method is called, a 
                         RuntimeError is raised. Wait terminates when invokes notify() method or notify_all() method. The return value is True
                         unless a given timeout expired, in which case it is False.
'''

from threading import Thread, Condition
from time import sleep
lst = []

def produce():
    cv.acquire()        # Lock acquire gareko 
    for i in range(1,6):
        lst.append(i)   # khali list ma 1,2,3,4,5 append huncha
        sleep(1)        # 1 sec ko delay produce dincha 
        print('Item Produced...')   
        
    cv.notify()         # notify() le wait() lai notify garcha wakeup huna lai
    cv.release()

def consume():  
    cv.acquire()        # lock acquire garcha
    cv.wait(timeout=0)  # wait() le notify() le notify nagarey samaa wait garera bascha.
    cv.release()        # sabai flag lai reset garera lock release garera False banai dincha
    print(lst)
    
    
cv = Condition()
t1 = Thread(target=produce)
t2 = Thread(target=consume)
t1.start()
t2.start()
