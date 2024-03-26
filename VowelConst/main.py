f=input("Enter The File Name : ")
with open(f) as file:
    text=file.read()
    v=0
    c=0
    for char in text:
        if char in "aeiouAEIOU":
            v+=1
        else :
            c+=1
    vp = (v*100) / len(text)
    cp = (c*100) / len(text)
    print(text)
    print("No.Of Vowels : ",v)
    print("No.Of Consonants : ",c)
    print("Precentage Of Vowels : ",vp,"%")
    print("Percentage Of Consonants : ",cp,"%")
    