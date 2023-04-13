def is_isogram(string):
    s = len(set(string.lower()))
    n = len(string)
    if s == n or s == 0:
        return True
    else:
        return False


print(is_isogram(""))
