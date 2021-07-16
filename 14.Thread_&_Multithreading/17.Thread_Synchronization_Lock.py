from threading import Thread, current_thread, Lock


class Flight(Thread):
    def __init__(self, availabe_seats):
        self.available_seats = availabe_seats
        self.l = Lock()
        #print(self.l)       # Lock() object ho 
        
    def reserve(self, needed_seat):
        #lock maintain gareko
        self.l.acquire(blocking=True, timeout=2)        # blocking and timeout nahalda ni huncha bydefault lincha. bydefault blocking= True huncha.
        
        print('Available Seats: ', self.available_seats)
        
        if (self.available_seats >= needed_seat):
            name = current_thread().name
            print(f'{needed_seat} seat is alloted for {name}')
            self.available_seats -= needed_seat
        
        else:
            print('Sorry! All seats has alloted')
        
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