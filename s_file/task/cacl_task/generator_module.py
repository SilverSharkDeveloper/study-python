def get_log_generator(file):
    while True:
        yield file.readline()


def get_line(file):
    return file.readline()