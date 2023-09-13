
# Comprehension(컴프리헨션: 이해력)
# 반복되거나 특정 조건을 만족하는 리스트를 보다 쉽게 만들어 내기 위한 방법

# List Comprehension 구문
# [표현식 for 항목 in interator (if 조건)]


# iterator 값 담기 -> 조건검사 ->표현식 리스트에 추가 -> 반복 ->리스트 반환

a = [1, 2, 3, 4]
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# print(a * 3)

# result = []

# for num in a:
#     result.append(num * 3)
#
# print(result)

result = [num * 3 for num in a]
print(result)

# [1, 2, 3, 4]
a = [1, 2, 3, 4]
# [6, 12]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# [표현식 if 조건 else 표현식 for 항목 in interator (if 조건)]
# [1, 6, 3, 12]
a = [1, 2, 3, 4]
result = [num * 3 if num % 2 == 0 else num for num in a]
print(result)


a = [10, 20, 30, -20, -3, 50, -70]
# 위 리스트에서 '양수'만 추출하여 새로운 리스트 만들기
result = [
    number
    for number in a
    if number > 0
]

print(result)

# n개의 0으로만 채워진 list

# 제곱의 결과가 10보다 큰 결과만 담은 list
a = [1, -2, 3, -4, 5]


# a = [1,2,3,4]
#
# b= [num * 3 if num%2==0 else num for num in a ]
#
# print(b)





a = [1,2,3,4]

b= [num * 3 if num%2==0 else num for num in a ]

print(b)


a=[10,20,30,-20,-3,50,-70]

b=[pos for pos in a if pos>0]
print(b)


#n개의 0으로만 채워진 list

c= [0 for i in range(int(input("n :")))]
print(c)


#제곱의 결과가 10보다 큰 결과만 담은 list

a= [1,-2,3,-4,5]

d=[num**2 for num in a if num**2 >10]
print(d)





# 값 in 리스트 -> 있으면 true 없으면 false


#[리스트에 차례로 담을 값(변수명 활용) for 변수명 in iterable (if 조건식 -> true 일 때만 리스트에 값을 담음)]


#0~9까지 중 3의 배수만 list에 담고 출력

print([num for num in range(10) if num%3==0] )