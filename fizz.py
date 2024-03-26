for i in range(51):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
        
n=int(input("Enter the number:"))
sum=0
for num in range(1,n+1,1):
    sum=sum+num
print("sum of first",n,"num is:",sum)
avg=sum/n
print("The average of first",n,"number is:",avg)

class error(Exception):
    pass
class toosmallerror(error):
    pass
class toolargeerror(error):
    pass
num=10
while(1):
    try:
        ch=int(input("Enter a number: "))
        if ch<10:
            raise toosmallerror
        elif ch>10:
            raise toolargeerror
        break
    except toosmallerror:
        print("Enter too small...try again...")
    except toolargeerror:
        print("Enter too large...try again...")
print("Entered correct Number...!")

f=input("Enter the file name:")
with open(f) as file:
    text=file.read()
    v=0
    c=0
    for char in text:
        if char in "aeiouAEIOU":
            v+=1
        else:
            c+=1
    vp=((v*100)//len(text))
    cp=((c*100)//len(text))
    print(text)
    print("number of vowels:",v)
    print("number of consonants:",c)
    print("Percentage of vowels:",vp,"%")
    print("percentaeg of consonants:",cp,"%")
    
file=open("Sample.txt","rb")
print("position of file pointer before reading is:",file.tell())
print(file.read(10))
print("setting 4 bytes form the current position of file pointer:")
file.seek(4,1)
print(file.read())
file.close()