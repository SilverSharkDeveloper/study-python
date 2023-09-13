# 두 정수의 연산을 수행하는 계산기 모듈 제작
# 연산 수행 시 해당 시간을 기록하고,
# 연산 수행 중 오류 발생 시 오류 사항과 시간을 기록하도록 한다.

# 입력 예
# 두 정수를 입력하세요.
# 연산자를 선택하세요

# 출력 예
# 1 + 3 = 4
# 10 / 0 = ZeroDivisionError


from calc_module import *
from log_module import *
from generator_module import *



# @calc.log_time
# def oper_file(reslut_string:str):
#     file = open("calc_log.txt", "a", encoding="utf-8")
#     file.write(reslut_string + "\n")
#     file.close()




while True:
    choice = int(input("1.두정수 연산\n2.로그출력"))
    if choice ==2:
        file = open("calc_log.txt", "r", encoding="utf-8")
        log_generator = get_log_generator(file)
        while True :
            log = next(log_generator)
            # log = get_line(file)
            if log:
                print(log,end="")
            else:
                file.close()
                break
    elif choice==1 :
        try:
            n1, n2,oper = input("두 정수와 연산자 [+ - * /]중 한개를 선택해 공백으로 구분지어 적어주세요").split(" ")
            calc_object = Calc.create_perfect_statement(n1,n2,oper)
            #이부분 클로저
            result_string = calc_object.get_result_string()
            Log.oper_file(result_string)
            print(result_string)
        except ZeroDivisionError as e:
            Log.error_file(str(e))
            print(e)
        except OperCheckException as e:
            error_message = OperCheckException.oper_error(oper)
            Log.error_file(error_message)
            print(error_message)
        except ValueError as e:
            Log.error_file(str(e))
            print(e)
    else:
        print("다시입력")

