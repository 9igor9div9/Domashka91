def filter_by_state(list_of_events: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и опционально значение для ключа. Возвращает новый список словарей,
    содержащий только те словари, у которых ключ соответствует указанному значению."""
    sort_list_of_events = []
    for event in list_of_events:
        if event.get("state") == state:
            sort_list_of_events.append(event)
    return sort_list_of_events


def sort_by_date(list_of_events_2: list[dict], sort_order: bool = True) -> list[dict]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки.
    Возвращает новый список, отсортированный по дате."""
    sort_list_of_events2 = sorted(list_of_events_2, key=lambda x: x["date"], reverse=sort_order)
    return sort_list_of_events2


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
    )

    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
        )
    )
