# Retrieve Student's Grade.

student_grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}
def students_grades_values(d, key):
    value = d.get(key, "Key not found.")
    return value
print(students_grades_values(student_grades, 'Alice'))

# Update Product Information.

product = {
    "name": "Laptop",
    "price": 1000,
    "stock": 50
}
def update_product(d, key, value):
    d.update({key: value})
    return d
print(update_product(product, 'stock', 75))

# Add an Item to a Category.

categories = {
    "fruits": ["apple", "banana"],
    "vegetables": ["carrot", "broccoli"]
}
def add_item(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        d.setdefault(key, value)
    return d
print(add_item(categories, 'fruits', 'orange'))

# Merge Two Dictionaries.

person = {
    "name": "John",
    "age": 30,
    "job": "Engineer"
}
contact = {
    "email": "john@example.com",
    "phone": "123-456-7890"
}
def merging(d_1, d_2):
    d_1.update(d_2)
    return d_1
print(merging(person, contact))

# Iterate Over a Dictionary.

products = {
    "Apple": 1.2,
    "Banana": 0.5,
    "Cherry": 3.0
}
def iterating(d):
    for key, value in d.items():
         print(f'{key}: {value}')
iterating(products)

# Pop and Clear Dictionary

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
popped_key = person.pop('age')
person.clear()

# List Keys, Values, and Items.

countries = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin"
}
countries_list = list(countries.keys())
capitals_list = list(countries.values())
list_of_tuples = list(countries.items())

# Modify Dictionary and Set Default.

products = {
    "Laptop": 1000,
    "Phone": 500,
    "Tablet": 300
}
products.popitem()
products.setdefault('Phone', 750)

# Create Dictionary with Default Values.

keys = ["name", "age", "job"]
new_dict = dict.fromkeys(keys)
print(new_dict)

# Update Personal Dictionary with Contact Information.

personal = {
    "name": "John",
    "age": 28
}

contact = {
    "email": "john@example.com",
    "phone": "123-456-7890"
}
personal.update(contact)