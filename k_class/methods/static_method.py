class Student:
    country = '대한민국'
    status = '쉬는 중'

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math
        # self.status = status

    # static 필드 수정 혹은 전체 객체에 동시에 반영할 기능을 작성할 수 있다.
    @staticmethod
    def study():
        Student.status = "공부 중"


student1 = Student(100, 15, 30)
student2 = Student(100, 15, 30)

print(student1.status)
print(student2.status)

Student.study()

print(student2.status)
print(student2.status)


