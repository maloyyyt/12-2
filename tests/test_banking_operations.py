import re
import pytest
from banking_operations import filter_transactions_by_description, count_transactions_by_category

@pytest.fixture
def transactions():
    return [
        {'description': 'Grocery Shopping', 'amount': 100},
        {'description': 'Online Purchase', 'amount': 200},
        {'description': 'Gas Station', 'amount': 50},
        {'description': 'Coffee Shop', 'amount': 10},
        {'description': 'Grocery Store', 'amount': 150}
    ]

def test_filter_transactions_by_description(transactions):
    # Test case 1: Search for 'Grocery'
    result = filter_transactions_by_description(transactions, 'Grocery')
    expected = [
        {'description': 'Grocery Shopping', 'amount': 100},
        {'description': 'Grocery Store', 'amount': 150}
    ]
    assert result == expected

    # Test case 2: Search for 'Shop'
    result = filter_transactions_by_description(transactions, 'Shop')
    expected = [
        {'description': 'Grocery Shopping', 'amount': 100},
        {'description': 'Coffee Shop', 'amount': 10}
    ]
    assert result == expected

    # Test case 3: Search for a non-existent description
    result = filter_transactions_by_description(transactions, 'Restaurant')
    expected = []
    assert result == expected

def test_count_transactions_by_category(transactions):
    # Test case 1: Count categories
    categories = ['Grocery', 'Shop', 'Gas']
    result = count_transactions_by_category(transactions, categories)
    expected = {
        'Grocery': 2,
        'Shop': 2,
        'Gas': 1
    }
    assert result == expected

    # Test case 2: Count with no matching categories
    categories = ['Restaurant', 'Entertainment']
    result = count_transactions_by_category(transactions, categories)
    expected = {
        'Restaurant': 0,
        'Entertainment': 0
    }
    assert result == expected

    # Test case 3: Count with case insensitive match
    categories = ['grocery', 'shop', 'gas']
    result = count_transactions_by_category(transactions, categories)
    expected = {
        'grocery': 2,
        'shop': 2,
        'gas': 1
    }
    assert result == expected
