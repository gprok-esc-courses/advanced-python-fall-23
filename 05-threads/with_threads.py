from time import ctime, sleep
import random
from threading import Thread


def counter(sid):
    for i in range(10):
        print("Session " + str(sid) + ": " + str(i))
        sleep(random.randint(2, 5))


if __name__ == '__main__':
    threads = []
    print("Start at:", ctime())
    for session in range(5):
        th = Thread(target=counter, args=(session,))
        threads.append(th)
        th.start()
    for th in threads:
        th.join()
    print("Stop at:", ctime())
    print("Completed")
