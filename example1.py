import os
from multiprocessing import Pool

def worker(i):
    print 'pid=%d ppid=%d i=%d' % (os.getpid(), os.getppid(), i)

print 'pid=%d' % os.getpid()
pool = Pool(processes=4)
pool.map(worker, xrange(10))
pool.terminate()
