import time
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[..., Any]:
    def wrapper(funk: Callable) -> Callable:
        @wraps(funk)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                start_funk = time.time()
                result = funk(*args, **kwargs)
                end_funk = time.time()
                log_message = (
                    f"{funk.__name__} ok\n"
                    f"Время начала выполнения функции: {start_funk}\n"
                    f"Время окончания выполнения функции: {end_funk}\n"
                    f"Время выполнения: {end_funk - start_funk:.6f} сек.\n"
                    f"Результат: {result}\n"
                    f"\n"
                )
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                return result

            except Exception as e:
                error_message = (
                    f"{funk.__name__} error\n" f"Тип ошибки: {e}\n" f"Входные параметры: {args}, {kwargs}\n" f"\n"
                )
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(error_message)
                else:
                    print(error_message)
                raise

        return inner

    return wrapper


# if __name__ == "__main__":
#
#     @log("mylog.txt")
#     def my_function(x, y):
#         return x / y
#
#     my_function(2, "3")
# #
# # #
# # #     # with open('mylog.txt') as f:
# # #     #     line = f.readline()
# # #     #     print(line)
