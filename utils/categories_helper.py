CATEGORIES = {
    "dairy": ["milk", "cheese", "butter", "yogurt"],
    "produce": ["apple", "banana", "orange", "tomato", "onion"],
    "bakery": ["bread", "bun", "cake"],
    "beverages": ["juice", "water", "coffee", "tea"],
    "snacks": ["chips", "biscuits", "cookies"],
    "household": ["soap", "detergent", "toothpaste"]
}


def get_category(item):

    item = item.lower()

    for category, items in CATEGORIES.items():
        if item in items:
            return category

    return "other"
