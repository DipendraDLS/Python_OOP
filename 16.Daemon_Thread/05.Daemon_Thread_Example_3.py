from threading import Thread, current_thread
from time import sleep

def teacher():
    for i in range(1, 11):
        print('Teaching Session', i)
        sleep(1)

t1 = Thread(target=teacher)

t1.setDaemon(True)      # 't1' thread lai daemon thread banayeko becz main thread non-daemon thread ho jasle exam finished vani print dincha..
                        # jaba non-daemon thread execute vayera terminate huncha taba daemon thread pani terminate huncha so yesto garna le jaba Exam finished print auncha taba daemon thread pani terminate huncha and further more 'Teaching Session' vanera print aundaina.
                        # 't1' thread lai daemon thread banayena vani 'Main Thread' chalera Exam Finished vanera pani ajhai daemon thread terminate vako hundaina ra output ma Teaching Session vanera ayerakhxha..
                        
t1.start()  
# t1.join()             # 'join()' method halyo vani chai purai t1 thread ko completion vaye pachi matrai main thread chalcha.
                        # i.e sabai Teaching Session sakey pachi matrai Exam Finished vanni msg auncha.             
sleep(6)
print('Exam Finished ', current_thread().name)