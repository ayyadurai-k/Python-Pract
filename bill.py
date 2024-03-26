pname=input("enter the product name:")
value=int(input("enter the price:"))
quantity=int(input("enter the qt:"))
discount=int(input("enter the discount:"))
tax=int(input("enter the tax amount:"))
discount=discount/100
tax=tax/100
value=value*quantity
discount=value*discount
tax=value*tax
totalamount=value-discount+tax
print("product name:",pname)
print("price:",value)
print("discount:",discount)
print("tax:",tax)
print("bill amount:",totalamount)