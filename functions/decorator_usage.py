"""When to Use a Decorator in Python You'll use a decorator when you need
to change the behavior of a function without modifying the function itself.
A few good examples are when you want to add logging, test performance,
perform caching, verify permissions, and so on. """


from datetime import datetime

def main_decorator(decorated_func):
    def wrapper():
        start = datetime.now()
        decorated_func()
        end = datetime.now()
        print(f'The function has been executed in {end - start}seconds')
    return wrapper

def main_decorator_2(decorated_func):
    def wrapper():
        start = datetime.now()
        decorated_func()
        end = datetime.now()
        print(f'The function has been executed in {end - start}seconds AGAIN')
    return wrapper

@main_decorator_2
@main_decorator
def multiply():
    for i in range(1501):
        print(i**6)

multiply()