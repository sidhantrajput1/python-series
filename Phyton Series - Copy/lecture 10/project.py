import random
import string

# print(string.ascii_letters)
# print(string.ascii_uppercase)

# randNum = random.randint(1 , 10)
# print(randNum)
pas_len = 12
charValues = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.octdigits + string.punctuation + string.printable


password = ""
for i in range(pas_len) :
    password += random.choice(charValues)


print(password)