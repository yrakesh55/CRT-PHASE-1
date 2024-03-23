def prime():
    f=1
    n=int(input("enter a number"))
    for i in range(2,n):
        if n%i==0:
            f=0
            break
    if f==1:
        print("Prime number")
    else:
        print("Not Prime")
prime()