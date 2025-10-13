import json

import os

def transactions_data(path_data: str) -> list[dict] | None:
    """Возвращает список словарей с данными о финансовых транзакциях из JSON-файла."""
    if not os.path.exists(path_data):
        print(f"Ошибка: файл '{path_data}' не найден.")
        return []
    with open(path_data, "r", encoding="utf-8") as f:
        file = f.read()
    if len(file) == 0:
        print("Ошибка. Файл пуст")
        return []
    else:
        try:
            with open(path_data, "r" , encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, list):
                print("Ошибка: файл не содержит список транзакций.")
                return []
            return data
        except json.JSONDecodeError:
            print("Ошибка декодирования файла")
            return []


if __name__ == "__main__":
    print(transactions_data("C:/Users/wapwi/PycharmProjects/Domashka91/data/operations.json"))
    print(transactions_data("../data/operations1.json"))
    print(transactions_data("../data/operations2.json"))
    print(transactions_data("../data/operations3.json"))
    print(transactions_data("../data/operations4.json"))
