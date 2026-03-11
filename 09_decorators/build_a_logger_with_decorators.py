from functools import wraps


def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f" Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f" Finished {func.__name__}")
        return result
    return wrapper


@log_function_call
def brew_chai(type):
    print(f"Brewing {type} Chai")


brew_chai("Masala Chai")
