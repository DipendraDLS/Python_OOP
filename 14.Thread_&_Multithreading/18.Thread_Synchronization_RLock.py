'''
- In RLock, same thread can acquire lock multiple times.

- A reentrant lock is synchronization primitive that may be acquired multiple times by the same thread.

- The standard Lock doesn't know which thread is currently holding the lock. If the lock is held, any thread that attempts to acquire it will block
  even if the same thread itself is already holding the lock. In such cases, RLock(re-entrant lock) is used.

- A reentrant lock must be released by the thread that acquired it. Once a thread has acquired a reentrant lock, the same thread may acquire it again without blocking.
  the Thread must release it once for each time it has acquired it.
  
'''
from threading import Thread, current_thread, RLock


class Flight(Thread):
    def __init__(self, availabe_seats):
        self.available_seats = availabe_seats
        self.l = RLock()
        #print(self.l)       # Lock() object ho 
    
    def reserve(self, needed_seat):
        #lock maintain gareko
        self.l.acquire()        # RLock() ma yeutai thread le multiple time lock acquire garna sakcha.
        self.l.acquire()        # blocking and timeout nahalda ni huncha bydefault lincha. bydefault blocking= True huncha.
        
        #print(self.l)       # Lock() object ho 
        
        print('Available Seats: ', self.available_seats)
        
        if (self.available_seats >= needed_seat):
            name = current_thread().name
            print(f'{needed_seat} seat is alloted for {name}')
            self.available_seats -= needed_seat
        
        else:
            print('Sorry! All seats has alloted')
        
        self.l.release()        # jati choti RLock() ma lock acquire gareko huncha teti choti nai release garna parni huncha.
        self.l.release()

f = Flight(2)

t1 = Thread(target=f.reserve, args=(1,), name='Raman')
t2 = Thread(target=f.reserve, args=(1,), name='Baman')
t3 = Thread(target=f.reserve, args=(1,), name='Sonam')
t1.start()
t2.start()
t3.start()


# Main Thread bydefault huni garda cha so tyo main thread bich ma execute navai last ma execute hoss vanera join() method use gareko
t1.join()
t2.join()
t3.join()



print('Main Thread')