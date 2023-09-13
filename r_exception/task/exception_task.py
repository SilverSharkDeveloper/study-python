#캐릭터 닉네임 정할 때 비속어를 사용하지 못허게 막아주기
#바보 멍게 해삼 운영자
#직접 Error을 제작하여 발생 시 안내 메세지까지 출력하기


class BadWordError(Exception):


    def printError(self,nickname):

        print(f"{nickname}은 비속어 입니다!")


def check_bad_word(nickname):
    bad_words = ["바보","해삼","말미잘","운영자","멍게"]
    for word in bad_words:
        if nickname.__contains__(word):
            raise BadWordError


nickname = input("캐릭터 닉네임을 정해주세요")


try:
    check_bad_word(nickname)
    print(f"{nickname}으로 닉네임을 정하겠습니다!")

except BadWordError as error:
    error.printError(nickname)




