import pytest

from src.processing import filter_by_state, sort_by_date

from tests.conftest import (list_filter, list_expected_parametric_1,
                            list_expected_parametric_2, list_expected_parametric_3)


def test_filter_by_state_by_default(list_of_event, list_of_event_expected):
    """Тестирование фильтрации списка словарей по умолчанию"""
    assert filter_by_state(list_of_event) == list_of_event_expected


def test_filter_by_state_not_default(list_of_event, list_of_event_expected_state):
    """Тестирование фильтрации списка словарей по заданному статусу"""
    assert filter_by_state(list_of_event, "CANCELED") == list_of_event_expected_state


def test_filter_by_date_not_state_in_list(list_of_event_expected):
    """Проверка работы функции при отсутствии словарей с указанным статусом"""
    assert filter_by_state(list_of_event_expected, "CANCELED") == []


@pytest.mark.parametrize("list_parametric, state, expected", [(list_filter, "EXECUTED", list_expected_parametric_1),
                                                            (list_filter, "PENDING", list_expected_parametric_2),
                                                            (list_filter, "CANCELED", list_expected_parametric_3)])
def test_filter_by_state_parametrize(list_parametric, state, expected):
    """Параметризация тестов для различных возможных значений статуса."""
    assert filter_by_state(list_filter, state) == expected


