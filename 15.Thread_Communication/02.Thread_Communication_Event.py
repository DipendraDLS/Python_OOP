'''
- Event: This is one of the simplest mechanisms for communication between threads. 
         One thread signals an event and other threads wait for it.
         
         An event object manages an internal flag that can be set to true with the set() method and reset to false with the clear()
         method. The wait() method blocks until the flag is true.
         
         The flag is initially false. 
         
- Create Event Object:
    
    from threading import Event
    e = Event()     #'e' is the Event() object. This object maintains the flag.

- Event Methods: 
  => set(): It sets the internal flag to true. All threads waiting for it to become true are awakened. Threads that call wait()
            once the flag is true will not block at all.
  
  => clear(): It resets the internal flag to false. Subsequently, threads calling wait() will block until set() is called to set the 
              internal flag to true again.
  
  => is_set(): It returns true if and only if the internal flag is true.
  
  => wait(timeout=None): It blocks until the internal flag is true. If the internal flag is true on entry, return immediately. Otherwise,
                         block until another thread calls set() to set the flag to true, or until the optional timeout occurs.
                         When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the
                         operation in seconds(or fractions thereof).

'''



from threading import Thread, Event
from time import sleep

def light_switch(): 
    sleep(3)        # Terminal ma after 3sec pachi matrai display aauna suru huncha
    e.set()         # 'e' vaneko event object ho. 'e.set' event le flag lai true banauncha ani duitai thread 't1' and 't2' simulataneously chaleko huncha ra flag set huna bitikai 'e.wait' unblock huncha 
    print('Green Light ON')
    sleep(5)
    print('Red Light ON')
    e.clear()       # It resets the internal flag to false

def traffic():
    e.wait()            # 'e.wait()' block mode ma vayerako huncha.. taba samaa block mode ma huncha jaba samma 'e.set()' flag lai true banaundaina.. jaba flag true huncha 'e.wait()' unblock huncha.
    while e.is_set():
        print('You Can Go...')
        sleep(.5)
    print('Program Done')
    
e = Event()
t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)
t1.start()
t2.start()
