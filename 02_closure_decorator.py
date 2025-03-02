closure_ = '''A closure occurs when a function returns another function that retains access to the enclosing function's local variables,
even after the outer function has finished executing.'''
decorator_ = '''A decorator is a function that modifies or enhances another function's behavior without changing its actual code.'''

# Create a closure that returns a function that multiplies a number by a given factor.

def multiply_by(n):
    def my_func(y):
        return y * n
    return my_func

closure = multiply_by(2) #We also created closure
print(closure(10))

# Create a decorator that modifies the input of a function and prints the result.

def debug(func):
    def my_func_1(name):
        name = func(name)
        return name
    return my_func_1

@debug
def greet(name):
    return f'Hello, {name}!'
print(greet('Areg'))

# Create a closure that acts as a counter, incrementing on each call.

def counter():
    count = 0
    def my_func_2():
        nonlocal count
        count += 1
        return count
    return my_func_2

counter_func = counter()
print(counter_func())

# Create a decorator that accepts arguments and returns the result of a function.

def decorator(func):
    def my_func_3(*args):
        result = func(*args)
        return result
    return my_func_3

@decorator
def greet(name, age):
    return f"Hello {name}, you are {age} years old."
print(greet('Areg', 23))

# Create a decorator that validates inputs before executing a function.

def validate_input(func):
    def my_func_4(*args):
        result = func(*args)
        return result
    return my_func_4

def add(a, b):
    return a + b
output = validate_input(add)
print(output(1, 2))