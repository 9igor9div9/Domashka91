import pytest

from unittest.mock import patch, mock_open
import pandas as pd
import logging

from tests.conftest import expected_data_table_csv, expected_data_table_xlsx
from src.utils_table import transactions_data_csv, transactions_data_xlsx


def test_transactions_data_csv_success(expected_data_table_csv: list[dict]) -> None:
    """Тест успешного чтения CSV файла"""
    with patch("pandas.read_csv") as mock_read_csv:
        # Настраиваем мок для pd.read_csv
        mock_read_csv.return_value = pd.DataFrame(expected_data_table_csv)

        # Вызываем тестируемую функцию
        result = transactions_data_csv("test_path.csv")

        # Проверяем, что pd.read_csv был вызван с правильными аргументами
        mock_read_csv.assert_called_once_with("test_path.csv", sep=";")

        # Проверяем результат
        assert result == expected_data_table_csv


def test_transactions_data_csv_file_not_found() -> None:
    """Тест обработки ошибки FileNotFoundError"""
    with patch("pandas.read_csv") as mock_read_csv:
        # Настраиваем мок для выброса FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError(f"Ошибка: файл не найден.")

        # Вызываем тестируемую функцию
        result = transactions_data_csv("nonexistent.csv")

        # Проверяем, что функция вернула пустой список
        assert result == []


def test_transactions_data_csv_empty_data() -> None:
    """Тест обработки пустого файла"""
    with patch("pandas.read_csv") as mock_read_csv:
        # Настраиваем мок для выброса EmptyDataError
        mock_read_csv.side_effect = pd.errors.EmptyDataError("Ошибка. Файл пуст")

        # Вызываем тестируемую функцию
        result = transactions_data_csv("empty.csv")

        # Проверяем, что функция вернула пустой список
        assert result == []


def test_transactions_data_csv_parser_error() -> None:
    """Тест обработки ошибки парсинга"""
    with patch("pandas.read_csv") as mock_read_csv:
        # Настраиваем мок для выброса ParserError
        mock_read_csv.side_effect = pd.errors.ParserError("Ошибка парсинга")

        # Вызываем тестируемую функцию
        result = transactions_data_csv("corrupted.csv")

        # Проверяем, что функция вернула пустой список
        assert result == []


def test_transactions_data_csv_unicode_error() -> None:
    """Тест обработки ошибки кодировки"""
    with patch("pandas.read_csv") as mock_read_csv:
        # Настраиваем мок для выброса UnicodeDecodeError
        mock_read_csv.side_effect = UnicodeDecodeError("utf-8", b"", 0, 1, "Неверная кодировка файла")

        # Вызываем тестируемую функцию
        result = transactions_data_csv("wrong_encoding.csv")

        # Проверяем, что функция вернула пустой список
        assert result == []


def test_transactions_data_csv_general_exception() -> None:
    """Тест обработки общей ошибки"""
    with patch("pandas.read_csv") as mock_read_csv:
        # Настраиваем мок для выброса общего исключения
        mock_read_csv.side_effect = Exception("Произошла ошибка")

        # Вызываем тестируемую функцию
        result = transactions_data_csv("problematic.csv")

        # Проверяем, что функция вернула пустой список
        assert result == []


def test_transactions_data_csv_logging() -> None:
    """Тест логирования при успешном выполнении"""
    with patch("pandas.read_csv") as mock_read_csv, \
            patch.object(logging.getLogger("utils"), "info") as mock_logger_info:
        # Настраиваем мок данные
        expected_data = [{"id": 1, "amount": 1000}]
        mock_read_csv.return_value = pd.DataFrame(expected_data)

        # Вызываем тестируемую функцию
        result = transactions_data_csv("test.csv")

        # Проверяем, что были вызваны логи
        mock_logger_info.assert_any_call("Начало работы функции")
        mock_logger_info.assert_any_call("Читаем CSV файл")
        mock_logger_info.assert_any_call("Работа функции завершилась успешно")


def test_transactions_data_csv_error_logging() -> None:
    """Тест логирования при ошибке"""
    with patch("pandas.read_csv") as mock_read_csv, \
            patch.object(logging.getLogger("utils"), "error") as mock_logger_error:
        # Настраиваем мок для выброса ошибки
        mock_read_csv.side_effect = FileNotFoundError("Ошибка: файл не найден")

        # Вызываем тестируемую функцию
        result = transactions_data_csv("nonexistent.csv")

        # Проверяем, что была записана ошибка в лог
        mock_logger_error.assert_called_once_with("Ошибка: файл 'nonexistent.csv' не найден.")


def test_transactions_data_xlsx_success(expected_data_table_xlsx: list[dict]) -> None:
    """Тест успешного чтения xlsx файла"""
    with patch("pandas.read_excel") as mock_read_excel:
        # Настраиваем мок для pd.read_xlsx
        mock_read_excel.return_value = pd.DataFrame(expected_data_table_xlsx)

        # Вызываем тестируемую функцию
        result = transactions_data_xlsx("test_path.xlsx")

        # Проверяем, что pd.read_csv был вызван с правильными аргументами
        mock_read_excel.assert_called_once_with("test_path.xlsx")

        # Проверяем результат
        assert result == expected_data_table_xlsx


def test_transactions_data_xlsx_file_not_found() -> None:
    """Тест обработки ошибки FileNotFoundError"""
    with patch("pandas.read_excel") as mock_read_excel:
        # Настраиваем мок для выброса FileNotFoundError
        mock_read_excel.side_effect = FileNotFoundError(f"Ошибка: файл не найден.")

        # Вызываем тестируемую функцию
        result = transactions_data_xlsx("nonexistent.xlsx")

        # Проверяем, что функция вернула пустой список
        assert result == []


def test_transactions_data_xlsx_empty_data() -> None:
    """Тест обработки пустого файла"""
    with patch("pandas.read_excel") as mock_read_excel:
        # Настраиваем мок для выброса EmptyDataError
        mock_read_excel.side_effect = pd.errors.EmptyDataError("Ошибка. Файл пуст")

        # Вызываем тестируемую функцию
        result = transactions_data_xlsx("empty.xlsx")

        # Проверяем, что функция вернула пустой список
        assert result == []


def test_transactions_data_xlsx_parser_error() -> None:
    """Тест обработки ошибки парсинга"""
    with patch("pandas.read_excel") as mock_read_excel:
        # Настраиваем мок для выброса ParserError
        mock_read_excel.side_effect = pd.errors.ParserError("Ошибка парсинга")

        # Вызываем тестируемую функцию
        result = transactions_data_xlsx("corrupted.xlsx")

        # Проверяем, что функция вернула пустой список
        assert result == []


def test_transactions_data_xlsx_unicode_error() -> None:
    """Тест обработки ошибки кодировки"""
    with patch("pandas.read_excel") as mock_read_excel:
        # Настраиваем мок для выброса UnicodeDecodeError
        mock_read_excel.side_effect = UnicodeDecodeError("utf-8", b"", 0, 1, "Неверная кодировка файла")

        # Вызываем тестируемую функцию
        result = transactions_data_xlsx("wrong_encoding.xlsx")

        # Проверяем, что функция вернула пустой список
        assert result == []


def test_transactions_data_xlsx_general_exception() -> None:
    """Тест обработки общей ошибки"""
    with patch("pandas.read_excel") as mock_read_excel:
        # Настраиваем мок для выброса общего исключения
        mock_read_excel.side_effect = Exception("Произошла ошибка")

        # Вызываем тестируемую функцию
        result = transactions_data_xlsx("problematic.xlsx")

        # Проверяем, что функция вернула пустой список
        assert result == []


def test_transactions_data_xlsx_logging() -> None:
    """Тест логирования при успешном выполнении"""
    with patch("pandas.read_excel") as mock_read_excel, \
            patch.object(logging.getLogger("utils"), "info") as mock_logger_info:
        # Настраиваем мок данные
        expected_data = [{"id": 1, "amount": 1000}]
        mock_read_excel.return_value = pd.DataFrame(expected_data)

        # Вызываем тестируемую функцию
        result = transactions_data_xlsx("test.xlsx")

        # Проверяем, что были вызваны логи
        mock_logger_info.assert_any_call("Начало работы функции")
        mock_logger_info.assert_any_call("Читаем xlsx файл")
        mock_logger_info.assert_any_call("Работа функции завершилась успешно")


def test_transactions_data_xlsx_error_logging() -> None:
    """Тест логирования при ошибке"""
    with patch("pandas.read_excel") as mock_read_excel, \
            patch.object(logging.getLogger("utils"), "error") as mock_logger_error:
        # Настраиваем мок для выброса ошибки
        mock_read_excel.side_effect = FileNotFoundError("Ошибка: файл не найден")

        # Вызываем тестируемую функцию
        result = transactions_data_xlsx("nonexistent.xlsx")

        # Проверяем, что была записана ошибка в лог
        mock_logger_error.assert_called_once_with("Ошибка: файл 'nonexistent.xlsx' не найден.")
