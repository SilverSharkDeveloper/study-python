# 다른 경로에 있을 경우 루트 경로부터 시작하여 절대 경로를 작성해준다.
import datetime

from s_file.task.log.log import log_time


class Calc:
    def __init__(self, number):
        self.number = number

    def calc(self, other, oper, file, error_message=""):
        oper_number = {'+': 0, '-': 1, '*': 2, '/': 3}
        if oper:
            self.oper = oper
            return [self.__add__, self.__sub__, self.__mul__, self.__floordiv__][oper_number.get(oper)](other,
                                                                                                        **{'file': file,
                                                                                                           'error_message': error_message})

        file.write(error_message + "\t\t / " + str(datetime.datetime.now()) + "\n")
        return None

    @log_time
    def __add__(self, other, **kwargs):
        return self.number + other

    @log_time
    def __sub__(self, other, **kwargs):
        return self.number - other

    @log_time
    def __mul__(self, other, **kwargs):
        return self.number * other

    @log_time
    def __floordiv__(self, other, **kwargs):
        result = None
        try:
            result = self.number // other, self.number % other
        except ZeroDivisionError:
            pass

        return result
