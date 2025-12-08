from src.utils_regex import process_bank_operations, process_bank_search


def test_basic_functionality_process_bank_search(test_list_regex):
    """Тесты базовой функциональности"""
    # Тест 1: Поиск по слову "перевод"
    result = process_bank_search(test_list_regex, "перевод")
    assert len(result) == 4

    # Тест 2: Поиск по точной фразе "Перевод организации"
    result = process_bank_search(test_list_regex, "Перевод организации")
    assert len(result) == 2

    # Тест 3: Поиск по слову "вклад"
    result = process_bank_search(test_list_regex, "вклад")
    assert len(result) == 1

    # Тест 4: Поиск по части слова "счет"
    result = process_bank_search(test_list_regex, "счет")
    assert len(result) == 2

    # Тест 5: Поиск несуществующего слова
    result = process_bank_search(test_list_regex, "кредит")
    assert len(result) == 0


def test_edge_cases_process_bank_search(test_list_regex):
    """Тесты граничных случаев"""
    # Тест 6: Пустая строка поиска
    result = process_bank_search(test_list_regex, "")
    assert len(result) == len(test_list_regex)

    # Тест 7: Пустой список данных
    result = process_bank_search([], "перевод")
    assert len(result) == 0

    # Тест 8: Регистронезависимость
    result_lower = process_bank_search(test_list_regex, "перевод")
    result_upper = process_bank_search(test_list_regex, "ПЕРЕВОД")
    result_mixed = process_bank_search(test_list_regex, "ПеРеВоД")

    assert len(result_lower) == len(result_upper) == len(result_mixed) == 4


def test_error_handling_process_bank_search(test_list_regex):
    """Тесты обработки ошибок"""
    # Тест 9: Некорректные регулярные выражения
    result = process_bank_search(test_list_regex, "[")
    assert result == []

    # Тест 10: Данные без ключа "description"
    broken_data = [{"id": 1, "amount": 100}]  # нет description
    result = process_bank_search(broken_data, "test")
    assert result == []

    # Тест 11: Не список в качестве data
    result = process_bank_search("not a list", "перевод")
    assert result == []

    # Тест 12: Не строка в качестве search
    result = process_bank_search(test_list_regex, 123)
    assert result == []

    # Тест 13: Данные с некорректным description (не строка)
    broken_data = [{"id": 1, "description": 123}]  # description не строка
    result = process_bank_search(broken_data, "test")
    assert result == []


def test_result_structure_process_bank_search(test_list_regex):
    """Тесты структуры результатов"""
    # Тест 14: Проверка сохранения структуры данных
    result = process_bank_search(test_list_regex, "перевод")
    assert len(result) > 0
    for item in result:
        assert isinstance(item, dict)
        assert "id" in item
        assert "description" in item
        assert "state" in item
        assert "date" in item
        assert "operationAmount" in item


def test_basic_functionality_process_bank_operations(
    test_list_regex, categories_regex1, categories_regex2, categories_regex3
):
    """Тесты базовой функциональности"""
    # Тест 1: Основной тест с categories1
    result = process_bank_operations(test_list_regex, categories_regex1)
    expected = {"Открытие вклада": 1, "Перевод организации": 2, "Перевод со счета на счет": 2}
    assert result == expected

    # Тест 2: Тест с categories2 (частичные совпадения)
    result = process_bank_operations(test_list_regex, categories_regex2)
    expected = {"Перевод": 4, "Вклад": 1, "Организации": 2}  # Все 4 перевода  # 1 вклад  # 2 перевода организации
    assert result == expected

    # Тест 3: Тест с categories3 (нет совпадений)
    result = process_bank_operations(test_list_regex, categories_regex3)
    expected = {}
    assert result == expected

    # Тест 4: Регистронезависимость
    result_lower = process_bank_operations(test_list_regex, ["перевод"])
    result_upper = process_bank_operations(test_list_regex, ["ПЕРЕВОД"])
    result_mixed = process_bank_operations(test_list_regex, ["ПеРеВоД"])

    assert result_lower == result_upper == result_mixed == {"Перевод": 4}


def test_edge_cases_process_bank_operations(test_list_regex, categories_regex1):
    """Тесты граничных случаев"""
    # Тест 5: Пустой список данных
    result = process_bank_operations([], categories_regex1)
    assert result == {}

    # Тест 6: Пустой список категорий
    result = process_bank_operations(test_list_regex, [])
    assert result == {}

    # Тест 7: Оба списка пустые
    result = process_bank_operations([], [])
    assert result == {}

    # Тест 8: Категория - подстрока
    result = process_bank_operations(test_list_regex, ["счет"])
    assert result == {"Счет": 2}


def test_error_handling_process_bank_operations(test_list_regex, categories_regex1):
    """Тесты обработки ошибок"""
    # Тест 9: Не список в качестве data
    result = process_bank_operations("not a list", categories_regex1)
    assert result == {}

    # Тест 10: Не список в качестве categories
    result = process_bank_operations(test_list_regex, "not a list")
    assert result == {}

    # Тест 11: Данные без ключа "description"
    broken_data = [{"id": 1, "amount": 100}]  # нет description
    result = process_bank_operations(broken_data, categories_regex1)
    assert result == {}

    # Тест 12: Данные с некорректным description (не строка)
    broken_data = [{"id": 1, "description": 123}]  # description не строка
    result = process_bank_operations(broken_data, categories_regex1)
    assert result == {}

    # Тест 13: Категории не строки
    mixed_categories = ["Перевод", 123, {"key": "value"}]
    result = process_bank_operations(test_list_regex, mixed_categories)
    # Должны посчитать только строковые категории
    assert result == {}


def test_structure_validation_process_bank_operations(test_list_regex, categories_regex1):
    """Тесты структуры результатов"""
    # Тест 14: Проверка типа результата
    result = process_bank_operations(test_list_regex, categories_regex1)
    assert isinstance(result, dict)

    # Тест 15: Проверка структуры словаря
    result = process_bank_operations(test_list_regex, categories_regex1)
    for key, value in result.items():
        assert isinstance(key, str)
        assert isinstance(value, int)
        assert value >= 0

    # Тест 16: Проверка, что возвращаются только запрошенные категории
    result = process_bank_operations(test_list_regex, ["Перевод организации", "Открытие вклада"])
    assert set(result.keys()) == {"Перевод организации", "Открытие вклада"}


def test_specific_scenarios_process_bank_operations(test_list_regex):
    """Конкретные сценарии"""
    # Тест 17: Перекрывающиеся категории
    result = process_bank_operations(test_list_regex, ["Перевод", "Перевод организации"])
    # "Перевод организации" попадает под обе категории
    expected = {"Перевод": 4, "Перевод организации": 2}
    assert result == expected

    # Тест 18: Одна операция под несколько категорий
    single_operation = [test_list_regex[0]]  # "Перевод со счета на счет"
    result = process_bank_operations(single_operation, ["Перевод", "счет", "организация"])
    expected = {"Счет": 1, "Перевод": 1}  # "организация" не найдена
    assert result == expected

    # Тест 19: Дублирующиеся категории
    result = process_bank_operations(test_list_regex, ["Перевод", "Перевод", "Вклад"])
    # Дубликаты должны обрабатываться корректно
    assert result["Перевод"] == 4
