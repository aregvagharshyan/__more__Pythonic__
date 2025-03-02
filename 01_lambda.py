lambda_ = '''A lambda function in Python is a small, anonymous function that can have any number of arguments but only one expression.
It’s often used for short, throwaway functions where defining a full function with def might feel cumbersome.
Lambda functions are useful when you need a simple function temporarily, typically used in functional programming constructs like map(), filter(), or sorted().'''
# Syntax is: lambda arguments: expression

# Lambda function that adds two numbers

add = lambda x, y: x + y
print(add(3, 5))

# Using with map and filter

numbers = [1, 2, 3, 4, 5]

squared = map(lambda x: x ** 2, numbers)
print(list(squared))

even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))

# Sorting by the second value in each tuple, with lambda
points = [(2, 3), (1, 2), (4, 1)]

points.sort(key=lambda x: x[1])
print(points)

