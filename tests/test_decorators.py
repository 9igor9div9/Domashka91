import pytest

from src.decorators import log


def test_log_file() -> None:
    """Проверка записи в файл"""
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open('mylog.txt') as f:
        line = f.readline()
        print(line)
        assert line.strip() == "Функция: my_function"


def test_log_file_consol(capsys) -> None:
    """Проверка вывода в консоль"""
    @log()
    def my_function(x, y):
        return x / y

    my_function(2, 1)
    result = capsys.readouterr()
    assert result.out.split("\n")[0] == "Функция: my_function"


def test_log_file_consol_error(capsys) -> None:
    """Проверка вывода в консоль при ошибке"""
    @log()
    def my_function(x, y):
        return x / y
    with pytest.raises(Exception):
        my_function(2, "3")


def test_log_file_consol_error_zero(capsys) -> None:
    """Проверка вывода в консоль при другой ошибке"""
    @log()
    def my_function(x, y):
        return x / y
    with pytest.raises(Exception):
        my_function(2, 0)
