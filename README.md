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
7. filter_by_currency: Принимает на вход список словарей, представляющих транзакции.
    Возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной.
8. transaction_descriptions: Принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди.
9. card_number_generator: Принимает начальное и конечное значения для генерации диапазона
    номеров (от 0000 0000 0000 0001 до 9999 9999 9999 9999).
    Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X— цифра номера карты.

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
  ```
  def filter_by_currency(transactions:, currency):
    transactions_iter = []
    if len(transactions) == 0:
        return "Отсутствуют входящие данные"
    else:
        for transaction in transactions:
            if "operationAmount" not in transaction:
                return "Некорректные входящие данные"
            elif transaction["operationAmount"]["currency"]["code"] == currency:
                 transactions_iter.append(transaction)
    if len(transactions_iter) == 0:
        return "Транзакции в заданной валюте отсутствуют"
    else:
        return iter(transactions_iter)
  ```
  ```
  def transaction_descriptions(transactions):
    transactions_iter1 = []
    if len(transactions) == 0:
        return "Отсутствуют входящие данные"
    else:
        for transaction in transactions:
            description = transaction["description"]
            transactions_iter1.append(description)
    return iter(transactions_iter1)
  ```
  ```
  def card_number_generator(start: int, stop: int) -> Generator[str]:
    if stop > 9999999999999999:
        raise ValueError("Превышен диапазон генерации номеров карт")
    elif start < 0 or stop < 0:
        raise ValueError("Число не может быть отрицательным")
    card_number_iter = []
    for i in range(start, stop + 1):
        number = str(i).zfill(16)
        formatted_number = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
        card_number_iter.append(formatted_number)
    return iter(card_number_iter)
  ```

## Проект протестирован при помощи Pytest
[Отчёт о тестировании](htmlcov/index.html)


## Лицензия:

Проект распространяется без лицензии.

### Проект на доработке.