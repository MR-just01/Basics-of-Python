def my_decorator(func):
    def wrapper():
        print("before the function")
        func()
        print("after the function")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()


def great_decorator(func):
    def wrapper(name):
        print("welcome")
        func(name)
        print("have a great day!!")
    return wrapper

@great_decorator
def greet (name):
    print(f"hello , {name}!!")

greet("nammmu")


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"function ' {func.__name__}' called with arguement{args}" )
        result = func(*args , **kwargs)
        print(f"function '{func.__name__}' returned {result}")
        return result

    @log_decorator
    def add(a,b):
        return a+b 
    
    add(3,5)