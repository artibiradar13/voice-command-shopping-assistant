SUGGESTIONS = {
    "milk": ["bread", "butter", "eggs"],
    "bread": ["butter", "jam"],
    "coffee": ["sugar", "milk"],
    "pasta": ["tomato sauce", "cheese"],
    "rice": ["dal", "vegetables"],
    "chips": ["soft drink"]
}


def get_suggestions(item):

    item = item.lower()

    if item in SUGGESTIONS:
        return SUGGESTIONS[item]

    return []
