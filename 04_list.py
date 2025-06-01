list_ = '''A list is a built-in data type in Python used to store multiple items in a single variable.
Lists are ordered, mutable, and allow duplicate values.'''
#*****#
members = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
numbers = [1, 2, 3, 4]
new_list = list()
new_list_2 = []
# methods
x = 'Alice'
i = 0
members.append(x) #Adds x to the end of the list
members.insert(i, x) #Inserts x at index i
members.extend(numbers) #Adds iterable
members.remove(x) #Removes the first occurrence of x
members.pop(i) #Removes and returns the element at i
members.clear() #Removes all elements from the list
members.index(x) #Returns the index of the first x
members.sort() #Sorts the list in ascending order
members.reverse() #Reverses the list in place
# indexing, slicing
print(members[0], members[-1], members[3])
del members[2:]
members[0:2] = ['kyaj', 'qyachal'] #adds by slicing
# Merging
merged = members + numbers #Creates new list
