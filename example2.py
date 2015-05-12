import os
from multiprocessing import Pool

print 'pid=%d' % os.getpid()
pool = Pool(processes=4)

def worker(i):
    print 'pid=%d ppid=%d i=%d' % (os.getpid(), os.getppid(), i)

pool.map(worker, xrange(10))
pool.terminate()
