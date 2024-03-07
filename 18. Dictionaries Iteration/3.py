def invert(dictofobjects):
    new_dict = {}
    for key, value in dictofobjects.items():
        new_dict[value] = key
    return new_dict

print(invert({"a": 1, "b": 2, "c": 3}))


def count_of_values(dictofobjects, target):
    count = 0
    for key, value in dictofobjects.items():
        if value == target:
            count += 1
    return count

print(count_of_values({"a": 1, "b": 2, "c": 3, "d": 1, "e": 1}, 1))
print(count_of_values({"a": 1, "b": 2, "c": 3, "d": 1, "e": 1, "f": 3}, 3))


def sum_of_values(dictofobjects, listofstrings):
    total = 0
    for key, value in dictofobjects.items():
        if key in listofstrings:
            total += value
    return total

dictofobjects = {"a": 5, "b": 3, "c": 10}
print(sum_of_values(dictofobjects, ["a"]))
print(sum_of_values(dictofobjects, ["a", "b", "c"]))
print(sum_of_values(dictofobjects, ["a", "c"]))
print(sum_of_values(dictofobjects, ["z"]))
    