from threading import Thread
def disp():
    print('Daemon Thread')

t1 = Thread(target=disp)
print('Before: ',t1.isDaemon())        # Checking whether Thread is Daemon thread or not using 'isDaemon() method.

# print('BeforeL ', t1.daemon)           # Checking whether Thread is Daemon or not using 'daemon' property.
# t1.daemon = True                       # 'daemon' = True garera t1 thread lai daemon thread banauna pani sakincha 


t1.setDaemon(True)                      # Set 't1' Thread as Daemon Thread.
print('After: ', t1.isDaemon())


