'''
join(): This method is used to wait till the thread completely executes the run() method.

'''

from threading import Thread
class MyThread(Thread):
    def run(self):      # run() method is override and run() method is called bydefault when thread is started.
        for i in range(5):
            print('Child Thread')

t = MyThread()      # Creating Child Thread
t.start()           # Starting Child Thread

t.join()        # Execution garda pahele child thread i.e 't' thread lai completely execute vayepachi matrai baki aru thread i.e main thread execution garauna cha vani join() method ko use huncha.

for i in range(5):
    print('Main Thread')