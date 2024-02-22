# Set in phython

# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

name = {'supriya', 'sidhant', 'amit' , 20, 22, 19 , 22 , 20 , 19}
# in set duplicate value are not allowed , if you assign duplicate value . Then sets are ignore duplicate value
# print(name)
# print(type(name))
# print(len(name))


# create a empty set
stud = set()
# print(type(stud))

# Method *****************************************************************************************************************

# stud.add('kartik')
# stud.add('Amit')
# stud.add('Rahul')
# stud.add(' Bikash')
# print(list(stud))

# stud.remove('kartik')

# stud.clear()
# print(stud)

# collect = {"kartik", "Amit", "Rhoit", 1 , 2 , 3}
# print(collect.pop())


set1 = {1, 2 ,3 ,4 ,5}
set2 = {3, 4 , 5 ,6 , 8}

print(set1.union(set2))

print(set1.intersection(set2))