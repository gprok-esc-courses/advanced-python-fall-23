from time import ctime, sleep
import random


def counter(sid):
    for i in range(10):
        print("Session", sid, ":", i)
        sleep(random.randint(2, 5))


if __name__ == '__main__':
    print("Start at:", ctime())
    for session in range(5):
        counter(session)
    print("End at:", ctime())
