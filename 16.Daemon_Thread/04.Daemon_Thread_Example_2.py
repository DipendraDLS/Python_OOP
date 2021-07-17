from threading import Thread, current_thread
def disp():
    print('Disp Function')
    t2 = Thread(target=show)
    print('T2: ', t2.isDaemon())
    t2.start()

def show():
    print('Show Function')

mt = current_thread()
print(mt.getName())
print('MT: ', mt.isDaemon())


t1 = Thread(target=disp)        # 't1' thread le 't2' thread banauncha ... 't1' thread bydefault non-dameon thread huncha ra 't1' le banayeko 't2' thread pani non-daemon thread huncha.
print('T1 Before: ', t1.isDaemon())
t1.setDaemon(True)
print('T1 After: ', t1.isDaemon())
t1.start()
t1.join()       # 't1' thread ko fully execution vaye sakey pachhi matrai arko thread(i.e in this case Main Thread) ko kam suru hoss vanera 'join()' method use gareko