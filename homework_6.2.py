from datetime import datetime as dt
from time import sleep


def check_before(func):
    def wrapper():
        now = dt.now()
        print(now.strftime(f'Function was called at %H : %M : %S  %d/%m/%Y'))
        func()

    return wrapper


def check_after(func):
    def wrapper():
        after = dt.now()
        print(after.strftime(f'Function was stopped at %H : %M : %S  %d/%m/%Y'))
        func()

    return wrapper


@check_before
def hello_world():
    print("Hello world!")
    sleep(1)


@check_after
def hello():
    pass


hello_world()
hello()


