from typing import Dict, List
import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        (
            [
                {"id": 939719570, "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}},
                {"id": 142264268, "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}},
                {"id": 873106923, "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB"}}},
                {"id": 895315941, "operationAmount": {"amount": "56883.54", "currency": {"code": "USD"}}},
            ],
            "USD",
            [
                {"id": 939719570, "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}},
                {"id": 142264268, "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}},
                {"id": 895315941, "operationAmount": {"amount": "56883.54", "currency": {"code": "USD"}}},
            ],
        ),
        (
            [
                {"id": 873106923, "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB"}}},
                {"id": 594226727, "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB"}}},
            ],
            "USD",
            [],
        ),
    ],
)
def test_filter_by_currency(transactions: List[Dict], currency: str, expected: List[Dict]):
    assert list(filter_by_currency(transactions, currency)) == expected


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {"id": 939719570, "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}, "description": "Перевод организации"},
                {"id": 142264268, "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}, "description": "Перевод со счета на счет"},
            ],
            ["Перевод организации", "Перевод со счета на счет"],
        ),
        ([], []),
    ],
)
def test_transaction_descriptions(transactions: List[Dict], expected: List[str]):
    assert list(transaction_descriptions(transactions)) == expected


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (0, 0, ["0000 0000 0000 0000"]),
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: List[str]):
    assert list(card_number_generator(start, stop)) == expected
