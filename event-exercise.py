import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(queue):
    event.wait()
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')

def worker2(queue):
    event.wait()
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')

def worker3(queue):
    # event.wait()
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    event.set()


if __name__ == '__main__':
    event = threading.Event()
    t1 = threading.Thread(target=worker1, args=(event,))
    t2 = threading.Thread(target=worker2, args=(event,))
    t3 = threading.Thread(target=worker3, args=(event,))
    t1.start()
    t2.start()
    t3.start()

