import json
import logging
import os

path_log_utils = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs", "utils.log"))
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
utils_handler = logging.FileHandler(path_log_utils, encoding="utf-8", mode="w")
utils_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
utils_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_handler)


def transactions_data(path_data: str) -> list[dict] | None:
    """Возвращает список словарей с данными о финансовых транзакциях из JSON-файла."""
    utils_logger.info("Начало работы функции")
    try:
        utils_logger.info("Открываем json файл")
        with open(path_data, "r", encoding="utf-8") as file:
            file1 = file.read()
        if len(file1) == 0:
            utils_logger.error("Ошибка. Файл пуст")
            print("Ошибка. Файл пуст")
            return []
        else:
            data = json.loads(file1)
            if not isinstance(data, list):
                utils_logger.error("Ошибка: файл не содержит список транзакций.")
                print("Ошибка: файл не содержит список транзакций.")
                return []
        utils_logger.info("Работа функции завершилась успешно")
        return data
    except FileNotFoundError:
        utils_logger.error(f"Ошибка: файл '{path_data}' не найден.")
        print(f"Ошибка: файл '{path_data}' не найден.")
        return []
    except json.JSONDecodeError:
        utils_logger.error("Ошибка декодирования файла")
        print("Ошибка декодирования файла")
        return []
    except Exception as e:
        utils_logger.error(f"Произошла ошибка: {str(e)}")
        print(f"Произошла ошибка: {str(e)}")
        return []


if __name__ == "__main__":
    print(transactions_data("C:/Users/wapwi/PycharmProjects/Domashka91/data/operations.json"))
    print(transactions_data("../data/operations.json"))
    print(transactions_data("../data/operations1.json"))
    print(transactions_data("../data/operations2.json"))
    print(transactions_data("../data/operations3.json"))
    print(transactions_data("../data/operations4.json"))
