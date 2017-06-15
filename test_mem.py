import thread
import multiprocessing
import time
import os

mem = 4000
div = 100
(n, s) = divmod(mem, div)


def allocate_mem(x, name):
    a = ' ' * x * 1000 * 1024
    while True:
        time.sleep(60)


def eat_thread():
    thread.start_new_thread(allocate_mem, (s, 'thread-0'))
    print 'Start thread-0'
    for i in range(0, n):
        try:
            thread.start_new_thread(allocate_mem, (div, 'thread-' + str(i+1)))
            print 'Start thread-' + str(i+1)
        except :
            print 'Start thread-' + str(i + 1) + ' failed'
            break
    while True:
        time.sleep(60)


def eat_process():
    p1 = multiprocessing.Process(target=allocate_mem, args=(s, 'process-0'))
    print 'Start process-0'
    p1.start()
    for i in range(0, n):
        try:
            multiprocessing.Process(target=allocate_mem, args=(div, 'process-' + str(i+1))).start()
            print 'Start process-' + str(i + 1)
        except MemoryError:
            print 'Start process-' + str(i + 1) + ' failed'
            break
        time.sleep(1)
    while True:
        time.sleep(60)

if __name__ == "__main__":
    eat_process()
