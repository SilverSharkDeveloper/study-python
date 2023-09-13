
class Car :

    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
        self.boot = False


    def turn_on(self):
        if not self.boot :
            self.boot = True
        else:
            print("시동 이미 켜짐")



    def turn_off(self):
        if  self.boot:
            self.boot = False
        else:
            print("시동 이미 꺼짐")

