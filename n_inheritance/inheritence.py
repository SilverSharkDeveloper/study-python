class TV:
    def __init__(self):
        self.power = False
        self.channel = 1
        self.volume = 1

    def display_info(self):
        print("전원: " + str(self.power))
        print("채널: " + str(self.channel))
        print("볼륨: " + str(self.volume))


tv = TV()

tv.power = True
tv.channel = 24
tv.volume = 14

tv.display_info()


class SmartTV(TV):
    def __init__(self):
        # 부모 생성자 호출
        super().__init__()
        self.ip ="192.168.1.1"

    def display_info(self):
        super().display_info()
        print("IP: " + self.ip)


smart_tv = SmartTV()

smart_tv.power = True
smart_tv.channel = 24
smart_tv.volume = 14

smart_tv.display_info()





class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("두 발로 걷기")


class Monkey(Human):
    def __init__(self, name, age, zoo):
        super().__init__(name, age)
        self.zoo = zoo

    # Overriding: 재정의
    # 부모의 메소드이름과 동일하게 자식에서 선언하면
    # 자식 객체에서는 자식에서 선언한 메소드로 실행된다.
    def walk(self):
        super().walk()
        print("네 발로 걷기")


kingkong = Monkey('멍순이', 10, '서울 어린이 대공원')
kingkong.walk()






