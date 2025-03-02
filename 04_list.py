list_ = '''A list is a built-in data type in Python used to store multiple items in a single variable.
Lists are ordered, mutable, and allow duplicate values.'''
#*****#
Members = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
Numbers = [1, 2, 3, 4]
new_list = list()
new_list_2 = []
# methods
x = 'Alice'
i = 0
Members.append(x) #Adds x to the end of the list
Members.insert(i, x) #Inserts x at index i
Members.extend(Numbers) #Adds iterable
Members.remove(x) #Removes the first occurrence of x
Members.pop(i) #Removes and returns the element at i
Members.clear() #Removes all elements from the list
Members.index(x) #Returns the index of the first x
Members.sort() #Sorts the list in ascending order
Members.reverse() #Reverses the list in place
# indexing, slicing
print(Members[0], Members[-1], Members[3])
del Members[2:]
Members[0:2] = ['kyaj', 'qyachal'] #adds by slicing
# Merging
merged = Members + Numbers #Creates new list
