#multiple inheritance

class SubjMarks: 
    math=int(input("Enter paper marks of maths"))
    DE=int(input("Enter paper marks of DE"))
    c=int(input("Enter paper marks of c language"))
    english = int(input ("Enter paaper marks of english"))
class PractMarks:
    cpract=int (input ("Enter practicals marks of cpract"))
class Result(SubjMarks,PractMarks): 
    def total(self):
        if self.math>40 and self.DE>40 and self.c>40:
            print("pass")
        else:
            print("fail")

obj=Result()
obj.total()
