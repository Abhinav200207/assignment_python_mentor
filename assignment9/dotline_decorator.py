def dotline_decorator(func):
    def wrapper(*args, **kwargs):
        print("." * 30)
        func(*args, **kwargs)
        print("." * 30)
    return wrapper

@dotline_decorator
def display_data(*args):
    for arg in args:
        print(arg)
