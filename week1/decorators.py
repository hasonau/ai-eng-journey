
import time

########################################################## Task-1 #############################################
# def timer(func):
#     def wrapper():
#         before_run = time.perf_counter()
#         func()
#         after_run = time.perf_counter()  
#         print("Time taken:", after_run - before_run, "seconds")
#     return wrapper

# @timer
# def decorated_function():
#     time.sleep(3)

# decorated_function()

########################################################## Task-2 #############################################

def timer(func):
    def wrapper(*args,**kwargs):
        before_run = time.perf_counter()
        result = func(*args,**kwargs)
        after_run = time.perf_counter()  
        print("Time taken:", after_run - before_run, "seconds")
        return result
    return wrapper

@timer
def add(a,b):
    return a + b

print("Result = ",add(3,b = 8))