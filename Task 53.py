class Car:
    def __init__(self):
        self.cgst=18%self.p
        self.sgst=18%self.p
        self.insurance=30%self.p
    def company(self):
        while True:
            a=["Toyota","Mercedes","Mahindra"]
            self.c=input("Enter the car company")
            if self.c=="Toyota":
                print("Welcome to Toyota")
                self.model()
                break
            elif self.c=="Mercedes":
                print("Welcome to Mercedes")
                self.model()
                break
            elif self.c=="Mahindra":
                print("Welcome to Mahindra")
                self.model()
                break
            else:
                print("Please enter a valid car company")
    def model(self):
        if self.c=="Toyota":
            while True:
                print("")


Owner=Car()
Car.company()