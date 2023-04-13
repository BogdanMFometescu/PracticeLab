def is_valid_walk(walk: list):
    north = "n"
    south = "s"
    east = "e"
    west = "w"
    n = walk.count(north)
    s = walk.count(south)
    e = walk.count(east)
    w = walk.count(west)
    if n == s and e == w and len(walk) <= 10:
        return True
    else:
        return False


print(is_valid_walk(['n', 'e', 's', 'e', 's', 'w', 'n', 'w']))
