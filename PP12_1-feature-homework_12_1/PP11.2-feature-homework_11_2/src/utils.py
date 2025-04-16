import json


def get_data(path):
    """
        Загружает данные из JSON-файла и возвращает их в виде списка
    """
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        if data:
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
