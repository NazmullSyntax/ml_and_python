print("Hello, World!")
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
print(my_dict["name"])
my_dict["age"] = 31
print(my_dict)
my_dict["country"] = "USA"
print(my_dict)
del my_dict["city"]
print(my_dict)
for key, value in my_dict.items():
    print(f"{key}: {value}")
if "name" in my_dict:
    print("Name is in the dictionary.")
else:
    print("Name is not in the dictionary.")
my_dict.clear()
print(my_dict)
