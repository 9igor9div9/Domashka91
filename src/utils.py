import json


def transactions_data(path_data: str) -> list[dict] | None:
    """Возвращает список словарей с данными о финансовых транзакциях из JSON-файла."""
    try:
        with open(path_data, "r", encoding="utf-8") as file:
            file1 = file.read()
        if len(file1) == 0:
            print("Ошибка. Файл пуст")
            return []
        else:
            data = json.loads(file1)
            if not isinstance(data, list):
                print("Ошибка: файл не содержит список транзакций.")
                return []
        return data
    except FileNotFoundError:
        print(f"Ошибка: файл '{path_data}' не найден.")
        return []
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return []


# if __name__ == "__main__":
#     print(transactions_data("C:/Users/wapwi/PycharmProjects/Domashka91/data/operations.json"))
#     print(transactions_data("../data/operations.json"))
#     print(transactions_data("../data/operations1.json"))
#     print(transactions_data("../data/operations2.json"))
#     print(transactions_data("../data/operations3.json"))
#     print(transactions_data("../data/operations4.json"))
