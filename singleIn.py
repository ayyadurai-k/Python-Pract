class Personal:
    def setData(self,emp_name,emp_id,bp):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.bp = bp
    def printData(self):
        print("Employee Name : ",self.emp_name)
        print("Employee Id : ",self.emp_id)
        print("Employee Basic Pay : ",self.bp)

class SalaryCalc(Personal):
    def calc(self):
        self.hra = 0.2* self.bp
        self.da = 0.5 * self.bp
        self.pf = 0.05*self.bp
        self.gp = self.hra + self.da + self.bp
        self.np = self.gp - self.pf
    def printCalc(self):
        print("HRA : ",self.hra)
        print("DA : ",self.da)
        print("PF : ",self.pf)
        print("Gross Salary  : ",self.gp)
        print("Net Salary  : ",self.np)

emp_name = input("Enter Employee Name : ")
emp_id = input("Enter Employee Id : ")
bp = int(input("Enter Employee Basic Pay  : "))
obj=SalaryCalc()
obj.setData(emp_name,emp_id,bp)
obj.calc()
obj.printData()
obj.printCalc()

