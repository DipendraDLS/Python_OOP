'''
- Main Thread is always non-daemon thread.
- Rest of the threads inherits daemon nature from their parents.
    - If parent thread is non daemon then child thread will become non-daemon thread.
    - If parent thread is daemon then child thread will also become a daemon thread.
- When last non-daemon thread terminates, automatically all daemon threads will be terminated. We are not required to terminate daemon
  thread explicitly.
'''

from threading import Thread, current_thread
def disp():
    print('Disp Function')


mt = current_thread()           # main thread ko object bancha becz current_thread() ma by default main thread huncha 
print(mt.getName())
print('MT: ', mt.isDaemon())    # main thread bydefault non-daemon huncha 

t1 = Thread(target=disp)        # Child thread 
print('T1: ', t1.isDaemon())    # As main thread non-daemon thread ho ra baneko child thread pani non-daemon thread nai huncha.
