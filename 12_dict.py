dictionary = '''A dictionary in Python is a built-in, mutable, ordered (by key) data type used to store key-value pairs.
Each key in the dictionary is unique, and it maps to a specific value.'''
#*****#
my_dict = {"key1": "value1", "key2": "value2"}
new_dict = dict(key1="value1", key2="value2")#creates new dict
new_dict_2 = {}
# methods
my_dict.get("key1")# avoids value or KeyError if the key is missing
my_dict.get("key3", "Not Found")# avoids "Not Found" if the key missing
my_dict.setdefault("key4", "value4")#is for checking a key’s existence and adding it with a default value if it doesn’t exist
my_dict.update({"key3": "value3"})# This can be another dictionary or an iterable of key-value pairs (e.g., a list of tuples, or a list of lists)
my_dict.pop("key1")# pops with key
my_dict.popitem()# pops last item
my_dict.clear()# clears and returns None
copy_dict = my_dict.copy()# creates copy of dict
my_dict.keys()# returns keys
my_dict.values()# returns values
my_dict.items()# returns keys, values
# ordered by key.
my_dict["key3"] = "value3"#Adds or modifies key3
del my_dict['key3']# removes the key and value
# unpacking, as creating.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2} # unpacking, creates new dict
print(merged_dict)
# merging, as creating
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2 # |merge operator, creates new dict
print(merged_dict)

