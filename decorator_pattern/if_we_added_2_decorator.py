def add_two(func):
    def wrapper(*args, **kwargs):
        print("\nThe result of {0} function is:".format(
              func.__name__))
        return_value = func(*args, **kwargs)
        print(return_value)
        print("If we added two we would have {0}".format(
            return_value + 2))
        return return_value
    return wrapper


@add_two
def sum1(a, b, c):
    return a + b + c


@add_two
def sum2(a, b):
    return a + b


@add_two
def multiply1(a, b, c):
    return a * b * c


sum1(1, 2, 3)
sum2(4, b=50)
multiply1(2, -2, 4)
