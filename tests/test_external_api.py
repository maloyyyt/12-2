from unittest.mock import patch

from src.external_api import get_amount_rub


def test_get_amount_rub_from_rub():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    assert get_amount_rub(transaction) == 31957.58


@patch("requests.request")
def test_get_amount_rub_from_usd(mock_request):
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = {'result': 435.649305}
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "5",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    assert get_amount_rub(transaction) == 435.649305
    mock_request.assert_called_once()


@patch("requests.request")
def test_get_amount_rub_exception(mock_request):
    mock_request.return_value.status_code = 500

    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "5",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    assert get_amount_rub(transaction) is None  # Ожидаем None
    mock_request.assert_called_once()
