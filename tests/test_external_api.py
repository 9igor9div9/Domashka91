from unittest.mock import Mock, patch

import requests

from src.external_api import amount_transactions_rur  # Замените на ваш модуль


def test_rub_transaction() -> None:
    """Тестирование транзакции в рублях"""
    transaction = {"operationAmount": {"amount": "1000.50", "currency": {"code": "RUB"}}}

    result = amount_transactions_rur(transaction)
    assert result == 1000.50


def test_usd_transaction_success() -> None:
    """Тестирование успешной конвертации USD в RUB"""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"success": True, "result": 7500.50}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = amount_transactions_rur(transaction)

        assert result == 7500.50
        mock_get.assert_called_once()


def test_api_error() -> None:
    """Тестирование ошибки API"""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout("Timeout error")

        try:
            amount_transactions_rur(transaction)
            assert False, "Должно было выбросить исключение 'Таймаут запроса к API превышен'"
        except requests.exceptions.RequestException:
            assert True


def test_invalid_transaction_structure() -> None:
    """Тестирование некорректной структуры"""
    try:
        amount_transactions_rur("not_a_dict")
        assert False, "Должно было выбросить исключение"
    except ValueError:
        assert True


def test_invalid_amount() -> None:
    """Тестирование некорректной суммы"""
    transaction = {"operationAmount": {"amount": "not_a_number", "currency": {"code": "USD"}}}

    try:
        amount_transactions_rur(transaction)
        assert False, "Должно было выбросить исключение"
    except ValueError:
        assert True


def test_invalid_currency_code() -> None:
    """Тестирование некорректного кода валюты"""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "US"}}}  # слишком короткий

    try:
        amount_transactions_rur(transaction)
        assert False, "Должно было выбросить исключение"
    except ValueError:
        assert True


def test_api_failed_response() -> None:
    """Тестирование неудачного ответа API"""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"success": False}  # API вернул ошибку
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        try:
            amount_transactions_rur(transaction)
            assert False, "Должно было выбросить исключение"
        except ValueError:
            assert True


def test_negative_amount() -> None:
    """Тестирование отрицательной суммы"""
    transaction = {"operationAmount": {"amount": "-100.00", "currency": {"code": "USD"}}}

    try:
        amount_transactions_rur(transaction)
        assert False, "Должно было выбросить исключение"
    except ValueError as e:
        assert "Сумма не может быть отрицательной" in str(e)


def test_api_missing_result_field() -> None:
    """Тестирование отсутствия поля result в ответе API"""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {
            "success": True
            # Нет поля 'result'
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        try:
            amount_transactions_rur(transaction)
            assert False, "Должно было выбросить исключение"
        except ValueError as e:
            assert "Ошибка в ответе API" in str(e)


def test_api_invalid_json_response() -> None:
    """Тестирование некорректного JSON в ответе"""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        try:
            amount_transactions_rur(transaction)
            assert False, "Должно было выбросить исключение"
        except ValueError as e:
            assert "Некорректный ответ API" in str(e)


def test_http_exception() -> None:
    """Тестирование HTTP исключения"""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("401 Unauthorized")
        mock_get.return_value = mock_response

        try:
            amount_transactions_rur(transaction)
            assert False, "Должно было выбросить исключение"
        except requests.exceptions.RequestException as e:
            assert "Ошибка API" in str(e)


def test_missing_api_key() -> None:
    """Тестирование отсутствия API ключа"""
    # Временно подменяем api_key на None
    with patch("src.external_api.api_key", None):
        transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

        try:
            amount_transactions_rur(transaction)
            assert False, "Должно было выбросить исключение"
        except ValueError as e:
            assert "API ключ не найден" in str(e)
