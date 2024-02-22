"""
Python tuples are a type of data structure that is very similar to lists. 
The main difference between the two is that tuples are immutable, 
meaning they cannot be changed once they are created.

("Suzuki", "Audi", "BMW"," Skoda ") is a tuple.  

"""

# tup = (2, 1, 3, 4)
# print(tup)
# print(tup[0])

# print(tup[0 : 2])

# mr = (1,)
# print(mr)
# print(type(mr))


# tup = (2, 1, 3, 4)
# print(tup.index(3))
# print(tup.count(2))


# movies = [];

# mov1 = input('Enter 1st movie name -> ')
# movies.append(mov1)
# mov2 = input('Enter 2nd movie name -> ')
# movies.append(mov2)
# mov3 = input('Enter 3rd movie name -> ')
# movies.append(mov3)
# print(movies)


list1 = [1, 2, 1]

new_list = list1.copy()
new_list.reverse()

if(new_list == list1) :
    print('Palindrome')
else:
    print('not Palindrome')    