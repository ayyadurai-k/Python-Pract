num1R = int(input("Enter 1st Complex Real Part : "))
num1I = int(input("Enter 1st Complex Imaginary Part : "))
num2R = int(input("Enter 2nd Complex Real Part : "))
num2I = int(input("Enter 2nd Complex Imaginary Part : "))

class Complex:
    def __init__(self):
        self.real = 0
        self.img = 0
    def set_values(self,real,img):
        self.real = real
        self.img = img
    def __add__(self,x):
        temp = Complex()
        temp.real = self.real + x.real
        temp.img = self.img + x.img
    def display1(self):
        print("First Complex  Number Is : ",self.real,"+",self.img,"i")
    def display2(self):
        print("Second Complex  Number Is : ",self.real,"+",self.img,"i")
    def display3(self):
        print("Third Complex  Number Is : ",self.real,"+",self.img,"i")

c1 = Complex()
c1.set_values(num1R,num1I)
c1.display1()
c2 = Complex()
c2.set_values(num2R,num2I)
c2.display2()
c3 = Complex()
c1.set_values(c1,c2)
c1.display3()




 