import os
import time
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import transactions_data
from src.utils_regex import process_bank_search
from src.utils_table import transactions_data_csv, transactions_data_xlsx
from src.widget import get_date, mask_account_card


def user_input() -> list[dict] | None:
    """Запрашивает у пользователя источник информации о транзакциях и возвращает список словарей с данными"""
    try:
        input_user = input("Введите 1, 2 или 3:").strip()
        if input_user == "1":
            print("Для обработки выбран JSON-файл.\n")
            return transactions_data(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                                      "data", "operations.json")))
        elif input_user == "2":
            print("Для обработки выбран CSV-файл.\n")
            return transactions_data_csv(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                                      "data", "transactions.csv")))
        elif input_user == "3":
            print("Для обработки выбран XLSX-файл.\n")
            return transactions_data_xlsx(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                                      "data", "transactions_excel.xlsx")))
        else:
            print("Такого пункта нет.")
            return user_input()
    except Exception as e:
        print(f"Ошибка: {e}")

def user_filter(transactions: list[dict]) -> list[dict] | None:
    """Запрашивает у пользователя статус, по которому необходимо выполнить фильтрацию
    и возвращает список словарей с данными"""
    try:
        filter_user = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.").strip()
        if filter_user.upper() != "EXECUTED" and filter_user.upper() != "CANCELED" and filter_user.upper() != "PENDING":
            print(f"Статус операции '{filter_user}' недоступен.")
            return user_filter(transactions)
        return filter_by_state(transactions, filter_user.upper())
    except Exception as e:
        print(f"Ошибка: {e}")


def user_sorted_up_to_down():
    """Запрашивает у пользователя порядок сортировки и возвращает булево значение"""
    try:
        user_sort_up_to_down = input("Отсортировать по возрастанию или по убыванию?").strip()
        if user_sort_up_to_down.upper() == "ПО ВОЗРАСТАНИЮ":
            return False
        elif user_sort_up_to_down.upper() == "ПО УБЫВАНИЮ":
            return True
        else:
            print("Такого пункта нет.")
            return user_sorted_up_to_down()
    except Exception as e:
        print(f"Ошибка: {e}")


def user_sorted_date(transactions):
    """Запрашивает у пользователя необходимость в сортировке по дате и сортирует в случае положительного ответа.
    Возвращает список словарей с данными"""
    try:
        user_sorted = input("Отсортировать операции по дате? Да/Нет").strip()
        if user_sorted.upper() == "ДА":
            sort_up_to_down = user_sorted_up_to_down()
            return sort_by_date(transactions, sort_up_to_down)
        elif user_sorted.upper() == "НЕТ":
            return transactions
        else:
            print("Такого пункта нет.")
            return user_sorted_date(transactions)
    except Exception as e:
        print(f"Ошибка: {e}")


def user_filter_currency(transactions):
    """Запрашивает у пользователя необходимость в фильтрации по валюте(рубль) и
    фильтрует в случае положительного ответа. Возвращает список словарей с данными"""
    try:
        user_sorted = input("Выводить только рублевые транзакции? Да/Нет").strip()
        if user_sorted.upper() == "ДА":
            return list(filter_by_currency(transactions, "RUB"))
        elif user_sorted.upper() == "НЕТ":
            return transactions
        else:
            print("Такого пункта нет.")
            return user_filter_currency(transactions)
    except Exception as e:
        print(f"Ошибка: {e}")


def user_filter_word(transactions):
    """Запрашивает у пользователя необходимость в фильтрации по наличию определённого слова в описании транзакции и
    фильтрует в случае положительного ответа. Возвращает список словарей с данными"""
    try:
        user_filter_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").strip()
        if user_filter_input.upper() == "ДА":
            user_input_search = input("Введите слово:").strip()
            return process_bank_search(transactions, user_input_search)
        elif user_filter_input.upper() == "НЕТ":
            return transactions
        else:
            print("Такого пункта нет.")
            return user_filter_word(transactions)
    except Exception as e:
        print(f"Ошибка: {e}")



def main():
    """Выполняет основную логику программы виджета банковских операций"""
    try:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
              "Выберите необходимый пункт меню:\n"
              "1. Получить информацию о транзакциях из JSON-файла\n"
              "2. Получить информацию о транзакциях из CSV-файла\n"
              "3. Получить информацию о транзакциях из XLSX-файла.")
        transactions_list = user_input()
        if len(transactions_list) == 0 :
            raise "Нет входящих данных для фильтрации"
        transactions_list_filter = user_filter(transactions_list)
        transactions_list_sort_date = user_sorted_date(transactions_list_filter)
        transactions_list_filter_currency = user_filter_currency(transactions_list_sort_date)
        transactions_list_sort_word = user_filter_word(transactions_list_filter_currency)
        text = "Распечатываю итоговый список транзакций...\n"
        for char in text:
            print(char, end='', flush=True)
            if char == '.':
                time.sleep(0.7)
        if len(transactions_list_sort_word) == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        else:
            print(f"Всего банковских операций в выборке: {len(transactions_list_sort_word)}")
        for transactions_result in transactions_list_sort_word:
            transactions_from = (
                                 f"{mask_account_card(transactions_result.get('from'))} -> "
                                 if 'from' in transactions_result.keys()
                                 and not isinstance(transactions_result.get('from'), float) else ""
                                )
            transactions_to = mask_account_card(transactions_result.get('to'))
            print(
                  f"{get_date(transactions_result.get('date'))} {transactions_result.get('description')}\n"
                  f"{transactions_from}{transactions_to}\n"
                  f"Сумма: {(transactions_result.get("operationAmount").get('amount') if 'operationAmount' 
                            in transactions_result.keys() else transactions_result.get('amount'))} "
                  f"{(transactions_result.get("operationAmount").get('currency').get("name") if 'operationAmount' 
                            in transactions_result.keys() else transactions_result.get('currency_name'))}\n"
                 )
    except Exception as e:
        print(f"Ошибка: {e}")



if __name__ == '__main__':
    main()
