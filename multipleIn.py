class Product:
    def getData(self,pid,pname,quantity,amount):
        self.pid = pid
        self.pname = pname
        self.quantity = quantity
        self.amount = amount
    def calc(self):
        self.cost = self.quantity * self.amount
        print("Cost Of The Product without GST : ",self.cost)

class ProductGST:
    def getDataGST(self,pid,pname,quantity,amount):
        self.pid = pid
        self.pname = pname
        self.quantity = quantity
        self.amount = amount
    def calcGST(self,GST):
        self.GST = GST
        self.cost = self.quantity * self.amount
        self.GSTCost = self.cost + self.GST
        print("Cost Of The Product with GST : ",self.GSTCost)
        
class ProductTotal(Product,ProductGST):
    def printData(self):
        print("Product ID : ",self.pid)
        print("Product Name : ",self.pname)
        print("Product Quantity : ",self.quantity)
        print("Product Amount : ",self.amount)
        print("Product Without GST : ",self.cost)
        print("Product  GST  : ",self.GST)
        print("Product with GST  : ",self.GSTCost)
obj = ProductTotal()
pid = input("Enter Product Id : ")
pname = input("Enter Product Name : ")
quantity = int(input("Enter Product Quantity : "))
amount = int(input("Enter Product Amount : "))
obj.getData(pid,pname,quantity,amount)
obj.calc()
obj.getData(pid,pname,quantity,amount)
GST = int(input("Enter GST : "))
obj.calcGST(GST)
obj.printData()


    
    