# def decorator_file(func):
#     def inner(*args, **kwargs):
#         res = func(*args, **kwargs)
#         with open("something.txt", "a", encoding="utf=8") as f:
#             f.write(f"{res}\n")
#         return f"{res}"
#
#     return inner
#
#
# @decorator_file
# def greetings(name):
#     return f"Hello {name}"
#
#
# @decorator_file
# def upper(name, surname):
#     return f"{name} {surname}".upper()
#
#
# x = greetings("Oleh")
# print(x)
# y = upper("Oleh", "Olehovich")
# print(y)

# Task 1
def action():
    return "Action"


def decorator_before_after(func):
    def inner(*args, **kwargs):
        return f"{action()}\n{func(*args, **kwargs)}\n{action()}"

    return inner


@decorator_before_after
def greetings(name):
    return f"Hello {name}"


print(greetings("Named"))


# Task 2
def file_writer(file_name):
    def decorator(func):
        def inner(*args, **kwargs):
            y = func(*args, **kwargs)
            with open(file_name, 'a') as file:
                file.write(f'{y}\n')
            return y

        return inner

    return decorator


@file_writer("Rex.txt")
def hello_user(name):
    return f"Hello {name}"


hello_user("Yaroslav")


# Task 3
def handle_exceptions(func):
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            return f"ERROR: {error}"

    return handler


@handle_exceptions
def divide(a, b):
    return a / b


print(divide(5, 0))
print("ap")

# Task 4
import time
from timeit import timeit


def measure_time(func):
    def measurer(*args, **kwargs):
        return timeit(f"{func(*args, **kwargs)}")

    return measurer


@measure_time
def some_function():
    time.sleep(2)


print(some_function())

# Task 5

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def log_arguments_results(func):
    def log(*args, **kwargs):
        logger.info(f"Function name: {func.__name__}; arguments: {args, kwargs}; result: {func(*args, **kwargs)};")
        return func(*args, **kwargs)

    return log


@log_arguments_results
def add_numbers(a, b):
    return a + b


add_numbers(3, 4)


# Task 6

def limit_calls(calls_left: int):
    def decorator(func):
        def decorated_function(*args, **kwargs):
            nonlocal calls_left
            if calls_left > 0:
                calls_left -= 1
                return func(*args, **kwargs)
            else:
                print(f"{func.__name__} limit calls exceed")

        return decorated_function

    return decorator


@limit_calls(3)
def some_function():
    print("Виклик функції 1")


@limit_calls(5)
def some_function2():
    print("Виклик функції 2")


some_function()
some_function()
some_function()
some_function()
some_function2()
some_function2()
some_function2()
some_function()
some_function2()
some_function2()
some_function2()
some_function()


# Task 7

def cached(func):
    cache = dict()

    def decorated_function(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]

    return decorated_function


@cached
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))  # Обчислюється з використанням кешу
print(fibonacci(101))  # Обчислення за один крок
