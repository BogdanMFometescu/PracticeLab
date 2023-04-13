def missing_letter(chars: list):
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    match = False
    count = 0
    for letter in s:
        if letter == chars[count]:
            match = True
            count = count + 1
        elif match:
            return letter
