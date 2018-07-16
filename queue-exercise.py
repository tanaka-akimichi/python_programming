import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(queue):
    logging.debug('start')
    # queue.put(100)
    # time.sleep(5)
    # queue.put(200)
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()

    time.sleep(3)
    logging.debug('time consuming processing')
    logging.debug('end')

def worker2(queue):
    logging.debug('start')
    # time.sleep(5)
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug('end')


if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(10000):
        queue.put(i)
    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue,))
        t.start()
        ts.append(t)

    # t2 = threading.Thread(target=worker2, args=(queue,))

    # t1.start()
    # t2.start()
    logging.debug('tasks are not done')
    queue.join()
    logging.debug('tasks are done')
    for _ in range(len(ts)):
        queue.put(None)
    [t.join() for t in ts]

    t.join()
