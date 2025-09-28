from typing import Iterator, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str]:
    for transaction in transactions:
        description = transaction["description"]
        yield description




transactions_1 =  [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2020-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "120000.07",
              "currency": {
                  "name": "RUR",
                  "code": "RUR"
              }
          },
          "description": "Перевод зарплаты",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2021-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "60000.93",
                  "currency": {
                      "name": "RUR",
                      "code": "RUR"
                  }
              },
              "description": "Перевод аванса",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]


if __name__ == "__main__":
    #for _ in range(2):
        #print(next(filter_by_currency(transactions_1, "USD")))

    descriptions = transaction_descriptions(transactions_1)
    for _ in range(4):
        print(next(descriptions))

