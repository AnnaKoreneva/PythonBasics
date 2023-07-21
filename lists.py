"""
List:
Collection of data
Mutable what means that items can be added, removed or changes
Can contain any types of data in a single list
Can contain any other types of collection(list, dictionaries and tuple) as a single item
Maintain order( element can be found by index)
"""

diff_types = [1, 1.2, "Anna", True, 123]
numerable_type = [12, 12.5, 0, -12, 10, 123.6, 12, 12]

print(diff_types)

diff_types.append("Test")  # add element to the list
print(diff_types)

diff_types.extend(numerable_type)  # extend the list with another list
print(diff_types)

print(diff_types.index(123))  # find the index of the element

numerable_type.sort(reverse=True)  # DESC order
print(numerable_type)

diff_types.pop(0)  # delete 0-index element; -1 will remove the last element of the list
print(diff_types)

diff_types.remove("Anna")  # delete element which match "Anna"
print(diff_types)

print("Test" in diff_types)  # Boolean operator to be sure that element with appropriate value in the list
print("Tests" in diff_types)

print(numerable_type.count(12))  # Return number of the elements which match with the search query

num_type = numerable_type.copy()
print(num_type)
