from unittest.mock import patch

from main import (main, user_filter, user_filter_currency, user_filter_word, user_input, user_sorted_date,
                  user_sorted_up_to_down)


def test_user_input_json_file() -> None:
    """
    Тест выбора JSON-файла (ввод "1")(def user_input)
    """
    # Подготовка
    test_data = [{"id": 1, "amount": 100}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.transactions_data") as mock_transactions,
    ):
        # Настраиваем моки
        mock_input.return_value = "1"
        mock_transactions.return_value = test_data

        # Выполнение
        result = user_input()

        # Проверка
        mock_input.assert_called_once_with("Введите 1, 2 или 3:")
        mock_print.assert_called_once_with("Для обработки выбран JSON-файл.\n")
        mock_transactions.assert_called_once()
        assert result == test_data


def test_user_input_csv_file() -> None:
    """
    Тест выбора CSV-файла (ввод "2")(def user_input)
    """
    # Подготовка
    test_data = [{"id": 2, "amount": 200}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.transactions_data_csv") as mock_csv,
    ):
        # Настраиваем моки
        mock_input.return_value = "2"
        mock_csv.return_value = test_data

        # Выполнение
        result = user_input()

        # Проверка
        mock_input.assert_called_once_with("Введите 1, 2 или 3:")
        mock_print.assert_called_once_with("Для обработки выбран CSV-файл.\n")
        mock_csv.assert_called_once()
        assert result == test_data


def test_user_input_xlsx_file() -> None:
    """
    Тест выбора XLSX-файла (ввод "3")(def user_input)
    """
    # Подготовка
    test_data = [{"id": 3, "amount": 300}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.transactions_data_xlsx") as mock_xlsx,
    ):
        # Настраиваем моки
        mock_input.return_value = "3"
        mock_xlsx.return_value = test_data

        # Выполнение
        result = user_input()

        # Проверка
        mock_input.assert_called_once_with("Введите 1, 2 или 3:")
        mock_print.assert_called_once_with("Для обработки выбран XLSX-файл.\n")
        mock_xlsx.assert_called_once()
        assert result == test_data


def test_user_input_invalid_then_valid() -> None:
    """
    Тест неверного ввода с последующим корректным вводом(def user_input)
    """
    # Подготовка
    test_data = [{"id": 1, "amount": 100}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.transactions_data") as mock_transactions,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["5", "1"]  # Сначала неверный, потом верный ввод
        mock_transactions.return_value = test_data

        # Выполнение
        result = user_input()

        # Проверка
        assert mock_input.call_count == 2
        assert mock_input.call_args_list[0][0][0] == "Введите 1, 2 или 3:"
        assert mock_input.call_args_list[1][0][0] == "Введите 1, 2 или 3:"

        # Проверяем сообщение об ошибке
        mock_print.assert_any_call("Такого пункта нет.")
        mock_print.assert_any_call("Для обработки выбран JSON-файл.\n")

        mock_transactions.assert_called_once()
        assert result == test_data


def test_user_input_exception_in_transactions_data() -> None:
    """
    Тест обработки исключения в функции загрузки JSON(def user_input)
    """
    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.transactions_data") as mock_transactions,
    ):
        # Настраиваем моки
        mock_input.return_value = "1"
        mock_transactions.side_effect = FileNotFoundError("Файл не найден")

        # Выполнение
        result = user_input()

        # Проверка
        mock_input.assert_called_once_with("Введите 1, 2 или 3:")
        mock_print.assert_any_call("Для обработки выбран JSON-файл.\n")
        mock_print.assert_any_call("Ошибка: Файл не найден")
        assert result is None


def test_user_input_exception_in_transactions_data_csv() -> None:
    """
    Тест обработки исключения в функции загрузки CSV(def user_input)
    """
    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.transactions_data_csv") as mock_csv,
    ):
        # Настраиваем моки
        mock_input.return_value = "2"
        mock_csv.side_effect = PermissionError("Нет прав доступа")

        # Выполнение
        result = user_input()

        # Проверка
        mock_input.assert_called_once_with("Введите 1, 2 или 3:")
        mock_print.assert_any_call("Для обработки выбран CSV-файл.\n")
        mock_print.assert_any_call("Ошибка: Нет прав доступа")
        assert result is None


def test_user_input_general_exception() -> None:
    """
    Тест общего исключения(def user_input)
    """
    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.transactions_data") as mock_transactions,
    ):
        # Настраиваем моки
        mock_input.return_value = "1"
        mock_transactions.side_effect = Exception("Неизвестная ошибка")

        # Выполнение
        result = user_input()

        # Проверка
        mock_input.assert_called_once_with("Введите 1, 2 или 3:")
        mock_print.assert_any_call("Для обработки выбран JSON-файл.\n")
        mock_print.assert_any_call("Ошибка: Неизвестная ошибка")
        assert result is None


def test_user_filter_executed_status() -> None:
    """
    Тест фильтрации по статусу EXECUTED(def user_filter)
    """
    # Подготовка
    transactions = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}, {"id": 3, "state": "PENDING"}]
    expected_result = [{"id": 1, "state": "EXECUTED"}]

    with (
        patch("builtins.input") as mock_input,
        patch("main.filter_by_state") as mock_filter,
    ):
        # Настраиваем моки
        mock_input.return_value = "EXECUTED"
        mock_filter.return_value = expected_result

        # Выполнение
        result = user_filter(transactions)

        # Проверка
        mock_input.assert_called_once_with(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING."
        )
        mock_filter.assert_called_once_with(transactions, "EXECUTED")
        assert result == expected_result


def test_user_filter_canceled_status() -> None:
    """
    Тест фильтрации по статусу CANCELED(def user_filter)
    """
    # Подготовка
    transactions = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}, {"id": 3, "state": "CANCELED"}]
    expected_result = [{"id": 2, "state": "CANCELED"}, {"id": 3, "state": "CANCELED"}]

    with (
        patch("builtins.input") as mock_input,
        patch("main.filter_by_state") as mock_filter,
    ):
        # Настраиваем моки
        mock_input.return_value = "CANCELED"
        mock_filter.return_value = expected_result

        # Выполнение
        result = user_filter(transactions)

        # Проверка
        mock_filter.assert_called_once_with(transactions, "CANCELED")
        assert result == expected_result


def test_user_filter_pending_status() -> None:
    """
    Тест фильтрации по статусу PENDING(def user_filter)
    """
    # Подготовка
    transactions = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}, {"id": 3, "state": "PENDING"}]
    expected_result = [{"id": 2, "state": "PENDING"}, {"id": 3, "state": "PENDING"}]

    with (
        patch("builtins.input") as mock_input,
        patch("main.filter_by_state") as mock_filter,
    ):
        # Настраиваем моки
        mock_input.return_value = "PENDING"
        mock_filter.return_value = expected_result

        # Выполнение
        result = user_filter(transactions)

        # Проверка
        mock_filter.assert_called_once_with(transactions, "PENDING")
        assert result == expected_result


def test_user_filter_lowercase_input() -> None:
    """
    Тест ввода статуса в нижнем регистре(def user_filter)
    """
    # Подготовка
    transactions = [{"id": 1, "state": "EXECUTED"}]
    expected_result = [{"id": 1, "state": "EXECUTED"}]

    with (
        patch("builtins.input") as mock_input,
        patch("main.filter_by_state") as mock_filter,
    ):
        # Настраиваем моки
        mock_input.return_value = "executed"
        mock_filter.return_value = expected_result

        # Выполнение
        result = user_filter(transactions)

        # Проверка
        mock_filter.assert_called_once_with(transactions, "EXECUTED")
        assert result == expected_result


def test_user_filter_invalid_then_valid_status() -> None:
    """
    Тест неверного ввода с последующим корректным вводом(def user_filter)
    """
    # Подготовка
    transactions = [{"id": 1, "state": "EXECUTED"}]
    expected_result = [{"id": 1, "state": "EXECUTED"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_state") as mock_filter,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["INVALID", "EXECUTED"]
        mock_filter.return_value = expected_result

        # Выполнение
        result = user_filter(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_print.assert_any_call("Статус операции 'INVALID' недоступен.")
        mock_filter.assert_called_once_with(transactions, "EXECUTED")
        assert result == expected_result


def test_user_filter_empty_transactions() -> None:
    """
    Тест фильтрации пустого списка транзакций(def user_filter)
    """
    # Подготовка
    transactions = []
    expected_result = []

    with (
        patch("builtins.input") as mock_input,
        patch("main.filter_by_state") as mock_filter,
    ):
        # Настраиваем моки
        mock_input.return_value = "EXECUTED"
        mock_filter.return_value = expected_result

        # Выполнение
        result = user_filter(transactions)

        # Проверка
        mock_filter.assert_called_once_with(transactions, "EXECUTED")
        assert result == expected_result


def test_user_filter_general_exception() -> None:
    """
    Тест общего исключения(def user_filter)
    """
    # Подготовка
    transactions = [{"id": 1, "state": "EXECUTED"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_state") as mock_filter,
    ):
        # Настраиваем моки
        mock_input.return_value = "EXECUTED"
        mock_filter.side_effect = Exception("Something went wrong")

        # Выполнение
        result = user_filter(transactions)

        # Проверка
        mock_filter.assert_called_once_with(transactions, "EXECUTED")
        mock_print.assert_any_call("Ошибка: Something went wrong")
        assert result is None


def test_user_filter_partial_status_name() -> None:
    """
    Тест ввода частичного названия статуса(def user_filter)
    """
    # Подготовка
    transactions = [{"id": 1, "state": "EXECUTED"}]
    expected_result = [{"id": 1, "state": "EXECUTED"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_state") as mock_filter,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["EXEC", "EXECUTED"]
        mock_filter.return_value = expected_result

        # Выполнение
        result = user_filter(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_print.assert_any_call("Статус операции 'EXEC' недоступен.")
        mock_filter.assert_called_once_with(transactions, "EXECUTED")
        assert result == expected_result


def test_user_sorted_ascending_lowercase() -> None:
    """
    Тест выбора сортировки по возрастанию (нижний регистр)(def user_sorted_up_to_down)
    """
    with patch("builtins.input") as mock_input, patch("builtins.print") as mock_print:
        # Настраиваем моки
        mock_input.return_value = "по возрастанию"

        # Выполнение
        result = user_sorted_up_to_down()

        # Проверка
        mock_input.assert_called_once_with("Отсортировать по возрастанию или по убыванию?")
        assert result is False
        mock_print.assert_not_called()


def test_user_sorted_ascending_uppercase() -> None:
    """
    Тест выбора сортировки по возрастанию (верхний регистр)(def user_sorted_up_to_down)
    """
    with patch("builtins.input") as mock_input, patch("builtins.print") as mock_print:
        # Настраиваем моки
        mock_input.return_value = "ПО ВОЗРАСТАНИЮ"

        # Выполнение
        result = user_sorted_up_to_down()

        # Проверка
        mock_input.assert_called_once_with("Отсортировать по возрастанию или по убыванию?")
        assert result is False
        mock_print.assert_not_called()


def test_user_sorted_descending_lowercase() -> None:
    """
    Тест выбора сортировки по убыванию (нижний регистр)(def user_sorted_up_to_down)
    """
    with patch("builtins.input") as mock_input, patch("builtins.print") as mock_print:
        # Настраиваем моки
        mock_input.return_value = "по убыванию"

        # Выполнение
        result = user_sorted_up_to_down()

        # Проверка
        mock_input.assert_called_once_with("Отсортировать по возрастанию или по убыванию?")
        assert result is True
        mock_print.assert_not_called()


def test_user_sorted_descending_uppercase() -> None:
    """
    Тест выбора сортировки по убыванию (верхний регистр)(def user_sorted_up_to_down)
    """
    with patch("builtins.input") as mock_input, patch("builtins.print") as mock_print:
        # Настраиваем моки
        mock_input.return_value = "ПО УБЫВАНИЮ"

        # Выполнение
        result = user_sorted_up_to_down()

        # Проверка
        mock_input.assert_called_once_with("Отсортировать по возрастанию или по убыванию?")
        assert result is True
        mock_print.assert_not_called()


def test_user_sorted_invalid_then_valid_ascending() -> None:
    """
    Тест неверного ввода с последующим корректным вводом (по возрастанию)(def user_sorted_up_to_down)
    """
    with patch("builtins.input") as mock_input, patch("builtins.print") as mock_print:
        # Настраиваем моки
        mock_input.side_effect = ["неправильно", "по возрастанию"]

        # Выполнение
        result = user_sorted_up_to_down()

        # Проверка
        assert mock_input.call_count == 2
        mock_print.assert_called_once_with("Такого пункта нет.")
        assert result is False


def test_user_sorted_invalid_then_valid_descending() -> None:
    """
    Тест неверного ввода с последующим корректным вводом (по убыванию)(def user_sorted_up_to_down)
    """
    with patch("builtins.input") as mock_input, patch("builtins.print") as mock_print:
        # Настраиваем моки
        mock_input.side_effect = ["abc", "по убыванию"]

        # Выполнение
        result = user_sorted_up_to_down()

        # Проверка
        assert mock_input.call_count == 2
        mock_print.assert_called_once_with("Такого пункта нет.")
        assert result is True


def test_user_sorted_empty_input() -> None:
    """
    Тест пустого ввода(def user_sorted_up_to_down)
    """
    with patch("builtins.input") as mock_input, patch("builtins.print") as mock_print:
        # Настраиваем моки
        mock_input.side_effect = ["", "по убыванию"]

        # Выполнение
        result = user_sorted_up_to_down()

        # Проверка
        assert mock_input.call_count == 2
        mock_print.assert_called_once_with("Такого пункта нет.")
        assert result is True


def test_user_sorted_general_exception() -> None:
    """
    Тест общего исключения(def user_sorted_up_to_down)
    """
    with patch("builtins.input") as mock_input, patch("builtins.print") as mock_print:
        # Настраиваем моки
        mock_input.side_effect = Exception("Произошла ошибка")

        # Выполнение
        result = user_sorted_up_to_down()

        # Проверка
        mock_input.assert_called_once_with("Отсортировать по возрастанию или по убыванию?")
        mock_print.assert_called_once_with("Ошибка: Произошла ошибка")
        assert result is None


def test_user_sorted_value_error() -> None:
    """
    Тест исключения ValueError(def user_sorted_up_to_down)
    """
    with patch("builtins.input") as mock_input, patch("builtins.print") as mock_print:
        # Настраиваем моки
        mock_input.side_effect = ValueError("Неверное значение")

        # Выполнение
        result = user_sorted_up_to_down()

        # Проверка
        mock_input.assert_called_once_with("Отсортировать по возрастанию или по убыванию?")
        mock_print.assert_called_once_with("Ошибка: Неверное значение")
        assert result is None


def test_user_sorted_date_yes_lowercase() -> None:
    """
    Тест выбора сортировки по дате (да, нижний регистр)(def user_sorted_date)
    """
    # Подготовка
    transactions = [{"id": 1, "date": "2023-01-01"}, {"id": 2, "date": "2023-01-02"}]
    sorted_transactions = [{"id": 2, "date": "2023-01-02"}, {"id": 1, "date": "2023-01-01"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.user_sorted_up_to_down") as mock_sorted_up_down,
        patch("main.sort_by_date") as mock_sort_by_date,
    ):
        # Настраиваем моки
        mock_input.return_value = "да"
        mock_sorted_up_down.return_value = True  # по убыванию
        mock_sort_by_date.return_value = sorted_transactions

        # Выполнение
        result = user_sorted_date(transactions)

        # Проверка
        mock_input.assert_called_once_with("Отсортировать операции по дате? Да/Нет")
        mock_sorted_up_down.assert_called_once()
        mock_sort_by_date.assert_called_once_with(transactions, True)
        assert result == sorted_transactions
        mock_print.assert_not_called()


def test_user_sorted_date_yes_uppercase() -> None:
    """
    Тест выбора сортировки по дате (ДА, верхний регистр)(def user_sorted_date)
    """
    # Подготовка
    transactions = [{"id": 1, "date": "2023-01-01"}]
    sorted_transactions = [{"id": 1, "date": "2023-01-01"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.user_sorted_up_to_down") as mock_sorted_up_down,
        patch("main.sort_by_date") as mock_sort_by_date,
    ):
        # Настраиваем моки
        mock_input.return_value = "ДА"
        mock_sorted_up_down.return_value = False  # по возрастанию
        mock_sort_by_date.return_value = sorted_transactions

        # Выполнение
        result = user_sorted_date(transactions)

        # Проверка
        mock_input.assert_called_once_with("Отсортировать операции по дате? Да/Нет")
        mock_sorted_up_down.assert_called_once()
        mock_sort_by_date.assert_called_once_with(transactions, False)
        assert result == sorted_transactions
        mock_print.assert_not_called()


def test_user_sorted_date_no_lowercase() -> None:
    """
    Тест отказа от сортировки по дате (нет, нижний регистр)(def user_sorted_date)
    """
    # Подготовка
    transactions = [{"id": 1, "date": "2023-01-01"}, {"id": 2, "date": "2023-01-02"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.user_sorted_up_to_down") as mock_sorted_up_down,
        patch("main.sort_by_date") as mock_sort_by_date,
    ):
        # Настраиваем моки
        mock_input.return_value = "нет"

        # Выполнение
        result = user_sorted_date(transactions)

        # Проверка
        mock_input.assert_called_once_with("Отсортировать операции по дате? Да/Нет")
        mock_sorted_up_down.assert_not_called()
        mock_sort_by_date.assert_not_called()
        assert result == transactions
        mock_print.assert_not_called()


def test_user_sorted_date_no_uppercase() -> None:
    """
    Тест отказа от сортировки по дате (НЕТ, верхний регистр)(def user_sorted_date)
    """
    # Подготовка
    transactions = [{"id": 1, "date": "2023-01-01"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.user_sorted_up_to_down") as mock_sorted_up_down,
        patch("main.sort_by_date") as mock_sort_by_date,
    ):
        # Настраиваем моки
        mock_input.return_value = "НЕТ"

        # Выполнение
        result = user_sorted_date(transactions)

        # Проверка
        mock_input.assert_called_once_with("Отсортировать операции по дате? Да/Нет")
        mock_sorted_up_down.assert_not_called()
        mock_sort_by_date.assert_not_called()
        assert result == transactions
        mock_print.assert_not_called()


def test_user_sorted_date_invalid_then_valid_yes() -> None:
    """
    Тест неверного ввода с последующим корректным вводом (да)(def user_sorted_date)
    """
    # Подготовка
    transactions = [{"id": 1, "date": "2023-01-01"}]
    sorted_transactions = [{"id": 1, "date": "2023-01-01"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.user_sorted_up_to_down") as mock_sorted_up_down,
        patch("main.sort_by_date") as mock_sort_by_date,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["может быть", "да"]
        mock_sorted_up_down.return_value = False
        mock_sort_by_date.return_value = sorted_transactions

        # Выполнение
        result = user_sorted_date(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_print.assert_called_once_with("Такого пункта нет.")
        mock_sorted_up_down.assert_called_once()
        mock_sort_by_date.assert_called_once_with(transactions, False)
        assert result == sorted_transactions


def test_user_sorted_date_invalid_then_valid_no() -> None:
    """
    Тест неверного ввода с последующим корректным вводом (нет)(def user_sorted_date)
    """
    # Подготовка
    transactions = [{"id": 1, "date": "2023-01-01"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.user_sorted_up_to_down") as mock_sorted_up_down,
        patch("main.sort_by_date") as mock_sort_by_date,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["y", "нет"]

        # Выполнение
        result = user_sorted_date(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_print.assert_called_once_with("Такого пункта нет.")
        mock_sorted_up_down.assert_not_called()
        mock_sort_by_date.assert_not_called()
        assert result == transactions


def test_user_sorted_date_yes_with_exception_in_user_sorted_up_to_down() -> None:
    """
    Тест исключения в функции user_sorted_up_to_down(def user_sorted_date)
    """
    # Подготовка
    transactions = [{"id": 1, "date": "2023-01-01"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.user_sorted_up_to_down") as mock_sorted_up_down,
        patch("main.sort_by_date") as mock_sort_by_date,
    ):
        # Настраиваем моки
        mock_input.return_value = "да"
        mock_sorted_up_down.side_effect = ValueError("Ошибка в выборе порядка сортировки")

        # Выполнение
        result = user_sorted_date(transactions)

        # Проверка
        mock_input.assert_called_once_with("Отсортировать операции по дате? Да/Нет")
        mock_sorted_up_down.assert_called_once()
        mock_sort_by_date.assert_not_called()
        mock_print.assert_called_once_with("Ошибка: Ошибка в выборе порядка сортировки")
        assert result is None


def test_user_sorted_date_yes_with_exception_in_sort_by_date() -> None:
    """
    Тест исключения в функции sort_by_date(def user_sorted_date)
    """
    # Подготовка
    transactions = [{"id": 1, "date": "2023-01-01"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.user_sorted_up_to_down") as mock_sorted_up_down,
        patch("main.sort_by_date") as mock_sort_by_date,
    ):
        # Настраиваем моки
        mock_input.return_value = "да"
        mock_sorted_up_down.return_value = True
        mock_sort_by_date.side_effect = Exception("Ошибка при сортировке")

        # Выполнение
        result = user_sorted_date(transactions)

        # Проверка
        mock_input.assert_called_once_with("Отсортировать операции по дате? Да/Нет")
        mock_sorted_up_down.assert_called_once()
        mock_sort_by_date.assert_called_once_with(transactions, True)
        mock_print.assert_called_once_with("Ошибка: Ошибка при сортировке")
        assert result is None


def test_user_sorted_date_empty_transactions() -> None:
    """
    Тест с пустым списком транзакций(def user_sorted_date)
    """
    # Подготовка
    transactions = []

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.user_sorted_up_to_down") as mock_sorted_up_down,
        patch("main.sort_by_date") as mock_sort_by_date,
    ):
        # Настраиваем моки
        mock_input.return_value = "да"
        mock_sorted_up_down.return_value = True
        mock_sort_by_date.return_value = []

        # Выполнение
        result = user_sorted_date(transactions)

        # Проверка
        mock_input.assert_called_once_with("Отсортировать операции по дате? Да/Нет")
        mock_sorted_up_down.assert_called_once()
        mock_sort_by_date.assert_called_once_with([], True)
        assert result == []
        mock_print.assert_not_called()


def test_user_sorted_date_none_transactions() -> None:
    """
    Тест с None вместо списка транзакций(def user_sorted_date)
    """
    # Подготовка
    transactions = None

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.user_sorted_up_to_down") as mock_sorted_up_down,
        patch("main.sort_by_date") as mock_sort_by_date,
    ):
        # Настраиваем моки
        mock_input.return_value = "да"
        mock_sorted_up_down.return_value = True
        mock_sort_by_date.side_effect = TypeError("'NoneType' object is not iterable")

        # Выполнение
        result = user_sorted_date(transactions)

        # Проверка
        mock_input.assert_called_once_with("Отсортировать операции по дате? Да/Нет")
        mock_sorted_up_down.assert_called_once()
        mock_sort_by_date.assert_called_once_with(None, True)
        mock_print.assert_called_once_with("Ошибка: 'NoneType' object is not iterable")
        assert result is None


def test_user_filter_currency_yes_lowercase() -> None:
    """
    Тест выбора фильтрации по валюте (да, нижний регистр)(def user_filter_currency)
    """
    # Подготовка
    transactions = [{"id": 1, "currency": "RUB"}, {"id": 2, "currency": "USD"}, {"id": 3, "currency": "RUB"}]
    filtered_transactions = [{"id": 1, "currency": "RUB"}, {"id": 3, "currency": "RUB"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_currency") as mock_filter_by_currency,
    ):
        # Настраиваем моки
        mock_input.return_value = "да"
        mock_filter_by_currency.return_value = filtered_transactions

        # Выполнение
        result = user_filter_currency(transactions)

        # Проверка
        mock_input.assert_called_once_with("Выводить только рублевые транзакции? Да/Нет")
        mock_filter_by_currency.assert_called_once_with(transactions, "RUB")
        assert result == filtered_transactions
        mock_print.assert_not_called()


def test_user_filter_currency_yes_uppercase() -> None:
    """
    Тест выбора фильтрации по валюте (ДА, верхний регистр)(def user_filter_currency)
    """
    # Подготовка
    transactions = [{"id": 1, "currency": "RUB"}, {"id": 2, "currency": "EUR"}]
    filtered_transactions = [{"id": 1, "currency": "RUB"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_currency") as mock_filter_by_currency,
    ):
        # Настраиваем моки
        mock_input.return_value = "ДА"
        mock_filter_by_currency.return_value = filtered_transactions

        # Выполнение
        result = user_filter_currency(transactions)

        # Проверка
        mock_input.assert_called_once_with("Выводить только рублевые транзакции? Да/Нет")
        mock_filter_by_currency.assert_called_once_with(transactions, "RUB")
        assert result == filtered_transactions
        mock_print.assert_not_called()


def test_user_filter_currency_no_lowercase() -> None:
    """
    Тест отказа от фильтрации по валюте (нет, нижний регистр)(def user_filter_currency)
    """
    # Подготовка
    transactions = [{"id": 1, "currency": "RUB"}, {"id": 2, "currency": "USD"}, {"id": 3, "currency": "EUR"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_currency") as mock_filter_by_currency,
    ):
        # Настраиваем моки
        mock_input.return_value = "нет"

        # Выполнение
        result = user_filter_currency(transactions)

        # Проверка
        mock_input.assert_called_once_with("Выводить только рублевые транзакции? Да/Нет")
        mock_filter_by_currency.assert_not_called()
        assert result == transactions
        mock_print.assert_not_called()


def test_user_filter_currency_no_uppercase() -> None:
    """
    Тест отказа от фильтрации по валюте (НЕТ, верхний регистр)(def user_filter_currency)
    """
    # Подготовка
    transactions = [{"id": 1, "currency": "RUB"}, {"id": 2, "currency": "USD"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_currency") as mock_filter_by_currency,
    ):
        # Настраиваем моки
        mock_input.return_value = "НЕТ"

        # Выполнение
        result = user_filter_currency(transactions)

        # Проверка
        mock_input.assert_called_once_with("Выводить только рублевые транзакции? Да/Нет")
        mock_filter_by_currency.assert_not_called()
        assert result == transactions
        mock_print.assert_not_called()


def test_user_filter_currency_invalid_then_valid_yes() -> None:
    """
    Тест неверного ввода с последующим корректным вводом (да)(def user_filter_currency)
    """
    # Подготовка
    transactions = [{"id": 1, "currency": "RUB"}, {"id": 2, "currency": "USD"}]
    filtered_transactions = [{"id": 1, "currency": "RUB"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_currency") as mock_filter_by_currency,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["может быть", "да"]
        mock_filter_by_currency.return_value = filtered_transactions

        # Выполнение
        result = user_filter_currency(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_print.assert_called_once_with("Такого пункта нет.")
        mock_filter_by_currency.assert_called_once_with(transactions, "RUB")
        assert result == filtered_transactions


def test_user_filter_currency_invalid_then_valid_no() -> None:
    """
    Тест неверного ввода с последующим корректным вводом (нет)(def user_filter_currency)
    """
    # Подготовка
    transactions = [{"id": 1, "currency": "RUB"}, {"id": 2, "currency": "USD"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_currency") as mock_filter_by_currency,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["y", "нет"]

        # Выполнение
        result = user_filter_currency(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_print.assert_called_once_with("Такого пункта нет.")
        mock_filter_by_currency.assert_not_called()
        assert result == transactions


def test_user_filter_currency_empty_transactions() -> None:
    """
    Тест с пустым списком транзакций(def user_filter_currency)
    """
    # Подготовка
    transactions = []
    filtered_transactions = []

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_currency") as mock_filter_by_currency,
    ):
        # Настраиваем моки
        mock_input.return_value = "да"
        mock_filter_by_currency.return_value = filtered_transactions

        # Выполнение
        result = user_filter_currency(transactions)

        # Проверка
        mock_input.assert_called_once_with("Выводить только рублевые транзакции? Да/Нет")
        mock_filter_by_currency.assert_called_once_with([], "RUB")
        assert result == filtered_transactions
        mock_print.assert_not_called()


def test_user_filter_currency_none_transactions() -> None:
    """
    Тест с None вместо списка транзакций(def user_filter_currency)
    """
    # Подготовка
    transactions = None

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_currency") as mock_filter_by_currency,
    ):
        # Настраиваем моки
        mock_input.return_value = "да"
        mock_filter_by_currency.side_effect = TypeError("'NoneType' object is not iterable")

        # Выполнение
        result = user_filter_currency(transactions)

        # Проверка
        mock_input.assert_called_once_with("Выводить только рублевые транзакции? Да/Нет")
        mock_filter_by_currency.assert_called_once_with(None, "RUB")
        mock_print.assert_called_once_with("Ошибка: 'NoneType' object is not iterable")
        assert result is None


def test_user_filter_currency_no_rub_transactions() -> None:
    """
    Тест фильтрации, когда нет рублевых транзакций(def user_filter_currency)
    """
    # Подготовка
    transactions = [{"id": 1, "currency": "USD"}, {"id": 2, "currency": "EUR"}, {"id": 3, "currency": "GBP"}]
    filtered_transactions = []

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_currency") as mock_filter_by_currency,
    ):
        # Настраиваем моки
        mock_input.return_value = "да"
        mock_filter_by_currency.return_value = filtered_transactions

        # Выполнение
        result = user_filter_currency(transactions)

        # Проверка
        mock_input.assert_called_once_with("Выводить только рублевые транзакции? Да/Нет")
        mock_filter_by_currency.assert_called_once_with(transactions, "RUB")
        assert result == filtered_transactions
        mock_print.assert_not_called()


def test_user_filter_currency_all_rub_transactions() -> None:
    """
    Тест фильтрации, когда все транзакции рублевые(def user_filter_currency)
    """
    # Подготовка
    transactions = [{"id": 1, "currency": "RUB"}, {"id": 2, "currency": "RUB"}, {"id": 3, "currency": "RUB"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.filter_by_currency") as mock_filter_by_currency,
    ):
        # Настраиваем моки
        mock_input.return_value = "да"
        mock_filter_by_currency.return_value = transactions

        # Выполнение
        result = user_filter_currency(transactions)

        # Проверка
        mock_input.assert_called_once_with("Выводить только рублевые транзакции? Да/Нет")
        mock_filter_by_currency.assert_called_once_with(transactions, "RUB")
        assert result == transactions
        mock_print.assert_not_called()


def test_user_filter_word_yes_lowercase() -> None:
    """
    Тест выбора фильтрации по слову (да, нижний регистр)(def user_filter_word)
    """
    # Подготовка
    transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Оплата услуг"},
    ]
    filtered_transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
    ]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["да", "Перевод"]
        mock_process_bank_search.return_value = filtered_transactions

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_input.assert_any_call("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        mock_input.assert_any_call("Введите слово:")
        mock_process_bank_search.assert_called_once_with(transactions, "Перевод")
        assert result == filtered_transactions
        mock_print.assert_not_called()


def test_user_filter_word_yes_uppercase() -> None:
    """
    Тест выбора фильтрации по слову (ДА, верхний регистр)(def user_filter_word)
    """
    # Подготовка
    transactions = [{"id": 1, "description": "Оплата услуг"}, {"id": 2, "description": "Оплата товаров"}]
    filtered_transactions = [{"id": 1, "description": "Оплата услуг"}, {"id": 2, "description": "Оплата товаров"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["ДА", "Оплата"]
        mock_process_bank_search.return_value = filtered_transactions

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_input.assert_any_call("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        mock_input.assert_any_call("Введите слово:")
        mock_process_bank_search.assert_called_once_with(transactions, "Оплата")
        assert result == filtered_transactions
        mock_print.assert_not_called()


def test_user_filter_word_no_lowercase() -> None:
    """
    Тест отказа от фильтрации по слову (нет, нижний регистр)(def user_filter_word)
    """
    # Подготовка
    transactions = [{"id": 1, "description": "Перевод организации"}, {"id": 2, "description": "Оплата услуг"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.return_value = "нет"

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        mock_input.assert_called_once_with("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        mock_process_bank_search.assert_not_called()
        assert result == transactions
        mock_print.assert_not_called()


def test_user_filter_word_no_uppercase() -> None:
    """
    Тест отказа от фильтрации по слову (НЕТ, верхний регистр)(def user_filter_word)
    """
    # Подготовка
    transactions = [{"id": 1, "description": "Перевод организации"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.return_value = "НЕТ"

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        mock_input.assert_called_once_with("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        mock_process_bank_search.assert_not_called()
        assert result == transactions
        mock_print.assert_not_called()


def test_user_filter_word_invalid_then_valid_yes() -> None:
    """
    Тест неверного ввода с последующим корректным вводом (да)(def user_filter_word)
    """
    # Подготовка
    transactions = [{"id": 1, "description": "Перевод организации"}, {"id": 2, "description": "Оплата услуг"}]
    filtered_transactions = [{"id": 1, "description": "Перевод организации"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["может быть", "да", "Перевод"]
        mock_process_bank_search.return_value = filtered_transactions

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        assert mock_input.call_count == 3
        mock_print.assert_called_once_with("Такого пункта нет.")
        mock_process_bank_search.assert_called_once_with(transactions, "Перевод")
        assert result == filtered_transactions


def test_user_filter_word_invalid_then_valid_no() -> None:
    """
    Тест неверного ввода с последующим корректным вводом (нет)(def user_filter_word)
    """
    # Подготовка
    transactions = [{"id": 1, "description": "Перевод организации"}, {"id": 2, "description": "Оплата услуг"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["y", "нет"]

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_print.assert_called_once_with("Такого пункта нет.")
        mock_process_bank_search.assert_not_called()
        assert result == transactions


def test_user_filter_word_empty_transactions() -> None:
    """
    Тест с пустым списком транзакций(def user_filter_word)
    """
    # Подготовка
    transactions = []
    filtered_transactions = []

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["да", "Слово"]
        mock_process_bank_search.return_value = filtered_transactions

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_process_bank_search.assert_called_once_with([], "Слово")
        assert result == filtered_transactions
        mock_print.assert_not_called()


def test_user_filter_word_none_transactions() -> None:
    """
    Тест с None вместо списка транзакций(def user_filter_word)
    """
    # Подготовка
    transactions = None

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["да", "Слово"]
        mock_process_bank_search.side_effect = TypeError("'NoneType' object is not iterable")

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_process_bank_search.assert_called_once_with(None, "Слово")
        mock_print.assert_called_once_with("Ошибка: 'NoneType' object is not iterable")
        assert result is None


def test_user_filter_word_empty_word_input() -> None:
    """
    Тест ввода пустой строки в качестве слова(def user_filter_word)
    """
    # Подготовка
    transactions = [{"id": 1, "description": "Перевод организации"}, {"id": 2, "description": "Оплата услуг"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["да", ""]
        # process_bank_search должен обрабатывать пустую строку
        mock_process_bank_search.return_value = []

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_process_bank_search.assert_called_once_with(transactions, "")
        assert result == []
        mock_print.assert_not_called()


def test_user_filter_word_multiple_word_input() -> None:
    """
    Тест ввода нескольких слов(def user_filter_word)
    """
    # Подготовка
    transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
    ]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["да", "Перевод организации"]
        # process_bank_search должен искать полную фразу
        mock_process_bank_search.return_value = [transactions[0]]

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_process_bank_search.assert_called_once_with(transactions, "Перевод организации")
        assert result == [transactions[0]]
        mock_print.assert_not_called()


def test_user_filter_word_no_matching_transactions() -> None:
    """
    Тест, когда нет транзакций с искомым словом(def user_filter_word)
    """
    # Подготовка
    transactions = [{"id": 1, "description": "Перевод организации"}, {"id": 2, "description": "Оплата услуг"}]

    with (
        patch("builtins.input") as mock_input,
        patch("builtins.print") as mock_print,
        patch("main.process_bank_search") as mock_process_bank_search,
    ):
        # Настраиваем моки
        mock_input.side_effect = ["да", "Карта"]
        mock_process_bank_search.return_value = []

        # Выполнение
        result = user_filter_word(transactions)

        # Проверка
        assert mock_input.call_count == 2
        mock_process_bank_search.assert_called_once_with(transactions, "Карта")
        assert result == []
        mock_print.assert_not_called()


def test_main_successful_flow() -> None:
    """
    Тест успешного выполнения основного потока программы(def main)
    """
    # Подготовка
    mock_transactions = [
        {
            "date": "2023-01-01T12:00:00.000",
            "description": "Перевод организации",
            "from": "Счет 12345678901234567890",
            "to": "Счет 98765432109876543210",
            "operationAmount": {"amount": "1000.00", "currency": {"name": "руб."}},
        },
        {
            "date": "2023-01-02T12:00:00.000",
            "description": "Оплата услуг",
            "from": "Visa Gold 1234567890123456",
            "to": "Счет 98765432109876543210",
            "operationAmount": {"amount": "500.00", "currency": {"name": "руб."}},
        },
    ]

    with (
        patch("builtins.print") as mock_print,
        patch("main.user_input") as mock_user_input,
        patch("main.user_filter") as mock_user_filter,
        patch("main.user_sorted_date") as mock_user_sorted_date,
        patch("main.user_filter_currency") as mock_user_filter_currency,
        patch("main.user_filter_word") as mock_user_filter_word,
        patch("main.mask_account_card") as mock_mask_account_card,
        patch("main.get_date") as mock_get_date,
        patch("main.time.sleep") as mock_sleep,
    ):
        # Настраиваем моки
        mock_user_input.return_value = mock_transactions
        mock_user_filter.return_value = mock_transactions
        mock_user_sorted_date.return_value = mock_transactions
        mock_user_filter_currency.return_value = mock_transactions
        mock_user_filter_word.return_value = mock_transactions

        mock_mask_account_card.side_effect = [
            "Счет **7890",  # для from первой транзакции
            "Счет **4321",  # для to первой транзакции
            "Visa Gold 1234 56** **** 3456",  # для from второй транзакции
            "Счет **4321",  # для to второй транзакции
        ]

        mock_get_date.side_effect = ["01.01.2023", "02.01.2023"]

        # Выполнение
        main()

        # Проверка
        # Проверяем приветственное сообщение
        mock_print.assert_any_call(
            "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла."
        )

        # Проверяем вызовы функций обработки транзакций
        mock_user_input.assert_called_once()
        mock_user_filter.assert_called_once_with(mock_transactions)
        mock_user_sorted_date.assert_called_once_with(mock_transactions)
        mock_user_filter_currency.assert_called_once_with(mock_transactions)
        mock_user_filter_word.assert_called_once_with(mock_transactions)

        # Проверяем анимацию печати
        text = "Распечатываю итоговый список транзакций...\n"
        for char in text:
            mock_print.assert_any_call(char, end="", flush=True)

        # Проверяем вызовы time.sleep для точек
        assert mock_sleep.call_count == 3  # 3 точки в тексте

        # Проверяем итоговое сообщение
        mock_print.assert_any_call(f"Всего банковских операций в выборке: {len(mock_transactions)}")

        # Проверяем вывод транзакций
        # Первая транзакция
        mock_print.assert_any_call(
            "01.01.2023 Перевод организации\n" "Счет **7890 -> Счет **4321\n" "Сумма: 1000.00 руб.\n"
        )

        # Вторая транзакция
        mock_print.assert_any_call(
            "02.01.2023 Оплата услуг\n" "Visa Gold 1234 56** **** 3456 -> Счет **4321\n" "Сумма: 500.00 руб.\n"
        )


def test_main_no_matching_transactions_after_word_filter() -> None:
    """
    Тест случая, когда фильтр по ключевому слову возвращает пустой список(def main)
    """
    # Подготовка
    initial_transactions = [
        {
            "date": "2023-01-01T12:00:00.000",
            "description": "Перевод организации",
            "from": "Счет 12345678901234567890",
            "to": "Счет 98765432109876543210",
            "operationAmount": {"amount": "1000.00", "currency": {"name": "руб."}},
        }
    ]

    # После фильтрации по статусу, сортировки и фильтра по валюте остались транзакции
    filtered_transactions = initial_transactions
    # Но фильтр по слову вернул пустой список
    word_filtered_transactions = []

    with (
        patch("builtins.print") as mock_print,
        patch("main.user_input") as mock_user_input,
        patch("main.user_filter") as mock_user_filter,
        patch("main.user_sorted_date") as mock_user_sorted_date,
        patch("main.user_filter_currency") as mock_user_filter_currency,
        patch("main.user_filter_word") as mock_user_filter_word,
    ):
        # Настраиваем моки
        mock_user_input.return_value = initial_transactions
        mock_user_filter.return_value = filtered_transactions
        mock_user_sorted_date.return_value = filtered_transactions
        mock_user_filter_currency.return_value = filtered_transactions
        mock_user_filter_word.return_value = word_filtered_transactions

        # Выполнение
        main()

        # Проверка
        mock_print.assert_any_call("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
