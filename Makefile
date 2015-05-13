all: busy.so

busy.so: busy.c
	$(CC) -o $@ -fPIC -shared -I/usr/include/python2.7 busy.c

clean:
	rm -f busy.so *.o

.PYONY: all clean
