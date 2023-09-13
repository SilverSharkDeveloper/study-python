# 상속 실습

# 정사각형 (Square)
#   └─ 정육면체 (Cube)

#  1. '정사각형' 객체 정의
#  클래스 이름 : Square
#  생성자 : '한 면의 길이(side)'를 받아서 초기화
#  면적을 계산하여 리턴하는 메소드 : getArea()

# 2. '정육면체' 객체 정의 <-- Square 상속받아 정의
#  클래스 이름 : Cube
#  getArea() : 정육면체의 총 면적(겉넓이, 각 면적의 합)
#  getVolume() : 정육면체의 부피 계산


class Square:
    def __init__(self, side):
        self.side = side

    def getArea(self):
        return self.side * self.side


class Cube(Square):
    def __init__(self, byn, side):
        super().__init__(side)
        self.side = byn


    def getArea(self):
        return super().getArea()*6

    def getVolumn(self):
        return self.side**3



cube = Cube(5,6)

print(cube.getArea())
print(cube.getVolumn())


print("a",[Cube(1,2),Cube(1,2)])