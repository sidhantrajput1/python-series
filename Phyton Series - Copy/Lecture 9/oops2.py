"""
class Student :

    def __init__ (self, name) :
        self.name = name

s1 = Student("Kartik")
print(s1.name)

del s1.name
print(s1.name) 


class Account :
    def __init__(self, acc_no, acc_pass) :
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # __ private symbol


acc1 = Account("123456789", "Sidhant@123")

print(acc1.acc_pass)
print(acc1.acc_no)


class Car :
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stoped")    

class ToyotaCar(Car):
    def __init__(self , name):
        self.name = name 

car1 = ToyotaCar("Fortunature")

print(car1.start())




class A :
    varA = "welcome A"
class B:
    varB = "Welcome B"

class C(A, B):
    varC = "Welcome C"

c1 = C()    
print(c1.varA)
print(c1.varB)
print(c1.varC)


"""

class Car :

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stoped")    

class ToyotaCar(Car):
    def __init__(self , name, type):
        super().__init__(type)
        super().start()
        self.name = name 

# car1 = ToyotaCar("Fortunature", "electric")
# print(car1.type)


class Student :
    def __init__(self, phy, math, chm) :
        self.phy = phy
        self.math = math
        self.chm = chm
        # self.percentage = str((self.phy + self.math + self.phy) / 3) + "%"

    @property
    def Percentage(self):
        return str((self.phy + self.math + self.phy) / 3) + "%"
    

# stu1 = Student(85, 96, 86)
# print(stu1.Percentage)


# stu1.phy = 95
# print(stu1.Percentage)
    

class Complex:
    def __init__ (self, real , img) :
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i+ ", self.img, "j")   


    def __add__(self, num2) :
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal , newImg)

num1 = Complex(5, 2)
num1.showNumber()
num2 = Complex(3, 4) 
num2.showNumber()

num3 = num1 + num2
num3.showNumber()