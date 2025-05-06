import json
import csv
import pandas as pd
from src.banking_operations import filter_transactions_by_description

from src.reader_operations import (
    read_transactions_from_csv,
    read_transactions_from_excel,
)

from src.utils import load_transactions


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта меню: ")

    filepath = ""
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        filepath = "data/operations.json"
        transactions = load_transactions(filepath)
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        filepath = "data/transactions.csv"
        transactions = read_transactions_from_csv(filepath)
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        filepath = "data/transactions_excel.xlsx"
        transactions = read_transactions_from_excel(filepath)
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
        return

    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
    ).upper()
    while status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Статус операции "{status}" недоступен.')
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
        ).upper()

    filtered_transactions = [t for t in transactions if t.get("state", {}) == status]
    print(f'Операции отфильтрованы по статусу "{status}"')

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        filtered_transactions.sort(
            key=lambda x: x["date"], reverse=(order == "по убыванию")
        )

    ruble_only = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if ruble_only == "да":
        if choice == "1":
            filtered_transactions = [
                t
                for t in filtered_transactions
                if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
            ]
        else:
            filtered_transactions = [
                t for t in filtered_transactions if t.get("currency_code") == "RUB"
            ]

    search_description = (
        input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
        )
        .strip()
        .lower()
    )
    if search_description == "да":
        search_string = input("Введите слово для поиска в описании: ")
        filter_transactions_by_description = search_operations_by_description(
            filtered_transactions, search_string
        )

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            if choice == "1":
                print(f"{transaction['date']} {transaction['description']}")
                print(
                    f"Сумма: {transaction.get('operationAmount', {}).get('amount', {})} {transaction.get('operationAmount', {}).get('currency', {}).get('code')}"
                )
                print()
            else:
                print(f"{transaction['date']} {transaction['description']}")
                print(
                    f"Сумма: {transaction.get('amount', {})} {transaction.get('currency_code')}"
                )
                print()


if __name__ == "__main__":
    main()
