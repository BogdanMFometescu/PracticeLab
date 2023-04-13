
# Given an array of bird sightings where every element represents a bird type id, determine the id
# of the most frequently sighted
# type. If more than 1 type has been spotted that maximum amount,
# return the smallest of their ids.


def migratory_birds(arr: list):
    birds = sorted(set(arr))
    freq_birds = [arr.count(i) for i in set(arr)]
    return birds[freq_birds.index(max(freq_birds))]


print(migratory_birds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
