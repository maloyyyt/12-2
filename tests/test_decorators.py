import os

from src.decorators import log


def setup_function():
    """Очищает логи перед каждым тестом."""
    if os.path.exists("../test_log.txt"):
        os.remove("../test_log.txt")


def read_log():
    """Читает содержимое лог-файла."""
    with open("../test_log.txt", "r", encoding="utf-8") as f:
        return f.read().strip()


def test_successful_function():
    setup_function()

    @log("../test_log.txt")
    def test_func(x, y):
        return x + y

    result = test_func(3, 4)
    assert result == 7

    log_content = read_log()
    assert log_content == "test_func ok"


def test_function_with_error():
    setup_function()

    @log("../test_log.txt")
    def test_func(x):
        return 1 / x

    result = test_func(0)
    assert result is None

    log_content = read_log()
    expected_message = "test_func error: ZeroDivisionError, (0,), {}"
    assert log_content == expected_message, f"Unexpected log content: {log_content}"
