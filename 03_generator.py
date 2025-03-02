generator_ = '''A generator in Python is a special type of iterator that is defined using a function with the yield keyword,
instead of returning a value with return. Generators allow you to iterate over a sequence of values, but they do so lazily,
meaning they produce values on demand and do not store the entire sequence in memory.'''
# Lazy Evaluation: Values are generated one at a time, which is memory-efficient, especially for large datasets.
# State Retention: A generator "remembers" the state between iterations, allowing it to resume execution where it left off.
# Iterable: Generators are iterables and can be used in loops like for, or with functions like next().
# We have 2 ways to create generators.
def count_up_to(max): # Generator function
    count = 1
    while count <= max:
        yield count # with yield keyword, it defines generator
        count += 1

gen = count_up_to(5)
for number in gen:
    print(number)

#or#

gen = (x * x for x in range(5)) # using generator expression
for number in gen:
    print(number)
print(type(gen)) # class generator

# And in the end. Generators are ideal for working with large datasets.