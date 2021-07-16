'''
- We can create our own thread child class by inheriting Thread module.

Synatax:
class ChildClassName(Thread):
    statements

Thread_object = ChildClassName()

Example:
class MyThread(Thread):
    pass
t = MyThread()
'''

from threading import Thread

class MyThread(Thread):
    pass

t = MyThread()
print(t.name)
