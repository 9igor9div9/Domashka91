import logging
import os

import pandas as pd

path_log_utils2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs", "utils_table.log"))
utils_table_logger = logging.getLogger("utils")
utils_table_logger.setLevel(logging.DEBUG)
utils_table_handler = logging.FileHandler(path_log_utils2, encoding="utf-8", mode="w")
utils_table_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
utils_table_handler.setFormatter(utils_table_formatter)
utils_table_logger.addHandler(utils_table_handler)


def transactions_data_csv(path_data: str) -> list[dict] | None:
    """Возвращает список словарей с данными о финансовых транзакциях из CSV-файла."""
    utils_table_logger.info("Начало работы функции")
    try:
        utils_table_logger.info("Читаем CSV файл")
        df_csv = pd.read_csv(path_data, sep=";")
        data = df_csv.to_dict(orient="records")
        result = list()
        for item in data:
            result.append(item)
        utils_table_logger.info("Работа функции завершилась успешно")
        return result
    except FileNotFoundError:
        utils_table_logger.error(f"Ошибка: файл '{path_data}' не найден.")
        print(f"Ошибка: файл '{path_data}' не найден.")
        return []
    except pd.errors.EmptyDataError:
        utils_table_logger.error("Ошибка. Файл пуст")
        print("Ошибка. Файл пуст")
        return []
    except pd.errors.ParserError as e:
        utils_table_logger.error(f"Ошибка парсинга: {e}")
        print(f"Ошибка парсинга: {e}")
        return []
    except UnicodeDecodeError:
        utils_table_logger.error("Неверная кодировка файла")
        print("Неверная кодировка файла")
        return []
    except Exception as e:
        utils_table_logger.error(f"Произошла ошибка: {str(e)}")
        print(f"Произошла ошибка: {str(e)}")
        return []


def transactions_data_xlsx(path_data: str) -> list[dict] | None:
    """Возвращает список словарей с данными о финансовых транзакциях из xlsx-файла."""
    utils_table_logger.info("Начало работы функции")
    try:
        utils_table_logger.info("Читаем xlsx файл")
        df_xlsx = pd.read_excel(path_data)
        data = df_xlsx.to_dict(orient="records")
        result = list()
        for item in data:
            result.append(item)
        utils_table_logger.info("Работа функции завершилась успешно")
        return result
    except FileNotFoundError:
        utils_table_logger.error(f"Ошибка: файл '{path_data}' не найден.")
        print(f"Ошибка: файл '{path_data}' не найден.")
        return []
    except pd.errors.EmptyDataError:
        utils_table_logger.error("Ошибка. Файл пуст")
        print("Ошибка. Файл пуст")
        return []
    except pd.errors.ParserError as e:
        utils_table_logger.error(f"Ошибка парсинга: {e}")
        print(f"Ошибка парсинга: {e}")
        return []
    except UnicodeDecodeError:
        utils_table_logger.error("Неверная кодировка файла")
        print("Неверная кодировка файла")
        return []
    except Exception as e:
        utils_table_logger.error(f"Произошла ошибка: {str(e)}")
        print(f"Произошла ошибка: {str(e)}")
        return []


# if __name__ == "__main__":
#     path_utils_csv = os.path.abspath(os.path.join(os.path.dirname(__file__),
#                                                   "..", "data", "transactions.csv"))
#     path_utils_xlsx = os.path.abspath(os.path.join(os.path.dirname(__file__),
#                                                    "..", "data", "transactions_excel.xlsx"))
#     print(transactions_data_csv(path_utils_csv))
#     print(transactions_data_xlsx(path_utils_xlsx))
