# Проект "Виджет банковских операций клиента"

## Описание:

Проект "Виджет банковских операций клиента" - Это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:

- Клонируйте репозиторий:
```
git clone https://github.com/9igor9div9/Domashka91
```
- Установка зависимостей:
```
pip install -r requirements.txt
```

## Использование функций:

1. mask_account_card: Принимает на вход строку формата: Visa Platinum 7000792289606361, или
   Maestro 7000792289606361, или Счет 73654108430135874305. И возвращает
   строку с замаскированным номером. Для карт и счетов используется разная маскировка
2. get_date(date: str): Принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'
   и возвращает строку с датой в формате 'ДД.ММ.ГГГГ' ('11.03.2024').
3. get_mask_card_number: Принимает на вход номер карты в виде числа и возвращает маску номера.
4. get_mask_account: Принимает на вход номер счета в виде числа и возвращает маску номера.
5. filter_by_state: Принимает список словарей и опционально значение для ключа. Возвращает новый список словарей,
   содержащий только те словари, у которых ключ соответствует указанному значению.
6. sort_by_date: Принимает список словарей и необязательный параметр, задающий порядок сортировки.
   Возвращает новый список, отсортированный по дате.

## Примеры работы функций:

- ```
  def mask_account_card(requisites_number):
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
        return "Количество цифр номера карты(счёта) неверно."

- ```
  def get_date(date)
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
  
- ```
  def get_mask_card_number(card_number)
    card_number_str = str(card_number)
    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"
  
- ```
  def get_mask_account(account)
    account_str = str(account)
    return f"**{account_str[-4:]}"
  
- ```
  def filter_by_state(list_of_events, state='EXECUTED')
    sort_list_of_events = []
    for event in list_of_events:
        if event.get('state') == state:
            sort_list_of_events.append(event)
    return sort_list_of_events

- ```
  def sort_by_date(list_of_events_2, sort_order=True)
    sort_list_of_events2 = sorted(list_of_events_2, key=lambda x: x['date'], reverse=sort_order)
    return sort_list_of_events2
  ```

## Лицензия:

Проект распространяется без лицензии.