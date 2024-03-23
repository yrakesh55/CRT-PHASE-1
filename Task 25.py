a=int(input("enter the number"))
b=0
c=0
for i in range(1,a):
    if a%i==0:
        b=b+i
        c=c+1
print(b)
print(c)
if b>a:
    print("true")
else:
    print("false")
    