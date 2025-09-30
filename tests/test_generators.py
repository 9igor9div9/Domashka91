from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from tests.conftest import (
    transactions_par,
    transactions_par_rur1,
    transactions_par_rur2,
    transactions_par_usd1,
    transactions_par_usd2,
)


def test_filter_by_currency(
    transactions_1: list[Any], currency_usd: str, transactions_usd1: dict, transactions_usd2: dict
) -> None:
    """Тестирование фильтрации транзакций по заданной валюте. filter_by_currency"""
    gen = filter_by_currency(transactions_1, currency_usd)
    assert next(gen) == transactions_usd1
    assert next(gen) == transactions_usd2


@pytest.mark.parametrize(
    "transactions_parametric, currency_parametric, expected_1, expected_2",
    [
        (transactions_par, "USD", transactions_par_usd1, transactions_par_usd2),
        (transactions_par, "RUR", transactions_par_rur1, transactions_par_rur2),
    ],
)
def test_filter_by_currency_parametric(
    transactions_parametric: list[Any], currency_parametric: str, expected_1: dict, expected_2: dict
) -> None:
    """Параметрический тест функции filter_by_currency."""
    gen_parametric = filter_by_currency(transactions_parametric, currency_parametric)
    assert next(gen_parametric) == expected_1
    assert next(gen_parametric) == expected_2


def test_filter_by_currency_not_currency(transactions_rur: list[Any], currency_usd: str) -> None:
    """Тестирование функции filter_by_currency, когда транзакции в заданной валюте отсутствуют."""
    assert filter_by_currency(transactions_rur, currency_usd) == "Транзакции в заданной валюте отсутствуют"


def test_filter_by_currency_not(currency_usd: str) -> None:
    """Тестирование функции filter_by_currency, при пустом списке"""
    assert filter_by_currency([], currency_usd) == "Отсутствуют входящие данные"


def test_filter_by_currency_not_operationamount(
    transactions_not_operationamount: list[Any], currency_usd: str
) -> None:
    """Тестирование функции filter_by_currency, без соответствующих валютных операций в списке"""
    assert filter_by_currency(transactions_not_operationamount, currency_usd) == "Некорректные входящие данные"


def test_transaction_descriptions(transactions_1: list[Any]) -> None:
    """Проверка, что функция transaction_descriptions возвращает корректные описания для каждой транзакции."""
    descriptions = transaction_descriptions(transactions_1)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод зарплаты"
    assert next(descriptions) == "Перевод аванса"


def test_transaction_descriptions2(transactions_rur: list[Any]) -> None:
    """Работа функции transaction_descriptions с другим количеством входных транзакций"""
    descriptions = transaction_descriptions(transactions_rur)
    assert next(descriptions) == "Перевод зарплаты"
    assert next(descriptions) == "Перевод аванса"


def test_transaction_descriptions_not_transactions(transactions_not: list[Any]) -> None:
    """Работа функции transaction_descriptions с пустым списком на входе"""
    assert next(transaction_descriptions(transactions_not)) == "Отсутствуют входящие данные"


def test_card_number_generator() -> None:
    """Тест функции card_number_generator на выдачу
    правильных номеров карт в заданном диапазоне"""
    gen_card = card_number_generator(1, 5)
    assert next(gen_card) == "0000 0000 0000 0001"
    assert next(gen_card) == "0000 0000 0000 0002"
    assert next(gen_card) == "0000 0000 0000 0003"
    assert next(gen_card) == "0000 0000 0000 0004"
    assert next(gen_card) == "0000 0000 0000 0005"


def test_card_number_generator_format() -> None:
    """Проверка корректности формата номеров карт. card_number_generator"""
    gen_card = next(card_number_generator(1, 1))
    list_num_gen_card = []
    for num_gen_card in str(gen_card):
        if num_gen_card.isdigit():
            list_num_gen_card.append("Цифра")
        elif num_gen_card == " ":
            list_num_gen_card.append("Пробел")
    assert list_num_gen_card == [
        "Цифра",
        "Цифра",
        "Цифра",
        "Цифра",
        "Пробел",
        "Цифра",
        "Цифра",
        "Цифра",
        "Цифра",
        "Пробел",
        "Цифра",
        "Цифра",
        "Цифра",
        "Цифра",
        "Пробел",
        "Цифра",
        "Цифра",
        "Цифра",
        "Цифра",
    ]


def test_card_number_generator_beginning() -> None:
    """Тест начальных значений диапазона номеров карт. card_number_generator"""
    gen_card1 = card_number_generator(0, 2)
    assert next(gen_card1) == "0000 0000 0000 0000"
    assert next(gen_card1) == "0000 0000 0000 0001"
    assert next(gen_card1) == "0000 0000 0000 0002"


def test_card_number_generator_ending() -> None:
    """Тест конечных значений диапазона номеров карт. card_number_generator"""
    gen_card2 = card_number_generator(9999999999999997, 9999999999999999)
    assert next(gen_card2) == "9999 9999 9999 9997"
    assert next(gen_card2) == "9999 9999 9999 9998"
    assert next(gen_card2) == "9999 9999 9999 9999"


def test_card_number_generator_beginning_exceeding_limit() -> None:
    """Тест превышения начальных значений диапазона номеров карт. card_number_generator"""
    with pytest.raises(ValueError):
        card_number_generator(-1, 1)


def test_card_number_generator_beginning_ending_limit() -> None:
    """Тест превышения конечных значений диапазона номеров карт. card_number_generator"""
    with pytest.raises(ValueError):
        card_number_generator(9999999999999999, 10000000000000000)
