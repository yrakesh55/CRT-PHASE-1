#singlelevel inheritance

class F15:
    def light(self):
        print("ok switching on the lights")
    def fan(self,speed):
        print("Fan is on and the speed is", speed)
        self.s=speed
    def cpu(self):
        print("Powering on the system")
        print("The speed of the fan is", self.s)

#kaushik=F15()
#kaushik.light()
#kaushik.fan(4)
#kaushik.cpu()


class Shopping(F15):
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
Rakesh.fan(3)
Rakesh.light()
Rakesh.cpu()
