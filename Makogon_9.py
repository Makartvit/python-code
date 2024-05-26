import datetime
import re


class Writer:
    def __init__(self, file_address):
        self.file_address = file_address

    def write(self, text):
        with open(self.file_address, 'a') as file:  # 'a' режим добавления
            file.write(text + '\n')


class Logger:
    def __init__(self, file_path):
        self.writer = Writer(file_path)
        self.error_count = 0

    def write(self, exception):
        self.error_count += 1
        error_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        error_class = exception.__class__.__name__
        error_message = str(exception)
        log_entry = f"{self.error_count}\t{error_time}\t{error_class}\t{error_message}"
        print(log_entry)  # Вывод для диагностики
        self.writer.write(log_entry)


def logger(log_instance):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                log_instance.write(e)
                raise

        return wrapper

    return decorator



log = Logger('log.txt')


@logger(log)
def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email address")
    return True


@logger(log)
def generate_candidates(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return [f"Candidate {i}" for i in range(n)]


@logger(log)
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b



try:
    validate_email("invalid-email")
except Exception as e:
    print(f"Caught an exception: {e}")

try:
    generate_candidates("five")
except Exception as e:
    print(f"Caught an exception: {e}")

try:
    divide(10, 0)
except Exception as e:
    print(f"Caught an exception: {e}")
