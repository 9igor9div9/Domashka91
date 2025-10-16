import os

import requests
from dotenv import load_dotenv
from requests.exceptions import RequestException, Timeout

load_dotenv()
api_key = os.getenv("API_KEY")
api_url = "https://api.apilayer.com/exchangerates_data/convert"
api_timeout = 30
rub_currency_code = "RUB"


def amount_transactions_rur(transaction: dict) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    """

    # Валидация структуры
    if not isinstance(transaction, dict) or "operationAmount" not in transaction:
        raise ValueError("Некорректная структура транзакции")

    op_amount = transaction["operationAmount"]

    if not isinstance(op_amount, dict) or "amount" not in op_amount or "currency" not in op_amount:
        raise ValueError("Некорректная структура operationAmount")

    currency = op_amount["currency"]
    amount_str = op_amount["amount"]

    if not isinstance(currency, dict) or "code" not in currency:
        raise ValueError("Некорректная структура currency")

    currency_code = currency["code"]

    # Валидация данных
    try:
        amount_float = float(amount_str)
    except (ValueError, TypeError):
        raise ValueError(f"Некорректная сумма: {amount_str}")

    if amount_float < 0:
        raise ValueError("Сумма не может быть отрицательной")

    if not isinstance(currency_code, str) or len(currency_code) != 3 or not currency_code.isalpha():
        raise ValueError(f"Некорректный код валюты: {currency_code}")

    # Возврат RUB суммы
    if currency_code == rub_currency_code:
        return amount_float

    # Конвертация других валют
    if not api_key:
        raise ValueError("API ключ не найден")

    payload = {"amount": str(amount_float), "from": currency_code, "to": rub_currency_code}
    headers = {"apikey": api_key}

    try:
        response = requests.get(api_url, headers=headers, params=payload, timeout=api_timeout)
        response.raise_for_status()
        data = response.json()
    except Timeout:
        raise RequestException("Таймаут запроса к API превышен")
    except RequestException as e:
        raise RequestException(f"Ошибка API: {e}")
    except ValueError:
        raise ValueError("Некорректный ответ API")

    if not data.get("success") or "result" not in data:
        raise ValueError("Ошибка в ответе API")

    try:
        return float(data["result"])
    except (ValueError, TypeError):
        raise ValueError("Некорректный результат конвертации")


# if __name__ == '__main__':
#     transactions1 = {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   }
#
#     transactions2 = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }
#
#     transactions3 = {
#     "id": 736942989,
#     "state": "EXECUTED",
#     "date": "2019-09-06T00:48:01.081967",
#     "operationAmount": {
#       "amount": "6357.56",
#       "currency": {
#         "name": "GBP",
#         "code": "GBP"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Visa Gold 3654412434951162",
#     "to": "Счет 59986621134048778289"
#   }
#
#     print(amount_transactions_rur(transactions3))
