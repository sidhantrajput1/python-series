"""
*********************************************************************
nums = [1,2,3,4,5,6,7,8,9]

for val in nums :
    print(val)

str = "apnacollege"
-------------------------------------------------------
for val in str :
    if(val == 'o') :
       print('o found')
       break  
    else :
        print('not found')
*********************************************************************

# ! range()  function

seq = range(10) 

for el in seq :
    print(el)
------------------------------------------------------
for val in range(10) :
    print(val)    

-----------------------------------------------
for el in range(1, 10) : # start and stop
    print(el)    
------------------------------------------------- 

for i in range(1 , 10, 3) :      # start #stop # step 
    print(i)

-------------------------------------------------------------    
*********************************************************************

*********************************************************************

*********************************************************************

*********************************************************************

*********************************************************************

*********************************************************************

*********************************************************************

*********************************************************************


"""

# n = int(input("Enter a number : "))
# for i in range(1, 11) :
#     print(n * i)

# n = 7
# sum = 0
# for i in range(1, n) :
#     sum += i
# print('total sum is : ',sum)    


n = 5 
fact = 1
for i in range(1 , n+1) :
    fact *= i
print('factorial is : ', fact)    