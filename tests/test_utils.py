import json
from unittest.mock import mock_open, patch

from src.utils import transactions_data  # Замените на ваш модуль


def test_successful_read_valid_data() -> None:
    """Тестирование успешного чтения данных"""
    test_data = [{"id": 1, "amount": 100.0}, {"id": 2, "amount": 200.0}]

    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
        result = transactions_data("valid_data.json")

        assert result == test_data


def test_file_not_found() -> None:
    """Тестирование случая, когда файл не существует"""
    with patch("builtins.open", side_effect=FileNotFoundError()):
        result = transactions_data("nonexistent_file.json")

        assert result == []


def test_empty_file() -> None:
    """Тестирование пустого файла"""
    with patch("builtins.open", mock_open(read_data="")):
        result = transactions_data("empty_file.json")

        assert result == []


def test_json_decode_error() -> None:
    """Тестирование ошибки декодирования JSON"""
    with patch("builtins.open", mock_open(read_data="invalid json content")):
        result = transactions_data("invalid_json.json")

        assert result == []


def test_file_not_list() -> None:
    """Тестирование случая, когда JSON не является списком"""
    with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
        result = transactions_data("not_list.json")

        assert result == []


def test_whitespace_only_file() -> None:
    """Тестирование файла только с пробелами"""
    with patch("builtins.open", mock_open(read_data="   \n   \t   ")):
        result = transactions_data("whitespace.json")

        assert result == []


def test_empty_list() -> None:
    """Тестирование файла с пустым списком"""
    with patch("builtins.open", mock_open(read_data="[]")):
        result = transactions_data("empty_list.json")

        assert result == []


def test_complex_data_structure() -> None:
    """Тестирование сложной структуры данных"""
    test_data = [
        {
            "id": 1,
            "date": "2023-01-01",
            "operationAmount": {"amount": "100.50", "currency": {"code": "USD"}},
            "description": "Payment",
            "from": "Account 1",
            "to": "Account 2",
        }
    ]

    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
        result = transactions_data("complex_data.json")

        assert result == test_data
        assert len(result) == 1
        assert result[0]["operationAmount"]["currency"]["code"] == "USD"


def test_file_with_only_newlines() -> None:
    """Тестирование файла только с переносами строк"""
    with patch("builtins.open", mock_open(read_data="\n\n\n")):
        result = transactions_data("newlines_only.json")

        assert result == []


def test_valid_data_with_whitespace() -> None:
    """Тестирование данных с окружающими пробелами"""
    test_data = [{"id": 1, "amount": 100.0}]

    with patch("builtins.open", mock_open(read_data=f"  {json.dumps(test_data)}  \n")):
        result = transactions_data("whitespace_around.json")

        assert result == test_data


def test_large_data_set() -> None:
    """Тестирование большого набора данных"""
    test_data = [{"id": i, "amount": i * 10.0} for i in range(100)]

    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
        result = transactions_data("large_data.json")

        assert result == test_data
        assert len(result) == 100
        assert result[-1]["id"] == 99


def test_general_exception() -> None:
    """Тестирование общего исключения"""
    with patch("builtins.open", side_effect=Exception("Some unexpected error")):
        result = transactions_data("error_file.json")

        assert result == []


def test_permission_error() -> None:
    """Тестирование ошибки прав доступа"""
    with patch("builtins.open", side_effect=PermissionError("Permission denied")):
        result = transactions_data("protected_file.json")

        assert result == []
