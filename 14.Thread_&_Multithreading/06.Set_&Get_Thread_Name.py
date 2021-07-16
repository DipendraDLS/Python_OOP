'''
1. current_thread() : This function return current thread object.
2. getName(): Every thread has a name by default, to get the name of thread we can use this method.
3. setName(name): This method is used to set the name of thread.
4. name Property : This property is used to get or set name of thread.

'''


# from threading import Thread, current_thread

# def disp():
#     print("Child Thread Object", current_thread().getName())        #current_thread() returns the current thread object.
#                                                                     #getName() will return the thread name 

# t1 = Thread(target=disp)
# t2 = Thread(target=disp)
# t1.start()
# t2.start()

# # Bydefault huni thread vaneko chai main thread ho.
# print("Main Thread: ", current_thread().getName())



# Set our own name for thread object
from threading import Thread, current_thread

def disp():
    print("Default Child Thread Object", current_thread().getName())  
    # To set our own thread name
    current_thread().setName('My Child Thread')
    print("New Child Thread Object", current_thread().getName())        #current_thread() returns the current thread object.
                                                                      #getName() will return the thread name 

t1 = Thread(target=disp)
t2 = Thread(target=disp)
t1.start()
t2.start()

# Bydefault huni thread vaneko chai main thread ho.
print("Default Main Thread: ", current_thread().getName())
current_thread().setName('My Main Thread')
print("New Main Thread: ", current_thread().getName())
