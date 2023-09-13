# 국어, 영어, 수학, 점수의 평균 구하기
#

def get_average(kor,eng,math):
    return (kor+eng+math)/3

scores1 = {"kor" : 100,"eng" : 40 ,"math":20}
scores2 = {"s" : 100,"t" : 100 ,"d":20}




print(get_average(**scores1))


def get_average(**scores):
    total = 0
    for sub,score in scores.items():
        total+=score


    return total/ len(scores)

print(get_average(**scores1,**scores2))



def get_average(*scores):
    total = 0
    for score in scores:
        total+=score


    return total/ len(scores)

print(get_average(**scores1))