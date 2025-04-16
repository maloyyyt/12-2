import json
import logging
from unittest.mock import mock_open, patch

from src.utils import get_data


def test_get_data():
    logging.disable(logging.CRITICAL)

    mock_data = '[{"id": 441945886, "state": "EXECUTED"}]'
    mock_file = mock_open(read_data=mock_data)

    with patch('builtins.open', mock_file), \
            patch('logging.FileHandler'):
        result = get_data("../data/operations.json")

    expected_result = json.loads(mock_data)
    assert result == expected_result
    mock_file.assert_called_once_with("../data/operations.json", encoding='utf-8')
