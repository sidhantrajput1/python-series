"""

class student :
    name = 'Sidhant',
    age = 29 ,
    college = 'Galgotias University'

    def __init__ (self, fullname, marks) :
        self.name = fullname
        self.marks = marks
        print('Adding new Student in Database -> ')

    def welcome(self) :
        print('Welcome...', self.name)    

s1 = student("Sidhant", 96)
# print(s1.name, s1.marks)
print(s1.college)    

s1.welcome()

"""


class Student :
    college = 'Galgotias College'
    def __init__ (self, name, marks) :
        self.name = name
        self.marks = marks
    def get_avg(self) :
        sum = 0
        for val in self.marks :
            sum += val 
        print('hy', self.name ,"Your avg Score is -> ", sum/3)

    @staticmethod
    def hello() :
        print("Hey Developer -> ")        

s1 = Student("Sidhant", [70,80,90])
# s1.get_avg()
# s1.hello()

class Car :
    def __init__(self) :
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started....")


car1 = Car()
# car1.start()

class Account :
    
    def __init__(self, bal, acc) :
        self.balance = bal
        self.account = acc
    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, "was credited")
        print("total balance = ", self.get_balance())
        
    
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 1234556)
acc1.debit(1000)
acc1.credit(2000)