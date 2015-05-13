import threading

duration = 10

def internal_busy():
    import time

    begin = time.time()
    while True:
        if time.time() - begin > duration:
            break

def external_busy():
    from ctypes import CDLL
    from ctypes import c_uint, c_void_p

    libbusy = CDLL('./busy.so')
    busy_wait = libbusy.busy_wait
    busy_wait.argtypes = [c_uint]
    busy_wait.restype = c_void_p

    busy_wait(duration)

print 'two internal busy threads, CPU utilization cannot over 100%'
t1 = threading.Thread(target=internal_busy)
t1.start()
t2 = threading.Thread(target=internal_busy)
t2.start()
t1.join()
t2.join()

print 'with one external busy thread, CPU utilization gains to 200%'
t1 = threading.Thread(target=internal_busy)
t1.start()
t2 = threading.Thread(target=external_busy)
t2.start()
t1.join()
t2.join()
