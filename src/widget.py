from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info):
    """
    Принимает на вход строку формата "Visa Platinum 7000792289606361" и "Счет 73654108430135874305"
    """
    if not isinstance(card_info, str):
        raise TypeError("Номер карты или счета должен быть строкой")

    if not card_info:
        raise ValueError("Номер карты или счета не может быть пустым")

    if "Счет" in card_info:
        return get_mask_account(card_info)
    else:
        try:
            return get_mask_card_number(card_info)
        except ValueError as e:
            raise ValueError(str(e))


def get_date(date_str):
    """
    Принимает на вход в формате "2024-03-11T02:26:18.671407" возвращает в формате "ДД.ММ.ГГГГ"
    """
    try:
        date_part = date_str.split("T")[0]
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
    except ValueError:
        raise ValueError("Неверный формат даты")


if __name__ == "__main__":
    card_info = input("enter card number:")
    account_info = input("enter account number:")
    date_str = input("enter date:")

    print(mask_account_card(card_info))
    print(mask_account_card(account_info))
    print(get_date(date_str))
