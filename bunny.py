n=153
n1=1
org=1
nod=0
while n>0:
    n=n//10
    nod=nod+1
sum1=0
while n1>0:
    digit=n%10
    sum1=sum1+digit**nod
    n1=n1//10
if sum1==org:
    print("yes")
else:
    print("no")
    