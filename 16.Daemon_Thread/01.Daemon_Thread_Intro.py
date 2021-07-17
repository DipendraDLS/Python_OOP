'''
- A daemon thread is thread which runs continuously in the background.
- It provides support to non-daemon threads.
- When last non-daemon thread terminates, automatically all daemon threads will be terminated.
- We aren't required to terminate daemon thread explicitly.

- Create Daemon Thread:
    => setDaemon(True) Method or daemon = True property is used to make a thread a Daemon thread.
    
    Eg:
        t1 = Thread(target = disp)      # t1 is a non-daemon thread for
        
        t1.setDaemon(True)      # non-daemon thread lai daemon thread banauni tarika... False lekhyo vani chai daemon thread changes to non-daemon thread
               or 
        t1.daemon = True
        

- Daemon Thread Method:
  => setDaemon(True/False): This method is used to set a thread as daemon thread. You can set thread as daemon only before starting that thread which means active
                            thread status can't be changed as daemon.
                            
                            If we pass True non-daemon thread will become daemon and if False daemon thread will become non-daemon.
                            
  
  => daemon Property: This property is used to check whether a thread is daemon or not. It returns True if thread is daemon else False.
                      We can also use daemon property to set a thread as daemon thread or vice versa.
                      
  => isDaemon(): This method is used to check whether a thread is daemon or not. It returns True if thread is daemon else False.
        

NOTE: Main Thread of Python in non-daemon thread.
'''