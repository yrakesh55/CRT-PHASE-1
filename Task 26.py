n=int(input("enter a value"))
b=0
c=n
while n>0:
    a=n%10
    b=b+a
    n=n//10
if c%b==0:
    print("Divisible")
else:
    print("Not divisible")
