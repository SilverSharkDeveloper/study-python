# closure check에서 key값과 value 값을 받아 set_target() 사용되어 결과값을 반환
# set_target 안에서 Bank.banks에 있는 내용을 bank에 넣고 bank에 있는 내용을 user에 넣는다.
# Bank.banks가 리스트 안에 리스트가 있는 2중 리스트이기 때문이다.
# user dictionary의 해당 키값이 value값과 같으면 user dictionary를 리턴
def check(*, key, value):
    def set_target():
        for bank in Bank.banks:
            for user in bank:
                if user.__getitem__(key) == value:
                    return user
        return None

    return set_target

# 배열 초기 선언, 은행 갯수 3개이므로 배열[] 안에 빈 배열[]3개 생성 -> [[],[],[]]
class Bank:
    total_count = 3
    banks = [[] for i in range(total_count)]
# 객체 초기화 (ex) owner: 자료형은 해당하는 매개변수의 자료형 선언
    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money
        self.object = self

# 클래스 메소드는 스태틱을 변환하기 위함, cls는 class명을 말하는것이나, cls로 선언시 객체가 따로 생성됨
    # open_account의 매개변수 자료형 강제 선언
    @classmethod
    def open_account(cls, owner: str, account_number: str, phone: str, password: str, money: int, bank_choice: int):
        # 선언 bank = [ShinHan, KookMin, KaKao][bank_choice -1]
        # -> if bank_choice 1일때 bank = list[0] : ShinHan
        # -> if bank_choice 2일때 bank = list[1] : KookMin
        # -> if bank_choice 3일때 bank = list[2] : KaKao
        bank = [
            ShinHan, KookMin, KaKao
            # ShinHan(owner, account_number, phone, password, money),
            # KookMin(owner, account_number, phone, password, money),
            # KaKao(owner, account_number, phone, password, money)
        ][bank_choice - 1]
        # 사용 (bank(owner, ...))
        # Bank(cls).banks[bank_choice - 1].append(bank(매개변수)).__dict__
        # static에 선언된 [[],[],[]]/ 몇번 방위치에다가 / bank를 dict형변환 후 해당 방 위치에 append
        # ex) bank_choice = 3이면 [[],[],[{owner : value, account_number : value, phone : value, password : value, money : value}]
        cls.banks[bank_choice - 1].append(bank(owner, account_number, phone, password, money).__dict__)
        return bank # bank_choice에 따라 신한, 국민, 카카오 중 하나를 반환
#
    @staticmethod #
    def check_account_number(account_number: str) -> dict:
        return check(key='account_number', value=account_number)()

    @staticmethod
    def check_phone(phone: str) -> dict:
        return check(key='phone', value=phone)()
# money만큼 입금
    def deposit(self, money: int):
        self.money += money
# money만큼 출금
    def withdraw(self, money: int):
        self.money -= money
# 잔액 반환
    def show_balance(self) -> int:
        return self.money
# 출력
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'

# 자식클래스로 입금 매소드 super로 불러와서 2로 나눠진 money를 전달
class ShinHan(Bank):
    def deposit(self, money: int):
        money /= 2
        super().deposit(돈)

# 자식클래스로 출금 매소드 super로 불러와서 1.5배 된 money를 전달
class KookMin(Bank):
    def withdraw(self, money: int):
        money *= 1.5
        super().withdraw(int(돈))


# 자식클래스로 조회 매소드를 super로 불러와서 조회 함수 사용 시 money가 2로 나눠지도록 함
class KaKao(Bank):
    def show_balance(self) -> int:
        self.money /= 2
        return super().show_balance()

# main에서 입력된것을 아래 변수에 저장
if __name__ == '__main__':

    bank_menu = "1. 신한 은행\n" \
                "2. 카카오 뱅크\n" \
                "3. 국민 은행\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True: #bank_choice에 입력한 번호를 저장, 4번일때 반복문 종료
        bank_choice = int(input(bank_menu))
        if bank_choice == 4:
            break

        while True: # menu_choice에 입력한 번호 저장, 5번일때 반복문 탈출하여 상위의 반복문으로 돌아감
            menu_choice = int(input(menu))
            if menu_choice == 5:
                break

            # 개설
            # menu_choice 1일때 owner에 예금주 이름 저장
            if menu_choice == 1:
                owner = input(owner_message)

                while True: # account_number에 계좌번호 입력
                    account_number = input(account_number_message)
                    # 위에서 입력한 계좌번호가 이미 있다면, Bank.check_account_number가 dictionary 타입으로
                    # 저장되어있어서 false를 반환 후 while문 안을 무한루프함,
                    # 계좌번호가 없다면 None이기 때문에 break
                    print(type(Bank.check_account_number(account_number)))
                    if Bank.check_account_number(account_number) is None:
                        break

                while True: # 입력된 전화번호를 phone에 저장, 저장되어 있는 phone이 없다면 break
                    phone = input(phone_message)
                    if Bank.check_phone(콜) is None:
                        break

                while True:# 입력된 패스워드 길이가 4가 아니라면 무한루프, 4면 break
                    password = input(password_message)
                    if password.__len__() == 4:
                        break

                # 예치금 입력, 저장
                money = int(input(money_message))

                # 왜 선언하는지 모르겠음
                user = None

                # 아래의 분기별 은행 분석을 한 줄로 변경!
                # [[],[],[]]의 방에 bank_choice에 따라 위치를 정하고 입력한 변수들을 저장
                # ex) bank_choice = 1
                #   [['임웅빈', '123-123-123456', '010-2923-7309', '1234', 10000, 1],[],[]]
                # 그러나 위로 가면 open_account에서 해당 변수들을 받아 dictionary로 변환 후 list에 append하기 때문에
                # 실제로는 user = [[{k:v,k:v,k:v,...}],[],[]]
                user = Bank.open_account(owner, account_number, phone, password, money, bank_choice)
                # # 신한 은행
                # if bank_choice == 1:
                #     user = ShinHan.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # # 카카오 뱅크
                # elif bank_choice == 2:
                #     user = KaKao.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # # 국민 은행
                # elif bank_choice == 3:
                #     user = KookMin.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # print(user, Bank.banks, sep="\n")

            # 입금
            elif menu_choice == 2:
                # 입금은 개설한 은행에서만 가능
                # 입력한 계좌번호는 account_number에 저장
                account_number = input(account_number_message)
                # user 부분 계좌번호가 없으면 None 있으면 check closure의 return user
                user = Bank.check_account_number(account_number)
                # 계좌번호가 있다면, 해당 배열 dictionary의 value가 입력값이랑 동일한지 검사 후
                # 동일하면 입금액을 입금 변수에 저장 후 user dictionary object키의 value값 (아마도 Bank)
                # 위가 맞다면 Bank.deposit(입금액) 이기 때문에 입금 매소드 실행
                if user is not None:
                    if user.__getitem__("password") == input(password_message):
                        deposit_money = int(input(deposit_message))
                        # 객체를 가져와서 deposite()실행
                        # user는 check에서 bank = [ShinHan,KookMin,KaKao] 중에서도 하나를 for user in bank로
                        # 저장하기때문에, bank.self.deposit(deposit_money) 호출
                        user.__getitem__("object").deposit(deposit_money)
                else: # 개설된 계좌가 없으면 입금이 안되기 때문에 에러메시지 출력
                    print(error_message)
            # 출금 , 입금과 흐름이 같음
            elif menu_choice == 3:
                # 계좌 존재 유무 검사
                account_number = input(account_number_message)
                # user 부분 계좌번호가 없으면 None 있으면 check closure의 return user
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user.__getitem__("password") == input(password_message):
                        # user는 check에서 bank = [ShinHan,KookMin,KaKao] 중에서도 하나를 for user in bank로
                        # 저장하기때문에, bank.self.withdraw(deposit_money) 호출
                        withdraw_money = int(input(withdraw_message))
                        if user.__getitem__("object").money >= withdraw_money:
                            user.__getitem__("object").withdraw(withdraw_money)
                        else:
                            print("대출을 진행할까요?")
                else:
                    print(error_message)
            # 잔액
            elif menu_choice == 4:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user.__getitem__("password") == input(password_message):
                        # user는 check에서 bank = [ShinHan,KookMin,KaKao] 중에서도 하나를 for user in bank로
                        # 저장하기때문에, bank.self.show_balance() 호출
                        print(f'현재 잔액: {user.__getitem__("object").show_balance()}')

                else:
                    print(error_message)