def get_category(item):

    item = item.lower()

    categories = {

        "dairy": [
            "milk", "cheese", "butter", "curd", "yogurt", "paneer"
        ],

        "fruits": [
            "apple", "banana", "orange", "mango", "grapes"
        ],

        "vegetables": [
            "onion", "potato", "tomato", "carrot", "cabbage"
        ],

        "bakery": [
            "bread", "bun", "cake", "biscuit"
        ],

        "beverages": [
            "coffee", "tea", "juice"
        ]

    }


    for category, items in categories.items():

        if item in items:

            return category


    return "other"