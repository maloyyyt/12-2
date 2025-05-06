import pytest
from unittest.mock import mock_open, patch
import pandas as pd
from src.reader_operations import read_transactions_from_csv, read_transactions_from_excel

def test_read_transactions_from_csv():
    csv_data = """date,amount,description
2023-01-01,100.0,Transaction 1
2023-01-02,200.0,Transaction 2
"""
    with patch('builtins.open', mock_open(read_data=csv_data)):
        transactions = read_transactions_from_csv('transactions.csv')
        assert transactions == [
            {'date': '2023-01-01', 'amount': '100.0', 'description': 'Transaction 1'},
            {'date': '2023-01-02', 'amount': '200.0', 'description': 'Transaction 2'}
        ]

def test_read_transactions_from_excel():
    data = {
        'date': ['2023-01-01', '2023-01-02'],
        'amount': [100.0, 200.0],
        'description': ['Transaction 1', 'Transaction 2']
    }
    df = pd.DataFrame(data)
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value = df
        transactions = read_transactions_from_excel('transactions_excel.xlsx')
        assert transactions == [
            {'date': '2023-01-01', 'amount': '100.0', 'description': 'Transaction 1'},
            {'date': '2023-01-02', 'amount': '200.0', 'description': 'Transaction 2'}
        ]
