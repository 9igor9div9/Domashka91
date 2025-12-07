import os
import time
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import transactions_data
from src.utils_regex import process_bank_search
from src.utils_table import transactions_data_csv, transactions_data_xlsx
from src.widget import get_date, mask_account_card


def user_input():
    input_user = input("Введите 1, 2 или 3:")
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


def user_filter(transactions):
    filter_user = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.")
    if filter_user.upper() != "EXECUTED" and filter_user.upper() != "CANCELED" and filter_user.upper() != "PENDING":
        print(f"Статус операции '{filter_user}' недоступен.")
        return user_filter(transactions)
    return filter_by_state(transactions, filter_user.upper())


def user_sorted_up_to_down():
    user_sort_up_to_down = input("Отсортировать по возрастанию или по убыванию?")
    if user_sort_up_to_down.upper() == "ПО ВОЗРАСТАНИЮ":
        return False
    elif user_sort_up_to_down.upper() == "ПО УБЫВАНИЮ":
        return True
    else:
        print("Такого пункта нет.")
        return user_sorted_up_to_down()


def user_sorted_date(transactions):
    user_sorted = input("Отсортировать операции по дате? Да/Нет")
    if user_sorted.upper() == "ДА":
        sort_up_to_down = user_sorted_up_to_down()
        return sort_by_date(transactions, sort_up_to_down)
    elif user_sorted.upper() == "НЕТ":
        return transactions
    else:
        print("Такого пункта нет.")
        return user_sorted_date(transactions)


def user_sorted_currency(transactions):
    user_sorted = input("Выводить только рублевые транзакции? Да/Нет")
    if user_sorted.upper() == "ДА":
        return list(filter_by_currency(transactions, "RUB"))
    elif user_sorted.upper() == "НЕТ":
        return transactions
    else:
        print("Такого пункта нет.")
        return user_sorted_currency(transactions)


def user_filter_word(transactions):
    user_filter_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    if user_filter_input.upper() == "ДА":
        user_input_search = input("Введите слово:")
        return process_bank_search(transactions, user_input_search)
    elif user_filter_input.upper() == "НЕТ":
        return transactions
    else:
        print("Такого пункта нет.")
        return user_filter_word(transactions)



def main():
    try:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
              "Выберите необходимый пункт меню:\n"
              "1. Получить информацию о транзакциях из JSON-файла\n"
              "2. Получить информацию о транзакциях из CSV-файла\n"
              "3. Получить информацию о транзакциях из XLSX-файла.")
        input_user = input("Введите 1, 2 или 3:")
        transactions_list = user_input()
        print(transactions_list)
        if len(transactions_list) == 0 :
            raise "Нет входящих данных для фильтрации"
        transactions_list_filter = user_filter(transactions_list)
        print(transactions_list_filter)
        transactions_list_sort_date = user_sorted_date(transactions_list_filter)
        print(transactions_list_sort_date)
        transactions_list_sort_currency = user_sorted_currency(transactions_list_sort_date)
        print(transactions_list_sort_currency)
        transactions_list_sort_word = user_filter_word(transactions_list_sort_currency)
        print(transactions_list_sort_word)
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
            # print(transactions_result.get('from'))
            # print(type(transactions_result.get('from')))
            transactions_from = (f"{mask_account_card(transactions_result.get('from'))} -> "
                                  if 'from' in transactions_result.keys()
                                  and not isinstance(transactions_result.get('from'), float) else "")
            transactions_to = mask_account_card(transactions_result.get('to'))
            print(f"{get_date(transactions_result.get('date'))} {transactions_result.get('description')}\n"
                  f"{transactions_from}{transactions_to}\n"
                  f"Сумма: {(transactions_result.get("operationAmount").get('amount') if 'operationAmount' 
                            in transactions_result.keys() else transactions_result.get('amount'))} "
                  f"{(transactions_result.get("operationAmount").get('currency').get("name") if 'operationAmount' 
                            in transactions_result.keys() else transactions_result.get('currency_name'))}\n")
    except Exception as e:
        print(f"Ошибка: {e}")



if __name__ == '__main__':
    main()
