from datetime import datetime

from src import masks


def mask_account_card(requisites_number: str) -> str:
    """Принимает на вход строку формата: Visa Platinum 7000792289606361, или
    Maestro 7000792289606361, или Счет 73654108430135874305. И возвращает
    строку с замаскированным номером. Для карт и счетов используется разная маскировка"""
    requisites_number_list = list(requisites_number)
    requisites_str = ""
    for number in requisites_number_list:
        if number.isdigit():
            requisites_str += number
    if len(requisites_str) == 16:
        return masks.get_mask_card_number(int(requisites_str))
    elif len(requisites_str) == 20:
        return masks.get_mask_account(int(requisites_str))
    else:
        raise ValueError("Количество цифр номера карты(счёта) неверно.")


def get_date(date: str) -> str:
    """Принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'
    и возвращает строку с датой в формате 'ДД.ММ.ГГГГ' ('11.03.2024')"""
    try:
        date_obj = datetime.fromisoformat(date)
        formatted_date = date_obj.strftime("%d.%m.%Y")
        return formatted_date
    except ValueError:
        return "Некорректный формат даты"


# if __name__ == "__main__":
#    print(mask_account_card("Счёт 73654108430135874305"))
#    print(mask_account_card("Visa Platinum 7000792289606361"))
#    print(get_date("2024-03-11T02:26:18.671407"))
