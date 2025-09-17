import pytest


from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number):
    """Тестирование функции get_mask_card_number при корректных данных"""
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_card_number_type():
    """Тестирование функции get_mask_card_number при неожидаемом типе данных"""
    with pytest.raises(TypeError):
        get_mask_card_number("7000792289606361")


def test_get_mask_card_number_negative():
    """Тестирование функции get_mask_card_number при отрицательном значении данных"""
    with pytest.raises(TypeError):
        get_mask_card_number(-7000792289606361)


def test_get_mask_card_number_len_max(card_number):
    """Тестирование функции get_mask_card_number при большем количестве цифр"""
    with pytest.raises(ValueError):
        get_mask_card_number(700079228960636156879546)


def test_get_mask_card_number_len_min(card_number):
    """Тестирование функции get_mask_card_number при меньшем количестве цифр"""
    with pytest.raises(ValueError):
        get_mask_card_number(70007922896)


def test_get_mask_card_number_none():
    """Тестирование функции get_mask_card_number при отсутствии входящих данных"""
    with pytest.raises(ValueError):
        get_mask_card_number(None)


def test_get_mask_account(account):
    """Тестирование функции get_mask_account при корректных данных"""
    assert get_mask_account(account) == "**4305"


def test_get_mask_account_type():
    """Тестирование функции get_mask_account при неожидаемом типе данных"""
    with pytest.raises(TypeError):
        get_mask_account("73654108430135874305")


def test_get_mask_account_negative():
    """Тестирование функции get_mask_account при отрицательном значении данных"""
    with pytest.raises(TypeError):
        get_mask_account(-73654108430135874305)


def test_get_mask_account_len_max(card_number):
    """Тестирование функции get_mask_account при большем количестве цифр"""
    with pytest.raises(ValueError):
        get_mask_account(736541084301358743055454876)


def test_get_mask_account_len_min(card_number):
    """Тестирование функции get_mask_account при меньшем количестве цифр"""
    with pytest.raises(ValueError):
        get_mask_account(7365410843013)


def test_get_mask_account_none():
    """Тестирование функции get_mask_account при отсутствии входящих данных"""
    with pytest.raises(ValueError):
        get_mask_account(None)
