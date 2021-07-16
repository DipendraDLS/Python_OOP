'''
- Race condition is a situation that occurs when threads are acting in an unexpected sequence, thus leading to unreliable output.

- This can be eliminated using thread synchronization.
'''

from threading import Thread, current_thread
 

class Flight(Thread):
    def __init__(self, availabe_seats):
        self.available_seats = availabe_seats
    
    def reserve(self, needed_seat):
        print('Available Seats: ', self.available_seats)
        
        if (self.available_seats >= needed_seat):
            name = current_thread().name
            print(f'{needed_seat} seat is alloted for {name}')
            self.available_seats -= needed_seat
        
        else:
            print('Sorry! All seats has alloted')

f = Flight(1)

t1 = Thread(target=f.reserve, args=(1,), name='Raman')
t2 = Thread(target=f.reserve, args=(1,), name='Baman')
t1.start()
t2.start()

#NOTE: yesma  kun thread ko pahele execution vanera fix hunaa so yesma pani Race condition aunxa.  