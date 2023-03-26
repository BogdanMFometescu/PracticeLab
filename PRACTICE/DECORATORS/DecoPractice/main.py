import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator")
        func()
        print("After the decorator")

    return function_that_runs_func


@my_decorator
def my_function():
    print("I am the function")


# my_function()


def decorator_with_arguments(num):
    def my_deco(func):
        @functools.wraps(func)
        def function_with_arguments(*args, **kwargs):
            if num == 56:
                print("In the decorator")
            else:
                func(*args, **kwargs)
            print("After the decorator")

        return function_with_arguments

    return my_deco


@decorator_with_arguments(57)
def my_function_two(x, y):
    print(x+y)


my_function_two(4,7)



