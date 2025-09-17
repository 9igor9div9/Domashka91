def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    if card_number is None:
        raise ValueError("Отсутствуют входящие данные")
    if not isinstance(card_number, int) or card_number < 0:
        raise TypeError("Неправильный ввод")
    if len(str(card_number)) > 16 or len(str(card_number)) < 16:
        raise ValueError("Неверное количество цифр")
    card_number_str = str(card_number)
    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"


def get_mask_account(account: int) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""
    if account is None:
        raise ValueError("Отсутствуют входящие данные")
    if not isinstance(account, int) or account < 0:
        raise TypeError("Неправильный ввод")
    if len(str(account)) > 20 or len(str(account)) < 20:
        raise ValueError("Неверное количество цифр")
    account_str = str(account)
    return f"**{account_str[-4:]}"


#if __name__ == "__main__":
#    print(get_mask_account(-73654108430135874305))
#    print(get_mask_card_number(7000792289606361))

