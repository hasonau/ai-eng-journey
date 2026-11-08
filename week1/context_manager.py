import time
from contextlib import contextmanager

# Context manager examples

####################################################### Task 1 ###########################################################
class Person:
    def __init__(self,name : str):
        self.name = name
    def __enter__(self):
        print("In Enter")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("exc_type" , exc_type)
        print("exc" , exc)
        print("tb" ,tb)

        print("end")

with Person("Umair") as p:
    print("Work goes here,the actual work,right,not in enter,it just enters,and gives us the self")
    print(p.name)
    # raise ValueError("something wrong here")

print("----------------------------------------------------------")
####################################################### Task 2 ###########################################################

@contextmanager
def person(name):
    try:
        print("Entered Function")
        print("Name = " ,name)
        yield
    finally:
        print("End,the exit data is here")


with person("Umair") as p1:
    print("nothing we reciveing so no need of 'as p1'")

print("----------------------------------------------------------")
####################################################### Task 3 ###########################################################

@contextmanager
def timer(data):
    before_yield = time.perf_counter()
    try:
        yield
    finally:
        after_yield = time.perf_counter()
        print(f"{data} took {after_yield - before_yield:.2f} seconds")

with timer("LLM Api call took "):
    time.sleep(3)