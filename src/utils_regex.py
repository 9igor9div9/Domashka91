import re


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка"""
    try:
        # Проверка типа входных данных
        if not isinstance(data, list):
            raise TypeError("data должен быть списком")
        if not isinstance(search, str):
            raise TypeError("search должен быть строкой")

        # Проверка на пустые данные
        if not data:
            return []
        if not search:
            return data

        pattern = re.compile(search.lower())
        list_search = [item for item in data if re.search(pattern, item["description"].lower())]
        return list_search
    except re.error as e:
        print(f"Ошибка в регулярном выражении: {e}")
        return []
    except KeyError as e:
        print(f"Отсутствует ключ в словаре: {e}")
        return []
    except AttributeError as e:
        print(f"Ошибка атрибута: {e}")
        return []
    except Exception as e:
        print(f"Ошибка: {e}")
        return []


if __name__ == "__main__":
    test_list = [
        {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD","code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
        },
        {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
        },
        {
        "id": 214024827,
        "state": "EXECUTED",
        "date": "2018-12-20T16:43:26.929246",
        "operationAmount": {"amount": "70946.18", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 10848359769870775355",
        "to": "Счет 21969751544412966366"
        },
        {
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-07-12T20:41:47.882230",
        "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 48894435694657014368",
        "to": "Счет 38976430693692818358"
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        }
    ]

    print(process_bank_search(test_list, "Открытие"))