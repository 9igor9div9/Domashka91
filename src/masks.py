import logging
import os

# Основная конфигурация logging

path_log_masks = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs", "masks.log"))
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s",  # Формат записи
    filename=path_log_masks,  # Запись логов в файл
    filemode="w",  # Перезапись файла при каждом запуске
    encoding="UTF-8",
)  # Задаёт кодировку сообщений в файле лога(если необходимо)

# Создаем логеры для различных компонентов программы
card_number_logger = logging.getLogger("card_number_logger")
account_logger = logging.getLogger("account_logger")


def get_mask_card_number(card_number: int = 0) -> str:
    """Принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    card_number_logger.info("Начало работы функции маскировки номера карты")
    if card_number == 0:
        card_number_logger.error("Отсутствует номер карты")
        raise ValueError("Отсутствует номер карты")
    if len(str(card_number)) > 16 or len(str(card_number)) < 16:
        card_number_logger.error("Неверное количество цифр в номере карты")
        print(card_number)
        raise ValueError(f"Неверное количество цифр в номере карты{card_number}")
    card_number_str = str(card_number)
    card_number_logger.info("Работа функции маскировки номера карты завершилась успешно")
    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"


def get_mask_account(account: int = 0) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""
    account_logger.info("Начало работы функции маскировки номера счёта")
    if account == 0:
        account_logger.error("Отсутствуют входящие данные")
        raise ValueError("Отсутствуют входящие данные")
    if len(str(account)) > 20 or len(str(account)) < 20:
        account_logger.error("Неверное количество цифр в номере счёта")
        raise ValueError("Неверное количество цифр в номере счёта")
    account_str = str(account)
    account_logger.info("Работа функции маскировки номера счёта завершилась успешно")
    return f"**{account_str[-4:]}"


if __name__ == "__main__":
#    print(get_mask_account(73654108430135874305))
#    print(get_mask_account())
    print(get_mask_card_number(int("0108438735874305")))
#   print(get_mask_card_number())
