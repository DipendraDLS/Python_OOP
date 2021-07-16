'''
Creating a thread without using a class.


Syntax:

from threading import Thread
thread_object = Thread(target=function_name, args=(args1,args2, .....))


thread_object => It represents our thread.
target => It represents the function on which the thread will act.
args => It represents a tuple of arguments which are passed to the function.

Eg:
t = Thread(target = disp, args = (10,20))


How to start Thread??
=> Once a thread is created it should be started by calling start() method.
'''


# from threading import Thread
# def disp(a):
#     print('Thread Running: ', a)

# t = Thread(target=disp, args=(10,))     # tuple ho args so single parameter send garda (10,) comma is imp for tuple.
# t.start()                               # Starting the thread.




from threading import Thread
def disp():
    for i in range(5):
        print("Child Thread Running")


t = Thread(target=disp)
t.start()

# yo Tala ko for loop Main Thread bata run vako huncha .
# Main Thread .py file banaundai by default baneko huncha
for i in range(5):
    print("Main Thread")
    
#NOTE: yaha duita thread cha yeuta Main Thread ani arko 't' vanni Thread so yo multithread ko process huni sequence different huncha each time program run garda.

