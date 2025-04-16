import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def get_amount_rub(transaction):
    """
        Конвертирует сумму транзакции в рубли
    """
    code = transaction.get('operationAmount').get('currency').get('code')
    amount = float(transaction.get('operationAmount').get('amount'))

    if code == 'RUB':
        return amount

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={code}&amount={amount}"

    payload = []
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    if status_code == 200:
        result = response.json()
        return result["result"]
