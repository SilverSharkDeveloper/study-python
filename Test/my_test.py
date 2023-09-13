# #3항 연산자
# import itertools
#
# print("cka" if "c" == "ㅇ" else "거짓")
#
#
# #list
# ar=[1,2,3,4,5]
#
#
#
# print(type(ar))
# print(type(ar[1]))
#
#
# ar[0] = 3
# print(ar)
#
#
#
# #tuple
#
# tuple = (1,2,3,4,5)
# print(type(tuple))
# print(type(tuple[0]))
# print(tuple)
#
#
# n,t = {1,2}
#
# print(n,t)


# 파이썬은 상수가 존재하지않음 -> tuple은 안에 주소값을 변경할 수 없는 불변 객체만 담음 -> tuple자체의 값은
# 바꿀 수 있지만 tuple이 가진 각각의 인덱스에 값은 변경할 수 없음


def decorator_function(original_function):
    def wrapper_function():
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function()

    return wrapper_function


@decorator_function
def display_1():
    print('display_1 함수가 실행됐습니다.')
    return "!"


print(display_1())


@decorator_function  # 1
def display_1():
    print('display_1 함수가 실행됐습니다.')


@decorator_function  # 2
def display_2():
    print('display_2 함수가 실행됐습니다.')



# display_1 = decorator_function(display_1)  # 3
# display_2 = decorator_function(display_2)  # 4


def out_fun(name):
    def in_fun():
        print(name)

    return in_fun


out_fun("허은상")()


def decor(funct):
    pass


@decor
def out(ar):
    return ar





