import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number_test: int) -> None:
    """Тестирование функции get_mask_card_number при корректных данных"""
    assert get_mask_card_number(card_number_test) == "7000 79** **** 6361"


def test_get_mask_card_number_len_max(card_number_test: int) -> None:
    """Тестирование функции get_mask_card_number при большем количестве цифр"""
    with pytest.raises(ValueError):
        get_mask_card_number(700079228960636156879546)


def test_get_mask_card_number_len_min(card_number_test: int) -> None:
    """Тестирование функции get_mask_card_number при меньшем количестве цифр"""
    with pytest.raises(ValueError):
        get_mask_card_number(70007922896)


def test_get_mask_account_no_number(card_number_test: int) -> None:
    """Тестирование функции get_mask_card_number при отсутствии номера карты"""
    with pytest.raises(ValueError):
        get_mask_card_number()


def test_get_mask_account(account_test: int) -> None:
    """Тестирование функции get_mask_account при корректных данных"""
    assert get_mask_account(account_test) == "**4305"


def test_get_mask_account_len_max(card_number_test: int) -> None:
    """Тестирование функции get_mask_account при большем количестве цифр"""
    with pytest.raises(ValueError):
        get_mask_account(736541084301358743055454876)


def test_get_mask_account_len_min(card_number_test: int) -> None:
    """Тестирование функции get_mask_account при меньшем количестве цифр"""
    with pytest.raises(ValueError):
        get_mask_account(7365410843013)


def test_get_mask_account_none() -> None:
    """Тестирование функции get_mask_account при отсутствии входящих данных"""
    with pytest.raises(ValueError):
        get_mask_account()
