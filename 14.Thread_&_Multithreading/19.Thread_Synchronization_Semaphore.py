'''
- Semaphore : This is one of the oldest synchronization primitives in the history of computer scicence, 
              invented by the early Dutch computer scientist Edsger W. Dijkstra.
              
              A semaphore manages an internal counter which is decremented by each acquire() call and 
              incremented by each release() call.
              
              The counter can never go below zero; when acquire() finds that it is zero, it blocks waiting
              until some other thread calls release().
              
              It's usually better to use the BoundedSemaphore class, which considers it to be an error to call
              release more often than you have called acquire.            

'''

from threading import BoundedSemaphore, Thread, current_thread, Semaphore


class Flight(Thread):
    def __init__(self, availabe_seats):
        self.available_seats = availabe_seats
        self.l = Semaphore(2)   # Seamaphore() is class in threading and here '2' means the limit of thread that can lock the resources at a time.
        
        # self.l = BoundedSemaphore(2)  # BoundedSemaphore() ma chai exactly jati limit diyeko huncha teti choti nai release garna parcha limit vanda badi release() garyo vani error auncha.
        
        
        #print(self.l)          # self.l object ho 
    
    def reserve(self, needed_seat):
        #lock maintain gareko
        self.l.acquire()        # acquire() call hunda semaphore() ma diyeko thread ko limnit '1' le ghatcha.
        
        print(self.l._value)       # self.l.value le semaphore ko yeuta private varaiable 'value' vanni ma j chatyo print dincha 
        
        print('Available Seats: ', self.available_seats)
        
        if (self.available_seats >= needed_seat):
            name = current_thread().name
            print(f'{needed_seat} seat is alloted for {name}')
            self.available_seats -= needed_seat
        
        else:
            print('Sorry! All seats has alloted')
        
        self.l.release()        # jati choti lock acquire gareko huncha teti choti nai release garna parni huncha.
        self.l.release()        # Semaphore() ma jati limit deko cha teti nai choti release garna parcha, yedi release() limit vanda ni dherai choti release() garyo vani ni error chai aundaina.
                                # BoundedSemaphore() ma chai exactly jati limit diyeko huncha teti choti nai release garna parcha limit vanda badi release() garyo vani error auncha.

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