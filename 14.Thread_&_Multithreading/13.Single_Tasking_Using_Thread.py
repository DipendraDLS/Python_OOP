'''
- When multiple tasks are executed by a thread one by one, then it is called single tasking.
'''

from threading import Thread
from time import sleep
class MyExam(Thread):
    def solve_questions(self):
        self.q1()
        self.q2()
        self.q3()
    
    def q1(self):
        print('Q1 Solved')
        sleep(3)
    
    def q2(self):
        print('Q2 Solved')
        sleep(3)
        
    def q3(self):
        print('Q3 Solved')

mye = MyExam()
t = Thread(target=mye.solve_questions)
t.start()       # Multiple task are being executed one by one.





