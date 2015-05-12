import os
import pp
import time
import random

print 'pid=%d' % os.getpid()

def worker(i):
    print 'pid=%d ppid=%d i=%d' % (os.getpid(), os.getppid(), i)
    time.sleep(random.randint(1, 3))

servers = ('127.0.0.1:10000', '127.0.0.1:10001', '127.0.0.1:10002')
job_server = pp.Server(1, ppservers=servers)

jobs = list()
for i in xrange(10):
    job = job_server.submit(worker, args=(i,), modules=('time', 'random'))
    jobs.append(job)

for job in jobs:
    job()
