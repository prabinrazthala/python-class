# WAP to create a decorator function which calcuates the total time to execute the following function
from time import time
def execution_time(took_time):
    def inner_func(*args,**kwargs):
        t1 = time()
        result = took_time(*args,**kwargs)
        t2 = time()
        print(f'it takes {t2 - t1} seconds to complete the result')
        return result
    return inner_func

@execution_time
def func():
    for i in range(100000000):
       continue
    print("loop is completed")
func()


