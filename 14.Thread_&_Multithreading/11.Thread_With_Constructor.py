from threading import Thread

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)       # Parent class 'Thread' ko constructor lai call gareko 
        print('Child Thread')

t = MyThread()
t.start()

print('Main Thread')
    