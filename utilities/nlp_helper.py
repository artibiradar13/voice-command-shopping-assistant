def process_command(command):

    command = command.lower().strip()

    action = None
    item = None
    quantity = 1


    words = command.split()


    # ADD COMMANDS
    if "add" in words or "buy" in words or "need" in words:

        action = "add"

        for word in words:

            if word.isdigit():

                quantity = int(word)

        item = words[-1]



    # REMOVE COMMAND
    elif "remove" in words or "delete" in words:

        action = "remove"

        item = words[-1]



    # SEARCH COMMAND
    elif "search" in words or "find" in words:

        action = "search"

        item = words[-1]


    return action, item, quantity