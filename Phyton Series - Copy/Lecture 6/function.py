# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.
# In Python a function is defined using the def keyword:


def cal_sum1 (a, b) :
    sum = a + b
    print(sum)
    return sum 

# cal_sum1(5, 10)


def cal_sum2 (a, b):
    return a + b
sum2 = cal_sum2(5, 6)
# print(sum2)


def avg_sum(a, b, c) :
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

# avg_sum(3, 4, 5)

num = [1,2,3,4,5,6,7,8,8,9] 

def cal_len (list) :
    print(len(list))

# cal_len(num)    


def cal_fact (n) :
    fact = 1
    for i in range(1 , n+1) :
        fact *= i
    print(fact)

# cal_fact(6 ) 


# ! recrsion 

def show(n) :
    if(n == 0):
        return
    show(n-1)
    print(n) 
                       
show(5)