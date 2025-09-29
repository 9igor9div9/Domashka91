from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import (list_expected_parametric_1, list_expected_parametric_2, list_expected_parametric_3,
                            list_filter)


def test_filter_by_state_by_default(
    list_of_event_test: list[dict[str, Any]], list_of_event_expected: list[dict[str, Any]]
) -> None:
    """Тестирование фильтрации списка словарей по умолчанию"""
    assert filter_by_state(list_of_event_test) == list_of_event_expected


def test_filter_by_state_not_default(
    list_of_event_test: list[dict[str, Any]], list_of_event_expected_state: list[dict[str, Any]], state_test: str
) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу"""
    assert filter_by_state(list_of_event_test, state_test) == list_of_event_expected_state


def test_filter_by_date_not_state_in_list(list_of_event_expected: list[dict[str, Any]], state_test: str) -> None:
    """Проверка работы функции при отсутствии словарей с указанным статусом"""
    assert filter_by_state(list_of_event_expected, state_test) == []


@pytest.mark.parametrize(
    "list_parametric, state, expected",
    [
        (list_filter, "EXECUTED", list_expected_parametric_1),
        (list_filter, "PENDING", list_expected_parametric_2),
        (list_filter, "CANCELED", list_expected_parametric_3)
    ]
)
def test_filter_by_state_parametrize(
    list_parametric: list[dict[str, Any]], state: str, expected: list[dict[str, Any]]
) -> None:
    """Параметризация тестов для различных возможных значений статуса."""
    assert filter_by_state(list_filter, state) == expected


def test_sort_by_date_by_default(
    list_of_events_2_test: list[dict[str, Any]], list_of_events_2_true: list[dict[str, Any]]
) -> None:
    """Тестирование сортировки списка словарей по датам без передачи дополнительного параметра (по возрастанию)."""
    assert sort_by_date(list_of_events_2_test) == list_of_events_2_true


def test_sort_by_date_down(
    list_of_events_2_test: list[dict[str, Any]], list_of_events_2_true: list[dict[str, Any]]
) -> None:
    """Тестирование сортировки списка словарей по датам по убыванию."""
    assert sort_by_date(list_of_events_2_test, True) == list_of_events_2_true


def test_sort_by_date_up(
    list_of_events_2_test: list[dict[str, Any]], list_of_events_2_false: list[dict[str, Any]]
) -> None:
    """Тестирование сортировки списка словарей по датам по возрастанию."""
    assert sort_by_date(list_of_events_2_test, False) == list_of_events_2_false


def test_sort_by_date_double_data(
    list_of_events_2_double_data: list[dict[str, Any]], list_of_events_2_double_data_test: list[dict[str, Any]]
) -> None:
    """Тестирование сортировки списка словарей по датам при одинаковой дате."""
    assert sort_by_date(list_of_events_2_double_data) == list_of_events_2_double_data_test


def test_sort_by_date_no_correct_data(list_of_events_2_no_correct_data: list[dict[str, Any]]) -> None:
    """Тестирование функции при неожидаемом типе данных"""
    with pytest.raises(TypeError):
        sort_by_date(list_of_events_2_no_correct_data)


def test_sort_by_date_no_data(list_of_events_2_no_data: list[dict[str, Any]]) -> None:
    """Тестирование функции при отсутствии даты"""
    with pytest.raises(ValueError):
        sort_by_date(list_of_events_2_no_data)


def test_sort_by_date_no_correct(list_of_events_2_no_correct: list[dict[str, Any]]) -> None:
    """Тест на работу функции с некорректным или нестандартным форматом дат"""
    assert sort_by_date(list_of_events_2_no_correct) == "Некорректный формат даты"
