




def check(*, key, value):
    def set_target():
        for bank in Bank.banks:
            for user in bank:
                if user.__getitem__(key) == value:
                    return user
        return None

    return set_target


class Bank:
    account_phone_number = {}

    def __init__(self, name: str, account: str, phone_number: str, password: str, balance: int = 0):
        self.name = name
        self.account = account
        self.phone_number = phone_number
        self.password = password
        self.balance = balance

    def __str__(self):
        return f"예금주 : {self.name} 계좌번호  :{self.account} 핸드폰번호 : {self.phone_number} 비밀번호  : {self.password} 잔액 : {self.balance}"

    @classmethod
    def make_account(cls, name: str, account: str, phone_number: str, password: str, balance: int = 0):
        for ac in cls.account_phone_number.keys():
            if ac == account:
                print(f"{account}는 {cls.__name__}에 이미 존재하는 계좌입니다.")
                return None

        for pn in cls.account_phone_number.values():
            if pn == phone_number:
                print(f"{phone_number}는 {cls.__name__}에 이미 존재하는  핸드폰번호입니다.")
                return None

        cls.account_phone_number[account] = phone_number

        print("계좌 개설 성공")
        print(cls.account_phone_number)
        return cls(name, account, phone_number, password, balance)

    def deposit(self, money: int):
        self.balance += money
        print(f"입금 성공 현재 잔액 : {self.balance}")

    def withdraw(self, money: int):
        if self.balance < money:
            print(f"잔액이 부족합니다. 현재잔액:{self.balance}")
            return

        self.balance -= money
        print(f"출금 성공 현재 잔액 :{self.balance}")

    def check_balance(self):
        print(f"현재{self.name}님의 계좌 {self.account}에는 {self.balance}원의 잔액이 있습니다.")


class SinhanBank(Bank):
    account_phone_number = {}


    def __str__(self):
        return f"{self.__class__.__name__} {super().__str__()}"

    def deposit(self, money: int):
        self.balance += round(money / 2)
        print(f"입금 성공 현재 잔액 : {self.balance} , 수수료 : {round(money / 2)}")


class KookminBank(Bank):
    account_phone_number = {}

    def __str__(self):
        return f"{self.__class__.__name__} {super().__str__()}"

    def withdraw(self, money: int):
        if self.balance < round(money * 1.5):
            print(f"잔액이 부족합니다. 현재잔액:{self.balance}, 필요금액 : {round(money * 1.5)}")
            return

        self.balance -= round(money * 1.5)
        print(f"출금 성공 현재 잔액 :{self.balance}")


class KakaoBank(Bank):
    account_phone_number = {}

    def __str__(self):
        return f"{self.__class__.__name__} {super().__str__()}"

    def check_balance(self):
        if self.balance == 0:
            print(f"현재 잔액은 0원입니다.")

            return

        self.balance = round(self.balance * 0.5)
        print(f"현재 잔액은 {self.balance}")


banks = {"sinhan": [], "kookmin": [], "kakao": []}

while True:
    choice = int(input("1.신한 \n2.국민 \n3.카카오\n4.전체 은행 조회"
                       ""))

    if choice == 1:
        choice = int(input("1.계좌 개설\n2.입금\n3.출금\n4.잔액조회"))

        if choice == 1:
            infos = input("예금주,계좌번호,핸드폰번호,비밀번호 차례대로 입력 :").split(" ")
            new_account = SinhanBank.make_account(*infos)
            if new_account is None:
                continue
            banks["sinhan"].append(new_account)


        elif choice == 2:
            flag = False
            account = input("계좌번호 입력")
            for bank in banks["sinhan"]:
                if bank.account == account:
                    flag = True
                    password = input("비밀번호 입력")
                    if password == bank.password:
                        money = int(input("넣으실 금액 : "))
                        bank.deposit(money)

                        break
                    else:
                        print(f"비번이 틀립니다.")
                        break
            if not flag:
                print("계좌번호가 존재하지 않습니다.")

        elif choice == 3:
            flag = False
            account = input("계좌번호 입력")
            for bank in banks["sinhan"]:
                if bank.account == account:
                    flag = True
                    password = input("비밀번호 입력")
                    if password == bank.password:
                        money = int(input("출금할 금액 : "))
                        bank.withdraw(money)

                        break
                    else:
                        print(f"비번이 틀립니다.")
                        break
            if not flag:
                print("계좌번호가 존재하지 않습니다.")

        elif choice == 4:
            flag = False
            account = input("계좌번호 입력")
            for bank in banks["sinhan"]:
                if bank.account == account:
                    flag = True
                    password = input("비밀번호 입력")
                    if password == bank.password:

                        bank.check_balance()

                        break
                    else:
                        print(f"비번이 틀립니다.")
                        break
            if not flag:
                print("계좌번호가 존재하지 않습니다.")


    elif choice == 2:
        choice = int(input("1.계좌 개설\n2.입금\n3.출금\n4.잔액조회"))

        if choice == 1:
            infos = input("예금주,계좌번호,핸드폰번호,비밀번호 차례대로 입력 :").split(" ")
            new_account = KookminBank.make_account(*infos)
            if new_account is None:
                continue
            banks["kookmin"].append(new_account)


        elif choice == 2:
            flag = False
            account = input("계좌번호 입력")
            for bank in banks["kookmin"]:
                if bank.account == account:
                    flag = True
                    password = input("비밀번호 입력")
                    if password == bank.password:
                        money = int(input("넣으실 금액 : "))
                        bank.deposit(money)

                        break
                    else:
                        print(f"비번이 틀립니다.")
                        break
            if not flag:
                print("계좌번호가 존재하지 않습니다.")

        elif choice == 3:
            flag = False
            account = input("계좌번호 입력")
            for bank in banks["kookmin"]:
                if bank.account == account:
                    flag = True
                    password = input("비밀번호 입력")
                    if password == bank.password:
                        money = int(input("출금할 금액 : "))
                        bank.withdraw(money)

                        break
                    else:
                        print(f"비번이 틀립니다.")
                        break
            if not flag:
                print("계좌번호가 존재하지 않습니다.")

        elif choice == 4:
            flag = False
            account = input("계좌번호 입력")
            for bank in banks["kookmin"]:
                if bank.account == account:
                    flag = True
                    password = input("비밀번호 입력")
                    if password == bank.password:

                        bank.check_balance()

                        break
                    else:
                        print(f"비번이 틀립니다.")
                        break
            if not flag:
                print("계좌번호가 존재하지 않습니다.")

    elif choice == 3:
        choice = int(input("1.계좌 개설\n2.입금\n3.출금\n4.잔액조회"))

        if choice == 1:
            infos = input("예금주,계좌번호,핸드폰번호,비밀번호 차례대로 입력 :").split(" ")
            new_account = KakaoBank.make_account(*infos)
            if new_account is None:
                continue
            banks["kakao"].append(new_account)


    else:
        for banklist in banks:
            for bank in banks[banklist]:
                print(bank)
