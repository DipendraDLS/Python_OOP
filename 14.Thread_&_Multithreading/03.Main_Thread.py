'''
When we start any Python Program, one thread begins running immediately, which is called Main Thread of that program created by PVM(Python Virtual Machine)

'''

import threading

t = threading.current_thread().getName()
print(t)