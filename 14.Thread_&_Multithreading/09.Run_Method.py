'''
run(): Every thread will run this method when thread is started. We can override this method and write our own code as body of the run() Method. A thread will terminate automatically when it comes out of the run() method.

'''
# run() method
from threading import Thread

class MyThread(Thread):
    def run(self):      # run() method lai override gareko yo method thread start hunda automatically call huncha
        print('Run Method Overriden')


t = MyThread()
t.start()

