'''
- The Queue class of queue module is useful to create a queue that holds the data produced by the producer.
- The data can be taken from the queue and utilized by the consumer.
- We need not use locks since queues are thread safe.

- Create Queue Object:
from queue import Queue
q=Queue()

- Queue Methods:
    => put(): This method is used by Producer to insert items into the queue.
              Syntax: queue_object.put(item)
              Eg: q.put(i)


    => get(): This method is used by Consumer to rerieve items from the queue/
              Syntax: producer_object.queue_object.get(item)
              Eg: p.q.get(i)
    
    => empty(): This method returns True if queue is Empty else return False.
              Eg: q.empty()
              
    => full(): This method returns True if queue is Full else return False.
              Eg: q.full()
    
'''
from threading import Thread
from queue import Queue
from time import sleep

class Producer:
    def __init__(self):
        self.q = Queue()        # Queue Object banayeko
        
    
    def produce(self):      
        for i in range(1,6):
            print('Item Produced', i)
            self.q.put(i)        # inserts item into queue
            sleep(1)     
            

class Consumer:
    def __init__(self, prod):   # prod ma producer ko object auncha.. yo producer ko object kina chaincha ta vanda becz producer le produce garera queue ma rakheko kura hamilai queue bata get garnu parcha.
        self.prod = prod
    
    
    def consume(self):
        for i in range(1,6):
            print('Item Received', self.prod.q.get(i))  # Producer class le produce garera Queue ma rakheko item lai get gareko.
                                                        # Producer class le produce gareko ra queue ma rakheko item lai get garna self.prod.q.get() garna parcha.  
            sleep(1)
            

p = Producer()
c = Consumer(p)     # producer ko object consumer class ma pass gardeko jun chai construnctor le lincha

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()