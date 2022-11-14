from concurrent.futures import ThreadPoolExecutor
import time

def make_udon(kind):
    print("{}udon boil".format(kind))
    time.sleep(3)
    return kind + 'udon'

kinds = ['tanuki', 'kake', 'zaru', 'kitsune', 'tempura', 'niku']
executor = ThreadPoolExecutor(max_workers=3)
futures = []

for kind in kinds:
    print("{}udon order".format(kind))
    future = executor.submit(make_udon, kind)
    futures.append(future)

for future in futures:
    print("{} omatasesimasita".format(future.result()))

executor.shutdown

"""
from threading import Thread
import time

def func1():
    num = 0
    while True:
        num += 1
        if num > 100_000:
            break
    print(num)

def func2(data):
    num = 0
    while True:
        num += data
        if num > 100_000:
            break
    print(num)

if __name__ == '__main__':
    data = 20
    thread_1 = Thread(target=func1)
    thread_2 = Thread(target=func2)

    thread_1.start()
    thread_2.start()
"""