import functools


def log(filename=None):
    """Декоратор логирования вызовов функций"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n"
            except Exception as e:
                message = f"{func.__name__} error: {e.__class__.__name__}, {args}, {kwargs}\n"
                result = None
            if filename:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(message)
            else:
                print(message)
            return result
        return wrapper
    return decorator


@log("mylog.txt")
def my_function(x, y):
    """Функция складывания"""
    return x + y


my_function(1, 2)


@log()
def error_function(x):
    """Функция деления на ноль"""
    return 1 / x


error_function(0)
