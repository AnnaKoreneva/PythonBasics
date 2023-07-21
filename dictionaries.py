"""
Dictionary:
- are type of data collection that stores data key - value pairs
- mutable(can be updated, added items, removed items)
"""
years = {"Anna": 1991, "Anton": 1994, "Mira": 2018, "Tanya": 1971, "Sergey": 1971}
# print(years.get("Anna"))
# print(years.items()) #get dictionary items
# print(years.keys())  #get items' key
# print(years.values())  #get items' values

print(years.popitem())  # Removes the item that was last inserted into the dictionary
print(years)

print(years.pop("Anna"))  #Removes the element with the specified key
print(years)

# print(years.setdefault("Oksana", 1974))  # Where do we use It?
# print(years)
#
# new_items = {"Anatol": 1968, "Anastasia": 1995}
# years.update(new_items)  # Add new items and update excisted
# print(years)
# new_items = {"Anatol": 1990, "Anastasia": 1996, "Anton": 1993}
# years.update(new_items)
# print(years)
