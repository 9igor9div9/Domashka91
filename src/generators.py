from typing import Any, Generator, Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> str | Iterator[Any]:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной."""
    transactions_iter = []
    if len(transactions) == 0:
        return "Отсутствуют входящие данные"
    else:
        for transaction in transactions:
            if "operationAmount" not in transaction:
                return "Некорректные входящие данные"
            elif transaction["operationAmount"]["currency"]["code"] == currency:
                transactions_iter.append(transaction)
    if len(transactions_iter) == 0:
        return "Транзакции в заданной валюте отсутствуют"
    else:
        return iter(transactions_iter)


def transaction_descriptions(transactions: list[dict]) -> Generator[str | Iterator[Any], Any, None]:
    """Принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди."""
    if len(transactions) == 0:
        yield "Отсутствуют входящие данные"
    else:
        for transaction in transactions:
            yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[Any]:
    """Принимает начальное и конечное значения для генерации диапазона
    номеров (от 0000 0000 0000 0001 до 9999 9999 9999 9999).
    Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X— цифра номера карты."""
    if stop > 9999999999999999:
        raise ValueError("Превышен диапазон генерации номеров карт")
    elif start < 0 or stop < 0:
        raise ValueError("Число не может быть отрицательным")
    card_number_iter = []
    for i in range(start, stop + 1):
        number = str(i).zfill(16)
        formatted_number = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
        card_number_iter.append(formatted_number)
    return iter(card_number_iter)


# transactions_2 = []
# transactions_1 =  [{
#              "id": 939719570,
#              "state": "EXECUTED",
#              "date": "2018-06-30T02:08:58.425572",
#              "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD" }},
#              "description": "Перевод организации",
#              "from": "Счет 75106830613657916952",
#              "to": "Счет 11776614605963066702"
#             },
#             {
#               "id": 142264268,
#               "state": "EXECUTED",
#               "date": "2019-04-04T23:20:05.206878",
#               "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#               "description": "Перевод со счета на счет",
#               "from": "Счет 19708645243227258542",
#               "to": "Счет 75651667383060284188"
#             },
#             {
#               "id": 939719570,
#               "state": "EXECUTED",
#               "date": "2020-06-30T02:08:58.425572",
#               "operationAmount": {"amount": "120000.07", "currency": {"name": "RUR", "code": "RUR"}},
#               "description": "Перевод зарплаты",
#               "from": "Счет 75106830613657916952",
#               "to": "Счет 11776614605963066702"
#             },
#             {
#               "id": 142264268,
#               "state": "EXECUTED",
#               "date": "2021-04-04T23:20:05.206878",
#               "operationAmount": {"amount": "60000.93", "currency": {"name": "RUR", "code": "RUR"}},
#               "description": "Перевод аванса",
#               "from": "Счет 19708645243227258542",
#               "to": "Счет 75651667383060284188"
#             }
#            ]


# if __name__ == "__main__":
#     gen = filter_by_currency(transactions_1, "RUR")
#     for _ in range(2):
#         print(next(gen))
#
# descriptions = transaction_descriptions(transactions_1)
# for _ in range(4):
#     print(next(descriptions))
# print(next(transaction_descriptions(transactions_2)))
#
#     for card_number in card_number_generator(-1, 10):
#         print(card_number)
#     g = filter_by_currency(transactions_1, "USD")
#    print(next(g))
#    print(next(g))
#    print(filter_by_currency(transactions_1, "USD"))
