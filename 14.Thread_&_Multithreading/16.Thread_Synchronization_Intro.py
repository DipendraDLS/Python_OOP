'''
- Thread Synchronization : Many threads trying to access the same object can lead to problems like making data inconsistent
                           or getting unexpected output. So when a thread is already accessing an object preventing any other
                           thread accessing the same object is called Thread Synchronization.
  
- The object on which the threads are synchronized is called Synchronized Object or Mutually Exclusive Lock(mutex).

- Thread Synchronization is recommended whene multiple threads are acting on the same object simultaneously.

- There are following techniques to do Thread Synchronization:
    => Using Locks
    => Using RLock(Re-Entrant Lock)
    => Using Semaphores
  
  
- Locks:  Locks are typically used to synchronize access to a shared resource. Lock can be used to lock the object in which the thread is acting.
          A Lock has only two states, locked and unlocked. It is created in the unlocked state.
          There are two method that is used in locks:
          
          => acquire() : This method is used to changes the state to locked and returns immediately. When the state is locked, acquire() blocks until 
                         a call to release() in another thread chages it to unlocked, then the acquire() call resets it to locked and returns.
                         
                         Syntax:- acquire(blocking=True, timeout=-1)
                         
                         - True: It blocks the thread until the lock is unlocked and then it  return True.
                         - False: It doesn't block the thread.
                         - Timeout: It represents for time duration for the thread to be blocked. A timeout argument of -1 specifies an unbounded wait. 
                                    It is forbidden to specify a timeout when blocking is false.
                          
                        
                         - This return value is True if the lock is acquired successfully, False if not (for example if the timeout expired.)
                        
            => release() : This method is used to release a lock. This can be called from any thread, not only the thread which has acquired the lock.
                            When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, 
                            allow exactly one of them to proceed.
                            When invoked on an unlocked lock, a RuntimeError is raised.
                            Threr is no return value.
                            
                            Syntax:
                            release()
                            
'''