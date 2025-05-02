from src.banking_operations import filter_transactions_by_description

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    transactions = [
        {'date': '2023-01-01', 'description': 'Открытие вклада', 'status': 'EXECUTED', 'amount': 40542, 'currency': 'руб.'},
        {'date': '2023-02-01', 'description': 'Перевод с карты на карту', 'status': 'CANCELED', 'amount': 130, 'currency': 'USD'},
        {'date': '2023-03-01', 'description': 'Перевод организации', 'status': 'EXECUTED', 'amount': 8390, 'currency': 'руб.'},
        {'date': '2023-04-01', 'description': 'Перевод со счета на счет', 'status': 'EXECUTED', 'amount': 8200, 'currency': 'EUR'},
    ]

    choice = input("Введите номер пункта меню: ")
    if choice == '1':
        print("Для обработки выбран JSON-файл.")
    elif choice == '2':
        print("Для обработки выбран CSV-файл.")
    elif choice == '3':
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
        return

    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper()
    while status not in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f"Статус операции \"{status}\" недоступен.")
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper()

    filtered_transactions = [t for t in transactions if t['status'] == status]
    print(f"Операции отфильтрованы по статусу \"{status}\"")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        filtered_transactions.sort(key=lambda x: x['date'], reverse=(order == 'по убыванию'))

    ruble_only = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if ruble_only == 'да':
        filtered_transactions = [t for t in filtered_transactions if t['currency'] == 'руб.']

    search_description = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if search_description == 'да':
        search_string = input("Введите слово для поиска в описании: ")
        filtered_transactions = search_operations_by_description(filtered_transactions, search_string)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(f"{transaction['date']} {transaction['description']}")
            print(f"Сумма: {transaction['amount']} {transaction['currency']}")
            print()


if __name__ == "__main__":
    main()
