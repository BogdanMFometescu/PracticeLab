import functools

num_to_test = 7


# Decorator with arguments

def my_decorator_func(num):
    def my_deco(func):
        @functools.wraps(func)
        def funct_to_apply(*args, **kwargs):
            if num < 0:
                print("Cant add numbers")
            else:
                func(*args, **kwargs)

        return funct_to_apply

    return my_deco


@my_decorator_func(num_to_test)
def adding_func(x, y):
    print(x + y)


@my_decorator_func(num_to_test)
def multiply_func(x, y):
    print(x * y)


adding_func(6, 7)
multiply_func(6, 7)


# Simple decorator
def deco_one(func):
    @functools.wraps(func)
    def deco_func():
        print("xxx")
        func()
        print("yyy")

    return deco_func


def my_second_deco_with_args(num1):
    def deco_with_args(func):
        @functools.wraps(func)
        def deco_funct(*args, **kwargs):
            if num1 < 100:
                func(*args, **kwargs)
            else:
                print("xxxx")

        return deco_funct

    return deco_with_args


@my_second_deco_with_args(10)
def my_funct_with_args(x, y):
    print(x * y)


my_funct_with_args(100, 20)
