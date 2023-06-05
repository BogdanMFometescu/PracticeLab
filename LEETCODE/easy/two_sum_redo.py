def two_sum(sequence, target):
    complement_map = {}

    for i, num in enumerate(sequence):
        complement = target - num

        print(complement_map)
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[num] = i

two_sum([3,3,1,4],5)