# Dictionary and Set
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# info = {
#     "Name" : "Sidhant",
#     "age" : 20,
#     "college" : "Galgotias",
#     'subjects' : ['C++', 'Java', 'Phyton'],
#     'topic' : ('Dicti', 'list')
# }
# print(info);
# print(type(info))
# print(info['subjects'])
# print(info['Name'])

# assign new value
# info['Name'] = 'Supriya'
# print(info)

# add new key value pairs
# info['sername'] = 'Rajput'
# print(info)


# create a null dictinoary
# null_dict = {}
# null_dict['Name'] = 'kartik'
# print(null_dict)

# Nested Dictionary
# student = {
#     "name" : "kartik",
#     "Subjects" : {
#         "phy" : 96,
#         "math" : 80,
#         "english" : 75
#     }
# }

# print(student)
# print(student["Subjects"])


# print(len(student))


# Dictionary Method

# print(student.keys())

# print(list(student.keys()))

# print(student.values())

# print(student.items())

# print(list(student.get('Subjects')))

# student.update({'city' : 'delhi'})
# college = {"C_name" : "Galgotia"}
# student.update(college)
# print(student)


# info = {
#     "table" : ['a piece of furniture' , 'list of facts'],
#     "cat" : "a small animal"
# }

# print(info["table"])

marks = {}

x = int(input('Enter phys marks : '))
marks.update({'phy' : x})

y = int(input('Enter math marks : '))
marks.update({'math' : y})

z = int(input('Enter chm marks : '))
marks.update({'chm' : z})

print(marks)