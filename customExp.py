class Error(Exception):
    pass
class TooSmallError(Error):
    pass
class TooLargeError(Error):
    pass
num=10
while(1):
    try:
        ch=int(input("Enter A Number  : "))
        if ch<10:
            raise TooSmallError
        elif ch>10 :
            raise TooLargeError
        break
    except TooLargeError:
        print("Entered Too Large Number,Try Again")
    except TooSmallError:
        print("Entered Too Small Number,Try Again")
print("Entered Correct Number...!")