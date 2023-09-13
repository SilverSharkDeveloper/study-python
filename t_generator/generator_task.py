import random

# 전달받은 명 수만큼 정보를 dict로 리턴한다.

# 리턴할 정보
# 번호, 이름, 전공

names = ['김보령', '김혜빈', '임수현', '이서호', '임웅빈', '장동혁']
majors = ['컴퓨터 공학', '전자 공학', '기계 공학', '의료 공학', '토목 공학']

# random.choice(list): list 요소 중 랜덤한 값 추출
# print(random.choice([1, 2, 3]))

def get_list(count: int = 0) -> list:
    count_list = []

    for person in range(count):
        count_list.append({random.choice(names):random.choice(majors)})

    return count_list


def get_generator(count: int = 0) -> dict:
    person_list = []
    for i in range(count):
        person_list.append({random.choice(names):random.choice(majors)})
        yield person_list[i]


def abc():
    yield "a"
    yield "b"
    yield "c"



abc = abc()
next(abc)
print(next(abc))


# n = int(input("몇명 드릴까여?"))
#
# generator_n = get_generator(n)
#
# # list_n = get_list(n)
#
# # for i  in range(n):
# #     print(list_n[i])
#
# #
# for i in range(n):
#   print(next(generator_n))

