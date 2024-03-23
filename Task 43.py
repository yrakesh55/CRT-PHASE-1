class Shopping:
    def dresstype(self,type):
        print("The dress type is", type)
        self.t=type
    def price(self,pr):
        print("The price of the dress is", pr)
        self.p=pr
    def size(self,si):
        print("The size of the dress is", si)
        self.s=si
        print("The speed of the fan is", self.s)
    def display(self):
        print("The details of the customer is")
        print("The dress type is", self.t)
        print("The price is", self.p)
        print("The size is", self.s)

Rakesh=Shopping()
Rakesh.dresstype("Casual")
Rakesh.price(5000)
Rakesh.size("XL")
Rakesh.display()
