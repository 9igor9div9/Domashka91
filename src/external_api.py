import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def amount_transactions_rur(transactions: dict) -> float:
    """Возвращает сумму транзакции в рублях"""
    if transactions["operationAmount"]["currency"]["code"] == "RUB":
        amount = transactions["operationAmount"]["amount"]
        return amount
    else:
        code = transactions["operationAmount"]["currency"]["code"]
        amount = transactions["operationAmount"]["amount"]
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            "amount": amount,
            "from": code,
            "to": "RUB"
        }
        headers = {
            "apikey": api_key
        }
        response = requests.request("GET", url, headers=headers, params=payload)
#        status_code = response.status_code
        result = response.json()['result']
        return result




if __name__ == '__main__':
    transactions1 = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

    transactions2 = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

    transactions3 = {
    "id": 736942989,
    "state": "EXECUTED",
    "date": "2019-09-06T00:48:01.081967",
    "operationAmount": {
      "amount": "6357.56",
      "currency": {
        "name": "USD",
        "code": "GBP"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 3654412434951162",
    "to": "Счет 59986621134048778289"
  }

    print(amount_transactions_rur(transactions2))


    # url = "https://api.apilayer.com/exchangerates_data/convert"
    #
    # payload = {
    #     "amount": "5",
    #     "from": "EUR",
    #     "to": "RUB"
    # }
    # headers = {
    #     "apikey": api_key
    # }
    #
    # response = requests.request("GET", url, headers=headers, params=payload)
    #
    # status_code = response.status_code
    # result = response.json()['result']
    # print(status_code)
    # print(result)
    # print(type(result))