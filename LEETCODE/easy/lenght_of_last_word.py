# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

def length_of_last_word(s):
    res = s.split(' ')
    while '' in res:
        res.remove('')

    return len(res[-1])


print(length_of_last_word('   fly me   to   the moon  '))
