from typing import Any

import pytest


# Фикстуры для test_masks.py
@pytest.fixture
def card_number_test() -> int:
    """Фикстура для get_mask_card_number"""
    return 7000792289606361


@pytest.fixture
def account_test() -> int:
    """Фикстура для get_mask_account"""
    return 73654108430135874305


# Фикстуры для test_widget.py
@pytest.fixture
def requisites_number_account() -> str:
    """Фикстура для mask_account_card"""
    return "Счет 73654108430135874305"


@pytest.fixture
def required_number_card() -> str:
    """Фикстура для mask_account_card"""
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def date_test() -> str:
    """Фикстура для get_date"""
    return "2024-03-11T02:26:18.671407"


# Фикстуры и переменные для test_processing.py
@pytest.fixture
def state_test() -> str:
    """Фикстура для filter_by_state"""
    return "CANCELED"


@pytest.fixture
def list_of_event_test() -> list[dict[str, Any]]:
    """Фикстура для filter_by_state"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594220000, "state": "PENDING", "date": "2017-05-12T21:27:25.241689"},
        {"id": 615061111, "state": "PENDING", "date": "2017-15-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_event_expected() -> list[dict[str, Any]]:
    """Фикстура для filter_by_state"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_of_event_expected_state() -> list[dict[str, Any]]:
    """Фикстура для filter_by_state"""
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Переменные для параметрического теста filter_by_state
list_filter = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594220000, "state": "PENDING", "date": "2017-05-12T21:27:25.241689"},
    {"id": 615061111, "state": "PENDING", "date": "2017-15-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

list_expected_parametric_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

list_expected_parametric_2 = [
    {"id": 594220000, "state": "PENDING", "date": "2017-05-12T21:27:25.241689"},
    {"id": 615061111, "state": "PENDING", "date": "2017-15-14T08:21:33.419441"},
]

list_expected_parametric_3 = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


# Фикстуры и переменные для test_processing.py
@pytest.fixture
def list_of_events_2_test() -> list[dict[str, Any]]:
    """Фикстура для sort_by_date"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_events_2_true() -> list[dict[str, Any]]:
    """Фикстура для sort_by_date"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_of_events_2_false() -> list[dict[str, Any]]:
    """Фикстура для sort_by_date"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def list_of_events_2_double_data() -> list[dict[str, Any]]:
    """Фикстура для sort_by_date"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064781, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_events_2_double_data_test() -> list[dict[str, Any]]:
    """Фикстура для sort_by_date"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064781, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_of_events_2_no_correct_data() -> list[dict[str, Any]]:
    """Фикстура для sort_by_date"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": 1234567890},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_events_2_no_data() -> list[dict[str, Any]]:
    """Фикстура для sort_by_date"""
    return [
        {"id": 41428829, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_events_2_no_correct() -> list[dict[str, Any]]:
    """Фикстура для sort_by_date"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Фикстуры и переменные для generators.py

@pytest.fixture
def transactions_1():
    """Фикстура для filter_by_currency и transaction_descriptions"""
    return [{
             "id": 939719570,
             "state": "EXECUTED",
             "date": "2018-06-30T02:08:58.425572",
             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD" }},
             "description": "Перевод организации",
             "from": "Счет 75106830613657916952",
             "to": "Счет 11776614605963066702"
            },
            {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
            },
            {
              "id": 939719570,
              "state": "EXECUTED",
              "date": "2020-06-30T02:08:58.425572",
              "operationAmount": {"amount": "120000.07", "currency": {"name": "RUR", "code": "RUR"}},
              "description": "Перевод зарплаты",
              "from": "Счет 75106830613657916952",
              "to": "Счет 11776614605963066702"
            },
            {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2021-04-04T23:20:05.206878",
              "operationAmount": {"amount": "60000.93", "currency": {"name": "RUR", "code": "RUR"}},
              "description": "Перевод аванса",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
            }
           ]


@pytest.fixture
def currency_usd():
    """Фикстура для filter_by_currency"""
    return "USD"


@pytest.fixture
def currency_rur():
    """Фикстура для filter_by_currency"""
    return "RUR"


@pytest.fixture
def transactions_usd1():
    """Фикстура для filter_by_currency"""
    return {'id': 939719570, 'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572',
            'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод организации',
            'from': 'Счет 75106830613657916952',
            'to': 'Счет 11776614605963066702'
            }


@pytest.fixture
def transactions_usd2():
    """Фикстура для filter_by_currency"""
    return {'id': 142264268, 'state': 'EXECUTED',
            'date': '2019-04-04T23:20:05.206878',
            'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод со счета на счет',
            'from': 'Счет 19708645243227258542',
            'to': 'Счет 75651667383060284188'
            }


@pytest.fixture
def transactions_rur():
    """Фикстура для filter_by_currency"""
    return [{
              "id": 939719570,
              "state": "EXECUTED",
              "date": "2020-06-30T02:08:58.425572",
              "operationAmount": {"amount": "120000.07", "currency": {"name": "RUR", "code": "RUR"}},
              "description": "Перевод зарплаты",
              "from": "Счет 75106830613657916952",
              "to": "Счет 11776614605963066702"
            },
            {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2021-04-04T23:20:05.206878",
              "operationAmount": {"amount": "60000.93", "currency": {"name": "RUR", "code": "RUR"}},
              "description": "Перевод аванса",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
            }
           ]


@pytest.fixture
def transactions_not_operationamount():
    """Фикстура для filter_by_currency"""
    return [{
             "id": 939719570,
             "state": "EXECUTED",
             "date": "2018-06-30T02:08:58.425572",
             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD" }},
             "description": "Перевод организации",
             "from": "Счет 75106830613657916952",
             "to": "Счет 11776614605963066702"
            },
            {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
            },
            {
              "id": 939719570,
              "state": "EXECUTED",
              "date": "2020-06-30T02:08:58.425572",
              "operationAmount": {"amount": "120000.07", "currency": {"name": "RUR", "code": "RUR"}},
              "description": "Перевод зарплаты",
              "from": "Счет 75106830613657916952",
              "to": "Счет 11776614605963066702"
            },
            {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2021-04-04T23:20:05.206878",
              "operationAmount": {"amount": "60000.93", "currency": {"name": "RUR", "code": "RUR"}},
              "description": "Перевод аванса",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
            }
           ]


@pytest.fixture
def transactions_not():
    return []


# Переменные для параметрического теста filter_by_currency
transactions_par = [{
             "id": 939719570,
             "state": "EXECUTED",
             "date": "2018-06-30T02:08:58.425572",
             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD" }},
             "description": "Перевод организации",
             "from": "Счет 75106830613657916952",
             "to": "Счет 11776614605963066702"
            },
            {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
            },
            {
              "id": 939719570,
              "state": "EXECUTED",
              "date": "2020-06-30T02:08:58.425572",
              "operationAmount": {"amount": "120000.07", "currency": {"name": "RUR", "code": "RUR"}},
              "description": "Перевод зарплаты",
              "from": "Счет 75106830613657916952",
              "to": "Счет 11776614605963066702"
            },
            {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2021-04-04T23:20:05.206878",
              "operationAmount": {"amount": "60000.93", "currency": {"name": "RUR", "code": "RUR"}},
              "description": "Перевод аванса",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
            }
           ]


transactions_par_usd1 = {'id': 939719570, 'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572',
            'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод организации',
            'from': 'Счет 75106830613657916952',
            'to': 'Счет 11776614605963066702'
            }


transactions_par_usd2 = {'id': 142264268, 'state': 'EXECUTED',
            'date': '2019-04-04T23:20:05.206878',
            'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод со счета на счет',
            'from': 'Счет 19708645243227258542',
            'to': 'Счет 75651667383060284188'
            }


transactions_par_rur1 = {'id': 939719570,
                         'state': 'EXECUTED',
                         'date': '2020-06-30T02:08:58.425572',
                         'operationAmount': {'amount': '120000.07', 'currency': {'name': 'RUR', 'code': 'RUR'}},
                         'description': 'Перевод зарплаты',
                         'from': 'Счет 75106830613657916952',
                         'to': 'Счет 11776614605963066702'
                         }


transactions_par_rur2 = {'id': 142264268,
                         'state': 'EXECUTED',
                         'date': '2021-04-04T23:20:05.206878',
                         'operationAmount': {'amount': '60000.93', 'currency': {'name': 'RUR', 'code': 'RUR'}},
                         'description': 'Перевод аванса',
                         'from': 'Счет 19708645243227258542',
                         'to': 'Счет 75651667383060284188'
                         }

