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

    alarm = loop.timer(0.0, 1.0, alarm_handler)
    alarm.start()

    timeout = loop.timer(10.0, 0.0, timeout_handler)
    timeout.start()

    sigint = loop.signal(signal.SIGINT, int_handler)
    sigint.start()

    loop.start()
