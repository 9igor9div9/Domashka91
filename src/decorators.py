import time
from functools import wraps
from typing import Optional


def log(filename: Optional[str] = None):
    def wrapper(funk):
        @wraps(funk)
        def inner(*args, **kwargs):
            try:
                start_funk = time.time()
                result = funk(*args, **kwargs)
                end_funk = time.time()
                log_message = (f"Функция: {funk.__name__}\n"
                               f"Время начала выполнения функции: {start_funk}\n"
                               f"Время окончания выполнения функции: {end_funk}\n"
                               f"Время выполнения: {end_funk - start_funk}\n"
                               f"Результат: {result}\n"
                               f"\n")
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                return result

            except Exception as e:
                error_message = (f"Функция: {funk.__name__}\n"
                                 f"Тип ошибки: {e}\n"
                                 f"Входные параметры: {args}, {kwargs}\n"
                                 f"\n")
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(error_message)
                else:
                    print(error_message)
                raise

        return inner

    return wrapper


if __name__ == "__main__":
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x / y


    my_function(2, 1)
