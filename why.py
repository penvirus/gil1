import pyev
import signal
import sys

def alarm_handler(watcher, revents):
    sys.stdout.write('.')
    sys.stdout.flush()

def timeout_handler(watcher, revents):
    loop = watcher.loop
    loop.stop()

def int_handler(watcher, revents):
    loop = watcher.loop
    loop.stop()

if __name__ == '__main__':
    loop = pyev.Loop()

    loop.timer(0.0, 1.0, alarm_handler).start()

    #timeout = loop.timer(0.0, 1.0, alarm_handler)
    #timeout.start()
    #timeout = loop.timer(10.0, 0.0, timeout_handler)
    #timeout.start()

    loop.start()
