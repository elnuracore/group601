from time import sleep
import asyncio
from datetime import datetime as dt

def check_before_after(func):
    async def wrapper():
        start = dt.now()
        await func()
        end = dt.now()
        print(start.strftime("Function called at %Y - %m - %d   %H : %M : %S"))
        print(end.strftime("Function ended at %Y - %m - %d   %H : %M : %S"))
    return wrapper

@check_before_after
async def my_coroutine():
    print("Hello")
    await asyncio.sleep(3)

asyncio.run(my_coroutine())
