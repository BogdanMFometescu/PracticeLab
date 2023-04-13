# Your task is to sort a given string. Each word in the string will contain a single number.
# This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input
# String will only contain valid consecutive numbers.


def order(sentence):
    x = [x for x in sentence.split(" ")]
    y = [item for sublist in x for item in sublist if item.isdigit()]
    d = dict(zip(x, y))
    sort_d = sorted(d.items(), key=lambda z: z[1])
    sorted_lst = []
    for item in sort_d:
        i = item[0]
        sorted_lst.append(i)

    result = " ".join(sorted_lst)
    print(result)


order("4of Fo1r pe6ople g3ood th5e the2")

s = "Fo1r the2 g3ood 4of th5e pe6ople"


def order_simple(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))


print(order_simple("Fo1r the2 g3ood 4of th5e pe6ople"))
