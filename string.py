str1=input("enter 1st string:")
str2=input("enter the 2nd string:")
print("select one of the following \n 1.concatenate \n 2.print \n 3.reverse \n 4.substring \n")
ch=int(input("enter your choice:"))
if(ch==1):
    concat=str1+str2
    print("concatenation=",concat)
elif(ch==2):
    print(str1)
    print(str2)
elif(ch==3):
    print(str1[::-1])
    print(str2[::-1])
elif(ch==4):
    print(str1[2:3])
    print(str2[1:2])    
    
    