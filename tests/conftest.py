import pytest


#Фикстуры для test_masks.py
@pytest.fixture
def card_number():
    """Фикстура для get_mask_card_number"""
    return 7000792289606361

@pytest.fixture
def account():
    """Фикстура для get_mask_account"""
    return 73654108430135874305

#Фикстуры для test_widget.py
@pytest.fixture
def requisites_number_account():
    """Фикстура для mask_account_card"""
    return "Счет 73654108430135874305"

@pytest.fixture
def required_number_card():
    """Фикстура для mask_account_card"""
    return "Visa Platinum 7000792289606361"

@pytest.fixture
def date():
    """Фикстура для get_date"""
    return "2024-03-11T02:26:18.671407"

#Фикстуры и переменные для test_processing.py
@pytest.fixture
def list_of_event():
    """Фикстура для filter_by_state"""
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594220000, "state": "PENDING", "date": "2017-05-12T21:27:25.241689"},
            {"id": 615061111, "state": "PENDING", "date": "2017-15-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
            ]

@pytest.fixture
def list_of_event_expected():
    """Фикстура для filter_by_state"""
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]

@pytest.fixture
def list_of_event_expected_state():
    """Фикстура для filter_by_state"""
    return [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]

# Переменные для параметрического теста filter_by_state
list_filter = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                   {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                   {"id": 594220000, "state": "PENDING", "date": "2017-05-12T21:27:25.241689"},
                   {"id": 615061111, "state": "PENDING", "date": "2017-15-14T08:21:33.419441"},
                   {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                   {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
                  ]

list_expected_parametric_1 = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                              {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]

list_expected_parametric_2 = [{"id": 594220000, "state": "PENDING", "date": "2017-05-12T21:27:25.241689"},
                              {"id": 615061111, "state": "PENDING", "date": "2017-15-14T08:21:33.419441"}]

list_expected_parametric_3 = [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                              {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]

