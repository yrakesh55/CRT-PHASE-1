class F15:
    def light(self):
        print("ok switching on the lights")
    def fan(self,speed):
        print("Fan is on and the speed is", speed)
        self.s=speed
    def cpu(self):
        print("Powering on the system")
        print("The speed of the fan is", self.s)

kaushik=F15()
kaushik.light()
kaushik.fan(4)
kaushik.cpu()
