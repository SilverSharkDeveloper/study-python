class Car:
    wheel = 4


    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    @classmethod

    def change_wheel(cls):
        cls.wheel = 10

    # static 메소드와 class 메소드의 공통점
    # 클래스로 접근해서 사용한다.
    # static 필드를 수정할 수 있다.

    # static 메소드와 class 메소드의 차이점
    # static 메소드는 해당 클래스의 필드에 접근할 수 없다.
    # class 메소드는 cls를 사용하여 해당 클래스의 필드에 접근할 수 있다.
    # class 메소드는 cls를 사용하여 새로운 객체를 생성한 뒤 리턴할 수 있다.

    @classmethod
    def translate_to_eng(cls, brand, color, price):
        color = 'red'
        # 생성자 wrapping
        return cls(brand, color, price)


ferrari = Car.translate_to_eng('페라리', '빨간색', 70000)
lamborghini = Car('람보르기니', '노란색', 60000)

Car.change_wheel()

print(ferrari.wheel, lamborghini.wheel)
print(ferrari.color)



class A :
    pass


a = A()

print(a.__class__)
print(A)
print(A())
print(a)
print(A.__class__)
print(a.__class__.__class__.__class__.__name__)


print((1).__class__)
print(type(1))




