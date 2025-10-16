import json
from unittest.mock import mock_open, patch

from src.utils import transactions_data  # Замените на ваш модуль


def test_file_not_found() -> None:
    """Тестирование случая, когда файл не существует"""
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = False

        result = transactions_data("nonexistent_file.json")

        mock_exists.assert_called_once_with("nonexistent_file.json")
        assert result == []


def test_empty_file() -> None:
    """Тестирование случая с пустым файлом"""
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data="")) as mock_file:
            result = transactions_data("empty_file.json")

            mock_exists.assert_called_once_with("empty_file.json")
            mock_file.assert_called_once_with("empty_file.json", "r", encoding="utf-8")
            assert result == []


def test_json_decode_error() -> None:
    """Тестирование ошибки декодирования JSON"""
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data="invalid json content")):
            result = transactions_data("invalid_json.json")

            mock_exists.assert_called_once_with("invalid_json.json")
            assert result == []


def test_file_not_list() -> None:
    """Тестирование случая, когда JSON не является списком"""
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
            result = transactions_data("not_list.json")

            mock_exists.assert_called_once_with("not_list.json")
            assert result == []


def test_successful_transaction_data() -> None:
    """Тестирование успешного чтения данных"""
    test_data = [{"id": 1, "amount": 100.0}, {"id": 2, "amount": 200.0}]

    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            result = transactions_data("valid_data.json")

            mock_exists.assert_called_once_with("valid_data.json")
            assert result == test_data
            assert isinstance(result, list)
            assert len(result) == 2


def test_file_with_whitespace_only() -> None:
    """Тестирование файла только с пробелами"""
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data="   \n   \t   ")):
            result = transactions_data("whitespace.json")

            mock_exists.assert_called_once_with("whitespace.json")
            assert result == []


def test_empty_list_in_file() -> None:
    """Тестирование файла с пустым списком"""
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data="[]")):
            result = transactions_data("empty_list.json")

            mock_exists.assert_called_once_with("empty_list.json")
            assert result == []


def test_valid_data_with_whitespace() -> None:
    """Тестирование валидных данных с окружающими пробелами"""
    test_data = [{"id": 1, "amount": 100.0}]

    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data=f"  {json.dumps(test_data)}  \n")):
            result = transactions_data("whitespace_around.json")

            mock_exists.assert_called_once_with("whitespace_around.json")
            assert result == test_data


def test_complex_data_structure() -> None:
    """Тестирование сложной структуры данных"""
    test_data = [{"id": 1, "amount": 100.50, "date": "2023-01-01", "category": "food"}]

    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            result = transactions_data("complex_data.json")

            mock_exists.assert_called_once_with("complex_data.json")
            assert result == test_data
            assert result[0]["category"] == "food"


def test_file_with_only_newlines() -> None:
    """Тестирование файла только с переносами строк"""
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data="\n\n\n")):
            result = transactions_data("newlines.json")

            mock_exists.assert_called_once_with("newlines.json")
            assert result == []


def test_special_characters_in_data() -> None:
    """Тестирование данных со специальными символами"""
    test_data = [{"description": "Café & restaurant", "amount": 50.0}]

    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            result = transactions_data("special_chars.json")

            mock_exists.assert_called_once_with("special_chars.json")
            assert result == test_data


def test_large_data_set() -> None:
    """Тестирование большого набора данных"""
    test_data = [{"id": i, "amount": i * 10.0} for i in range(10)]

    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            result = transactions_data("large_data.json")

            mock_exists.assert_called_once_with("large_data.json")
            assert result == test_data
            assert len(result) == 10


def test_file_path_with_spaces() -> None:
    """Тестирование пути файла с пробелами"""
    test_data = [{"test": "data"}]

    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            result = transactions_data("path with spaces.json")

            mock_exists.assert_called_once_with("path with spaces.json")
            assert result == test_data


def test_multiple_calls_same_function() -> None:
    """Тестирование множественных вызовов функции"""
    test_data1 = [{"id": 1}]
    test_data2 = [{"id": 2}]

    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True

        # Первый вызов
        with patch("builtins.open", mock_open(read_data=json.dumps(test_data1))):
            result1 = transactions_data("file1.json")
            assert result1 == test_data1

        # Второй вызов
        with patch("builtins.open", mock_open(read_data=json.dumps(test_data2))):
            result2 = transactions_data("file2.json")
            assert result2 == test_data2
