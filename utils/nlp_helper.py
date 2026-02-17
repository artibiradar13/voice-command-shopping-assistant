from transformers import pipeline
import re

# -------------------------
# LOAD MODEL
# -------------------------

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

actions = ["add item", "remove item", "search item"]


# -------------------------
# CLEAN TEXT
# -------------------------

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    return text


# -------------------------
# EXTRACT QUANTITY
# -------------------------

def extract_quantity(command):

    numbers = re.findall(r'\d+', command)

    if numbers:
        return int(numbers[0])

    words_to_num = {
        "one": 1, "two": 2, "three": 3,
        "four": 4, "five": 5
    }

    for word in command.split():
        if word in words_to_num:
            return words_to_num[word]

    return 1


# -------------------------
# EXTRACT ITEM
# -------------------------

def extract_item(command):

    ignore = [
        "add", "remove", "buy", "need", "want",
        "search", "find", "get", "me", "please",
        "item", "items"
    ]

    words = command.split()

    for word in words:
        if word not in ignore and not word.isdigit():
            return word

    return None


# -------------------------
# PROCESS COMMAND
# -------------------------

from transformers import pipeline
import re

# -------------------------
# LOAD MODEL
# -------------------------

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

actions = ["add item", "remove item", "search item"]


# -------------------------
# CLEAN TEXT
# -------------------------

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    return text


# -------------------------
# EXTRACT QUANTITY
# -------------------------

def extract_quantity(command):

    numbers = re.findall(r'\d+', command)

    if numbers:
        return int(numbers[0])

    words_to_num = {
        "one": 1, "two": 2, "three": 3,
        "four": 4, "five": 5
    }

    for word in command.split():
        if word in words_to_num:
            return words_to_num[word]

    return 1


# -------------------------
# EXTRACT ITEM
# -------------------------

def extract_item(command):

    ignore = [
        "add", "remove", "buy", "need", "want",
        "search", "find", "get", "me", "please",
        "item", "items"
    ]

    words = command.split()

    for word in words:
        if word not in ignore and not word.isdigit():
            return word

    return None


# -------------------------
# PROCESS COMMAND
# -------------------------
def process_command(command):

    command = command.lower()

    # Quantity detection
    qty_match = re.search(r'\d+', command)
    qty = int(qty_match.group()) if qty_match else 1

    stop_words = ["i", "need", "add", "buy", "please", "want", "to"]

    words = re.findall(r'\b[a-zA-Z]+\b', command)

    filtered = [w for w in words if w not in stop_words]

    if not filtered:
        return None, None, None

    item = filtered[-1]

    return "add", item, qty
