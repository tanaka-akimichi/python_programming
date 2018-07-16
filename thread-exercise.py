import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(d, lock):
    # print(threading.currentThread().getName(), 'start')
    logging.debug('start')
    lock.acquire()
    i = d['x']
    time.sleep(5)
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')
    # print(threading.currentThread().getName(), 'end')

def worker2(d, lock):
    # print(threading.currentThread().getName(), 'start')
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')
    # print(threading.currentThread().getName(), 'end')

if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.Lock()
    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))

    t1.start()
    t2.start()
    print('started')
