pname=input("Enter Person name : ")
age=int(input("Enter Age : "))
address = input("Enter Person Address : ")
mobile_no = int(input("Enter Mobile Number : "))

class Person:
    def getPerson(self):
        self.pname = pname
        self.age = age
        self.address = address
        self.mobile_no = mobile_no
    def printPerson(self):
        print("Person Name : ",self.pname)
        print("Age : ",self.age)
        print("Address : ",self.address)
        print("Mobile No : ",self.mobile_no)

fid = input("Enter Faculty Id : ")
fsalary = int(input("Enter Salary Of Faculty : "))

class Faculty(Person):
    def getFaculty(self):
        self.fid = fid
        self.fsalary = fsalary
    def printFaculty(self):
        print("Faculty Id : ",self.fid)
        print("Faculty Salary : ",self.fsalary)

bookname = input("Enter Bookname : ")
publisher = input("Enter Publisher Name : ")

class Publications(Faculty):
    def getBook(self):
        self.bookname = bookname
        self.publisher = publisher
    def printBook(self):
        print("Book Name : ",self.bookname)
        print("Publisher : ",self.publisher)

obj = Publications()
obj.getPerson()
obj.getFaculty()
obj.getBook()

obj.printPerson()
obj.printFaculty()
obj.printBook()

                                                               