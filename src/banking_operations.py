import re

def filter_transactions_by_description(transactions, search_string):
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]

def count_transactions_by_category(transactions, categories):
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get('description', '')
        for category in categories:
            if re.search(category, description, re.IGNORECASE):
                category_count[category] += 1
    return category_count
