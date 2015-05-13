import threading

duration = 10

def internal_busy():
    import time

    begin = time.time()
    while True:
        if time.time() - begin > duration:
            break

def external_busy_with_lock():
    from busy import with_lock

    with_lock(duration)

def external_busy_without_lock():
    from busy import without_lock

    without_lock(duration)

print 'two busy threads compete for GIL, CPU utilization cannot over 100%'
t1 = threading.Thread(target=internal_busy)
t1.start()
t2 = threading.Thread(target=external_busy_with_lock)
t2.start()
t1.join()
t2.join()

print 'with one busy thread released GIL, CPU utilization gains to 200%'
t1 = threading.Thread(target=internal_busy)
t1.start()
t2 = threading.Thread(target=external_busy_without_lock)
t2.start()
t1.join()
t2.join()
