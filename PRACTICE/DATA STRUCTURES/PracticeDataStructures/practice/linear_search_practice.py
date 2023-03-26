def linear_search_p(sequence, item):
    position = 0

    while position <= len(sequence):
        if sequence[position] == item:
            return position
        position += 1

    return -1


li = [33, 3,2,41,1,6]
itm = 6

result = linear_search_p(li,itm)
print(result)