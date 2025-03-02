# Accessing Dictionary Values

school = {
    "class_A": {"Alice": 90, "Bob": 85},
    "class_B": {"Charlie": 88, "David": 92}
}
print(school["class_A"]["Bob"])
print(school.get('class_A').get('Bob'))
school['class_B'].setdefault("Eve", 95)
school['class_B'].pop('Charlie')
print(school)

# Count Characters in a String.

def count_chars(text):
    result = {}
    for i in text:
        result[i] = result.get(i, 0) + 1
    print(result)
count_chars("hello")

# Merging Two Dictionaries and Summing Common Keys.

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 25, "c": 35, "d": 40}
sum_dict = {}
for key, value in dict1.items():
    for key1, value1 in dict2.items():
        if key == key1:
            sum_dict[key] = value + value1
for key, value in dict1.items():
    if key not in sum_dict:
        sum_dict[key] = value
for key, value in dict2.items():
    if key not in sum_dict:
        sum_dict[key] = value
print(sum_dict)

# Update Inventory.

def update_stock(inventory, item, quantity):
    for key, value in inventory.items():
        if item in inventory:
            inventory[item] = value + quantity
        else:
            inventory = inventory.setdefault(item, quantity)
        return inventory
store = {"apples": 10, "bananas": 5}
update_stock(store, "oranges", 3)
update_stock(store, "apples", 5)
print(store)

#  Sorting a Dictionary by Values

salaries = {"John": 50000, "Alice": 60000, "Bob": 45000}
sorted_result = dict(sorted(salaries.items(), key=lambda item: item[1], reverse=True))
print(sorted_result)
