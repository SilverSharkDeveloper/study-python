#number 가 양수인지, 음수인지,0인지 검사

# number = int(input("숫자 입력 : "))
#
# if number >0 :
#     print(f"{number}는 양수입니다.")
# elif number ==0 :
#     print(f"{number}는 0입니다")
# else :
#     print(f"{number}는 음수입니다")
#


#나이 입력받기 ->미성년자인지 검사

age = int(input("나이를 입력하세여 : "));

condition_adult = age>19

if condition_adult :
    print("어른이시네요!")
else:
    print("나이 더먹고 오세여")


