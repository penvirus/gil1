import gevent
from gevent import signal
import signal as o_signal
import sys

if __name__ == '__main__':
    ctx = dict(stop_flag=False)

    def int_handler():
        ctx['stop_flag'] = True
    gevent.signal(o_signal.SIGINT, int_handler)

    count = 0
    while not ctx['stop_flag']:
        sys.stdout.write('.')
        sys.stdout.flush()

        gevent.sleep(1)

        count += 1
        if count > 10:
            break
