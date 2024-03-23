
def login():

    n=1
    while n!=0:
        un=input("enter username")
        pwd=input("enter password")
        if un==pwd:
            print("Login successful")
            n=0
        else:
            print("Invalid enter again")
login()
