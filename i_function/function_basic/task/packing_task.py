#국어, 영어, 수학 점수를 전달받은 뒤 총 점수를 출력하는 함수
#list에 국어,영어,수학 점수를 각각 당ㅁ은 후 unpacking  발생시키기

def get_total(kor,eng,math):
    return kor+eng+math


scores=100,200,300

print(get_total(*scores))



def get_total(*scores):
    total = 0
    for score in scores:
        total+=score

    return total

scores=100,200,300

print(get_total(*scores))


#저장공간에 * -> packing
#값에 * -> unpacking


def check_A(*string) :
    count = 0
    for char in string:
        if char == "A":
            count+=1

    return count

print(check_A(*"ADTESDFEA"))

a,*b,c = 1,2,3,4

print(a,b,c)

print(*b)


a,b = 1,2



# keyword arguments
# def introduce(**info):
#     print(type(info))
#     print(info)
    # print(f'name: {info.get("name")}')
    # print(f'email: {info.get("email")}')

def introduce(name, email):
    print(f'name: {name}')
    print(f'email: {email}')

# dict를 그대로 보내면 TypeError 발생!
# introduce({"name": '한동석', "email": 'tedhan1204@gmail.com'})

# 직접 key=value를 작성하는 방법
# introduce(name='한동석', email='tedhan1204@gmail.com')

# packing을 발생시키는 방법
# introduce(**{"name": '한동석', "email": 'tedhan1204@gmail.com'})

# dict를 담은 후 packing 발생!
# info = {"name": '한동석', "email": 'tedhan1204@gmail.com'}
# introduce(**info)

# unpacking
info = {"name": '한동석', "email": 'tedhan1204@gmail.com'}
# key만 추출되어 전달
introduce(*info)
# value를 추출하기 위해서는 **info로 사용해야 한다.
introduce(**info)

introduce(name='한동석', email='tedhan1204@gmail.com')