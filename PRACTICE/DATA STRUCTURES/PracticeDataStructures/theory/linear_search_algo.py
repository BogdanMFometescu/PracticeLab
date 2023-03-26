cards = [1, 2, 3, 4, 5, 6]
query = 4


def locate_cards(cards_li, query_ui):
    # Create a variable for the position and set it to "0"
    position = 0

    # Set up the repetition using a while true loop
    while position < len(cards_li):
        # Check if element is at the position matching the query
        if cards[position] == query_ui:
            # We found the element
            return position
            # Increment the position
        position += 1

    return -1


print(locate_cards(cards, query))

#Big O Complexity
# O(N) and O(1)
