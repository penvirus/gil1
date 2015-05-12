import time
from multiprocessing import Process
from threading import Thread
from multiprocessing import Queue as MPQ
from Queue import Queue

MAX = 1000000

def test_(w_class, q_class):
    def worker(queue):
        for i in xrange(MAX):
            queue.put(i)

    q = q_class()
    w = w_class(target=worker, args=(q,))

    begin = time.time()
    w.start()
    for i in xrange(MAX):
        q.get()
    w.join()
    end = time.time()

    return end - begin

def test_sthread():
    q = Queue()

    begin = time.time()
    for i in xrange(MAX):
        q.put(i)
        q.get()
    end = time.time()

    return end - begin

print 'mprocess: %.6f' % test_(Process, MPQ)
print 'mthread:  %.6f' % test_(Thread, Queue)
print 'sthread:  %.6f' % test_sthread()
