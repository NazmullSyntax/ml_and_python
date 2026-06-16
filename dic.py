# print("Hello, World!")
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# print(my_dict)
# print(my_dict["name"])
# my_dict["age"] = 31
# print(my_dict)
# my_dict["country"] = "USA"
# print(my_dict)
# del my_dict["city"]
# print(my_dict)
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
# if "name" in my_dict:
#     print("Name is in the dictionary.")
# else:
#     print("Name is not in the dictionary.")
# my_dict.clear()
# print(my_dict)
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# print(my_dict.get("name"))
# print(my_dict.get("age"))
# print(my_dict.get("country", "Country not found"))
# #pop
# my_dict.pop("age")
# print(my_dict)
# #remove
# my_dict.popitem()
# print(my_dict)
# set_dict = {"apple", "banana", "cherry"}
# print(set_dict)
# for item in set_dict:
#     print(item)
set_items = {"apple": 1, "banana": 2, "cherry": 3}
for key, value in set_items.items():
    print(f"{key}: {value}")
#nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(nested_dict)
print(nested_dict["person1"]["name"])
for key, value in nested_dict.items():
    print(f"{key}: {value}")
    
    


