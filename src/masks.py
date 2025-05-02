import logging
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_info):
    """
    Принимает на вход строку с типом и номером карты и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    parts = card_info.split()
    card_number = parts[-1]
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    masked_card = f"{card_number[:4]} {card_number[4:6]} **** {card_number[-4:]}"
    logger.info(f"Маскированный номер карты: {masked_card}")
    return " ".join(parts[:-1]) + " " + masked_card


def get_mask_account(account_info):
    """
    Принимает на вход строку с типом и номером счета и возвращает маску номера по правилу **XXXX
    """
    parts = account_info.split()
    account_number = parts[-1]
    if len(account_number) < 6:
        raise ValueError("Номер счета должен содержать не менее 6 цифр.")
    masked_number = f"{account_number[-4:]}"
    logger.info(f"Маскированный номер карты: {masked_number}")
    return " ".join(parts[:-1]) + " " + masked_number

print(get_mask_account('36172638712'))
print(get_mask_card_number('2737193628281631'))
