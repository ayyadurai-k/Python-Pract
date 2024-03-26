class People:
    def __init__(self,age,gender):
        self.age=age
        self.gender=gender

class Student(People):
    def __init__(self,name,regno,m1,m2,m3,age,gender):
        super().__init__(age, gender)
        self.name=name
        self.regno=regno
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def display(self):
        print("Name : ",self.name)
        print("RegNo : ",self.regno)
        tot=self.m1+self.m2+self.m3
        print("Total : ",tot)
        print("Average : ",tot/3)
        print("Age : ",self.age)
        print("Gender : ",self.gender)

n=int(input("Enter No.Of Students : "))
objs=[]
for i in range(n):
    print("User ",i+1," : ")
    name = input("Bun uh Thaa : ")
    regno = int(input("Enter RegNo : "))
    m1,m2,m3 = int(input("Enter Mark 1 : ")),int(input("Enter Mark 2 : ")),int(input("Enter Mark 3 : "))
    age=int(input("Enter Age : "))
    gender=input("Enter Gender : ")
    obj = Student(name, regno, m1, m2, m3,age,gender)
    objs.append(obj)
i=0 
for obj in objs:
    print("User ",i+1," :- ")
    i+=1
    obj.display()
        