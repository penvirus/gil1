import os
from multiprocessing import Pool

def worker(i):
    print 'pid %d: %d' % (os.getpid(), i)

pool = Pool(processes=4)
pool.map(worker, xrange(10))
