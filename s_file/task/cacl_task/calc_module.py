import datetime
from error_module import *


class Calc:
    def __init__(self,n1:int,n2:int,oper:str):
        self.n1 =n1
        self.n2 =n2
        self.oper = oper

    @classmethod
    def create_perfect_statement(cls,n1,n2,oper):
        if oper not in "+-*/":
            raise OperCheckException
        return Calc(int(n1),int(n2),oper)

    def add(self):
        return self.n1 + self.n2

    def sub(self):
        return self.n1 - self.n2

    def mul(self):
        return self.n1 * self.n2

    def div(self):
        return self.n1 / self.n2



    def oper_choice(self):
        return {
            "+": self.add,
            "-": self.sub,
            "/": self.div,
            "*": self.mul
        }

    def get_result_string(self):
        return f"{self.n1} {self.oper} {self.n2} = {self.oper_choice()[self.oper]()}"












