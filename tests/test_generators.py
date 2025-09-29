from typing import Iterator

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import transactions_par, transactions_par_usd1, transactions_par_usd2, transactions_par_rur1, \
    transactions_par_rur2


def test_filter_by_currency(transactions_1, currency_usd, transactions_usd1, transactions_usd2) -> None:
    """Тестирование фильтрации транзакций по заданной валюте"""
    gen = filter_by_currency(transactions_1,currency_usd)
    assert next(gen) == transactions_usd1
    assert next(gen) == transactions_usd2


@pytest.mark.parametrize(
    "transactions_parametric, currency_parametric, expected_1, expected_2",
    [
        (transactions_par, "USD", transactions_par_usd1, transactions_par_usd2),
        (transactions_par, "RUR", transactions_par_rur1, transactions_par_rur2),
    ]
)
def test_filter_by_currency(transactions_parametric, currency_parametric, expected_1, expected_2) -> None:
    """Параметрический тест функции"""
    gen_parametric = filter_by_currency(transactions_parametric,currency_parametric)
    assert next(gen_parametric) == expected_1
    assert next(gen_parametric) == expected_2


def test_filter_by_currency_not_currency(transactions_rur, currency_usd) -> None:
    """Тестирование функции, когда транзакции в заданной валюте отсутствуют."""
    assert filter_by_currency(transactions_rur, currency_usd) == "Транзакции в заданной валюте отсутствуют"


def test_filter_by_currency_not(currency_usd) -> None:
    """Тестирование функции, при пустом списке"""
    assert filter_by_currency([], currency_usd) == "Отсутствуют входящие данные"


def test_filter_by_currency_not_operationamount(transactions_not_operationamount, currency_usd) -> None:
    """Тестирование функции, без соответствующих валютных операций в списке"""
    assert filter_by_currency(transactions_not_operationamount, currency_usd) == "Некорректные входящие данные"


def test_transaction_descriptions(transactions_1) -> None:
    """Проверка, что функция возвращает корректные описания для каждой транзакции."""
    descriptions = transaction_descriptions(transactions_1)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод зарплаты"
    assert next(descriptions) == "Перевод аванса"


def test_transaction_descriptions2(transactions_rur) -> None:
    """Работа функции с другим количеством входных транзакций"""
    descriptions = transaction_descriptions(transactions_rur)
    assert next(descriptions) == "Перевод зарплаты"
    assert next(descriptions) == "Перевод аванса"


def test_transaction_descriptions_not_transactions(transactions_not) -> None:
    """Работа функции с пустым списком на входе"""
    assert transaction_descriptions(transactions_not) == "Отсутствуют входящие данные"


