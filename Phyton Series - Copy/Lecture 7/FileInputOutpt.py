#  file input output

# python can be used to perform  operation on file . (read and write opearation)

# types of files 1. text file (ex :- .txt, .doc, .log, etc), 2. Binary Files (ex :- .mp4, .mov, .png , .jpeg etc.)

# f = open("demo.doc", "r")
# data = f.read()
# print(data)
# print(type (data))
# f.close()

# f = open("demo.doc", "r")
# line = f.readline()
# print(line)
# f.close()

# f = open("demo.doc", "w")

# data = f.write('i want to learn js tomorrow . 123')
# print(data)

# f.close()

# f = open("demo.doc", "a")

# data = f.write(' i want to learn React.')
# print(data)

# f.close()

 # crete a new file
# f = open('sample.log', 'w')
# f.close()

# other way 

# with open('demo.doc', 'a') as f:
#     data = f.write(" You are future of world")
#     print(data)

 # for deleting a file
# import os 
# os.remove('sample.log')


# f = open('practise.doc', 'w')
# f.close()

# with open("practise.doc", 'r') as f:
#     data = f.read()


# new_data = data.replace("java", 'javascript')
# print(new_data)

# with open("practise.doc", 'w') as f:
#     f.write(new_data)

word = 'learning'
with open('practise.doc', 'r') as f :
    data = f.read()
    if(data.find(word) != -1) :
        print('find')
    else : 
        print('not found')    