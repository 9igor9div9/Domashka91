import pytest

from src.widget import get_date, mask_account_card


def test_mask_account(requisites_number_account: str) -> None:
    """Тестирование функции mask_account_card при корректных данных(счёт)"""
    assert mask_account_card(requisites_number_account) == "**4305"


def test_mask_account_card(required_number_card: str) -> None:
    """Тестирование функции mask_account_card при корректных данных(карта)"""
    assert mask_account_card(required_number_card) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Счет 73654106789135874405", "**4405"),
        ("Mastercard 7011792289606251", "7011 79** **** 6251"),
        ("Счет 73654106789135874445", "**4445"),
        ("МИР 7011792289606276", "7011 79** **** 6276"),
        ("Account 73654106789135874488", "**4488"),
        ("UnionPay 7011792289606245", "7011 79** **** 6245"),
    ],
)
def test_mask_account_card_multi(account_card: str, expected: str) -> None:
    """Параметризованные тесты функции mask_account_card с разными типами
    карт и счетов для проверки универсальности функции."""
    assert mask_account_card(account_card) == expected


def test_mask_account_card_min() -> None:
    """Тестирование функции mask_account_card при большем количестве цифр"""
    with pytest.raises(ValueError):
        mask_account_card("Счет 73654106789135805")


def test_mask_account_card_max() -> None:
    """Тестирование функции mask_account_card при большем количестве цифр"""
    with pytest.raises(ValueError):
        mask_account_card("Mastercard 701179228967606251")


def test_mask_account_card_None() -> None:
    """Тестирование функции mask_account_card при отсутствии входящих данных"""
    with pytest.raises(ValueError):
        mask_account_card(None)


def test_mask_account_card_type() -> None:
    """Тестирование функции mask_account_card при неожидаемом типе данных"""
    with pytest.raises(TypeError):
        mask_account_card(3654108430135874)


def test_get_date(date_test: str) -> None:
    """Тестирование функции get_date при корректных данных(счёт)"""
    assert get_date(date_test) == "11.03.2024"


@pytest.mark.parametrize(
    "date_test, expected",
    [
        ("2024-03-11", "11.03.2024"),
        ("2024-03-11T02:26:18", "11.03.2024"),
        ("2024-03-11T02:26", "11.03.2024"),
        ("2024-03-11T02", "11.03.2024"),
        ("2024-03-11T02:26:18.6714075675648764856856757", "11.03.2024"),
    ],
)
def test_get_date_multi(date_test: str, expected: str) -> None:
    """Параметризованные тесты функции get_date на различных входных форматах даты."""
    assert get_date(date_test) == expected


def test_get_date_None() -> None:
    """Тестирование функции get_date при отсутствии входящих данных"""
    with pytest.raises(ValueError):
        get_date(None)


def test_get_date_type() -> None:
    """Тестирование функции get_date при неожидаемом типе данных"""
    with pytest.raises(TypeError):
        get_date(202403110218671407)


def test_get_date_not_date() -> None:
    """Тестирование функции get_date при отсутствии даты во входящих данных"""
    assert get_date("T02:26:18.671407") == "Некорректный формат даты"


def test_get_date_not_str() -> None:
    """Тестирование функции get_date при пустой строке во входящих данных"""
    assert get_date("") == "Некорректный формат даты"
