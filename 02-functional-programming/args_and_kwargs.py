from functools import reduce


def use_args(*args):
    return reduce(lambda a, b: a + b, args)


def print_total(msg, *args):
    return msg + str(reduce(lambda a, b: a + b, args))


print(use_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(print_total("TOTAL:", 1, 2, 3, 4, 5))


def use_kwargs(**kwargs):
    if 'version' in kwargs and kwargs['version'] > 3:
        print("Program is OK")
    else:
        print("Program not supported, you need Python v 3.0 or newer")


use_kwargs(language="Python", version=3.10, framework="Flask")
use_kwargs(language="Python", version=2.8, framework="Flask")


def use_all(msg, msg2, *args, **kwargs):
    print(msg)
    print(msg2)
    print(args)
    print(kwargs)

use_all("A", "B", 1, 2, 3, 4, values=6, age=34, address="Street No.2")




