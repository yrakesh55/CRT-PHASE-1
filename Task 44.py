class Shopping:
    def __init__(self,place):
        print("Welcome to Shopping at", place)
    def dresstype(self,type):
        self.t=type
    def price(self,pr):
        self.p=pr
    def size(self,si):
        self.s=si
    def display(self):
        print("The details of the customer are")
        print("Dress type", self.t)
        print("Price", self.p)
        print("Size", self.s)

Rakesh=Shopping("Peter England")
Rakesh.dresstype("Casual")
Rakesh.price(5000)
Rakesh.size("XL")
Rakesh.display()
