from typing import Iterator

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency(transactions_1, currency_usd, transactions_usd1) -> None:
    """Тестирование фильтрации транзакций по заданной валюте"""
    transactions_usd = []
    for _ in range(2):
        transactions_usd.append(next(filter_by_currency(transactions_1, currency_usd)))
    assert transactions_usd == transactions_usd1


def test_filter_by_currency_not_currency(transactions_rur, currency_usd) -> None:
    """Тестирование функции, когда транзакции в заданной валюте отсутствуют."""
    assert filter_by_currency(transactions_rur, currency_usd) == "Транзакции в заданной валюте отсутствуют"


def test_filter_by_currency_not(currency_usd) -> None:
    """Тестирование функции, при пустом списке"""
    assert filter_by_currency([], currency_usd) == "Отсутствуют входящие данные"


def test_filter_by_currency_not_operationamount(transactions_not_operationamount, currency_usd) -> None:
    """Тестирование функции, без соответствующих валютных операций в списке"""
    assert filter_by_currency(transactions_not_operationamount, currency_usd) == "Некорректные входящие данные"
