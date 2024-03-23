for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()


for i in range(1,5):
    for s in range(1,6-i):
        print(" ",end="")
    for j in range(1,8):
        if i==1 or i==4 or j==1 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()