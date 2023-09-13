# 문제 2: 학생 클래스
# 학생 클래스 이름(name), 학년(grade), 과목별 성적(scores)
# 주어진 과목명과 성적을 받아서, 해당 과목의 성적을 저장합니다.
# 이미 해당 과목의 성적이 있을 경우에는 성적을 업데이트합니다.
# get_average(): 학생의 전체 과목의 평균 성적을 계산하여 반환합니다

class Studnet:
    def __init__(self, name, grade, **scores):
        self.name = name
        self.grade = grade
        self.scores = scores

    def set_grade(self, subject, score):
        self.scores[subject] = score

    def get_average(self):
        total = 0
        for score in self.scores.values():
            total += score

        return total / len(self.scores)


s1 = Studnet("s1", "a", math=100)
s2 = Studnet("s2", "b", math=90,kor=50)

print(s1.scores)
print(s2.scores)

s1.set_grade("math",90)
s1.set_grade("kor",90)
s1.set_grade("eng",30)

print(s1.get_average())



#은행 -> 출금 입금,잔고확인
#처음 입금하면 두배
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance*2

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print(f"Not enough balance in account {self.account_number}.")

    def get_balance(self):
        print(f"Account {self.account_number} has a balance of {self.balance}")

# Create instances of BankAccount
account1 = BankAccount("123456", "heo")
account2 = BankAccount("789012", "kim", 1000)

account1.deposit(5000)
account1.withdraw(100000)
account1.get_balance()

account2.deposit(19999)

