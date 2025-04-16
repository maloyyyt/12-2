def get_mask_card_number(card_info):
    """
    Принимает на вход строку с типом и номером карты и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    parts = card_info.split()
    card_number = parts[-1]
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return ' '.join(parts[:-1]) + ' ' + masked_number


def get_mask_account(account_info):
    """
    Принимает на вход строку с типом и номером счета и возвращает маску номера по правилу **XXXX
    """
    parts = account_info.split()
    account_number = parts[-1]
    if len(account_number) < 6:
        raise ValueError("Номер счета должен содержать не менее 6 цифр.")
    masked_number = f"**{account_number[-4:]}"
    return ' '.join(parts[:-1]) + masked_number
