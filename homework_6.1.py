from datetime import datetime as dt

def checktime(func):
    def wrapper():
        now = dt.now()
        print(f'Function was called at {now.hour} : {now.minute} : {now.second} {now.day} / {now.month} / {now.year}')
        func()
    return wrapper

@checktime
def hello_world():
    print("Hello world!")

hello_world()


