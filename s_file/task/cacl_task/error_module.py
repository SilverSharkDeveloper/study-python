class OperCheckException(Exception):
    def __str__(self):
        return f"연산자 잘못 입력"

    @staticmethod
    def oper_error(oper):
        return f"연산자 {oper} 잘못 입력"