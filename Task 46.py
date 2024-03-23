#multilevel inheritance

class placements:
    def info(self):
        print("1062")
class dept(placements):
    def display(self):
        print("All depts")
class pragati(dept):
    def welcome(self):
        print("Welcome")

obj=pragati()
obj.welcome()
obj.display()
obj.info()
