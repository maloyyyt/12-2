import csv
import pandas as pd
from typing import List, Dict

def read_transactions_from_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из CSV файла.
    """
    transactions = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)
    return transactions

def read_transactions_from_excel(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из Excel файла.
    """
    df = pd.read_excel(file_path)
    transactions = df.to_dict(orient='records')
    return transactions
