import datetime


class Log :

    @staticmethod
    def log_time(original_function):
        def logging(*args):
            logging_time = datetime.datetime.now()
            print(logging_time)
            file = open("calc_log.txt", "a", encoding="utf-8")
            file.write(str(logging_time) + "\n")
            file.close()
            return original_function(*args)

        return logging

    @staticmethod
    @log_time
    def oper_file(reslut_string: str):
        file = open("calc_log.txt", "a", encoding="utf-8")
        file.write(reslut_string + "\n")
        file.close()

    @staticmethod
    @log_time
    def error_file(reslut_string: str):
        file = open("calc_log.txt", "a", encoding="utf-8")
        file.write(reslut_string + "\n")
        file.close()
