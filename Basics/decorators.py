# main template
# wrappers exist to intercept the call.
# The receptionist can

# verify appointment
# collect payment
# update records

# without changing the doctor.

# The doctor still does the same job.

# That's the wrapper.
# Because the outer function runs only once (during decoration), 
# whereas the wrapper runs every time the function is called.

'''
Production code

Always write:

from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling")
        return func(*args, **kwargs)

    return wrapper

This is the version you'll see in most Python libraries and frameworks.


Imagine six months from now you're debugging.

Without @wraps:

@timer
@retry
@cache
def process_payment():
    ...

You get an error:

Error in wrapper

Which wrapper?

timer?
retry?
cache?

You don't know.

With @wraps:

Error in process_payment

Much more useful.
'''

# 1
def decorator_func(func):
    def wrapper(*args, **kwargs):
        ## add any instruction you wish to execute ##
        # func to run
        res = func(*args, **kwargs)
        # return the result of the function
        return res

    return wrapper

# 2
def greeter(func):
    # print('outisde func gets printed only once as Python loads it only once, so we use wrappers')
    def wrapper():
        print(f'Calling {func.__name__}')
        res = func()
        print(f'Finished {func.__name__}')
        return res
    return wrapper

@greeter
def greet():
    print("Hello")

# greet()
# greet()

# 3
def calculator(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Finished {func.__name__}')
        return res
    return wrapper

@calculator
def add(a, b):
    return a + b

# print(add(3, 5))

# 4
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'square took {end-start:.6f} sec')
        return res
    return wrapper

@timer
def square(n):
    return n * n

# print(square(5))

# 5
'''
@wraps is almost always used in production code
@wraps copies the metadata (name, docstring, annotations, etc.) from the original function 
to the wrapper so that the wrapper still "looks like" the original function.
'''
from functools import wraps
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(5)
def hello():
    print("Hi")

def login_required(logged_in):
    def decorator_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(logged_in)
            if not logged_in:
                # print('Access Denied')
                return 'Access Denied'
            res = func()
            return res
        
        return wrapper
    return decorator_func

logged_in = True
# logged_in = False
@login_required(logged_in)
def view_profile():
    # print("Profile")
    return "Show Profile"

# print(view_profile())

from functools import wraps

def logger(func):
    print("Decorator executed")

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapper executed")
        return func(*args, **kwargs)

    return wrapper

@logger
def hello():
    print("Hello")

print("Program started")

hello()
hello()