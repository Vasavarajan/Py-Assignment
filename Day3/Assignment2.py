x=int(input("enter the num"))
if x>1:
    for i in range(2,x):
        if x%i==0:
            print(x, "is not the prime number")
            break
    else:
        print(x,"is the prime number")
else:
    print(x, "is not the prime number")