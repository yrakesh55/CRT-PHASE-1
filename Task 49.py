class father:
  def bike(self):
   print("GT")
  def laptop(self):
   print("2Gb")
class bunny(father):
    def laptop(self):
      print("8Gb")
obj=bunny()
obj.bike()
obj.laptop()
