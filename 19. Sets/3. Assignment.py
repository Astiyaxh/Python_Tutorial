movies = {"Bad Boys", "13 Hours: The Secret Soldiers of Benghazi", "Gladiator"}


months = {"January", "February", "March", "April"}


empty = set()
print(type(empty))


def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 3, 3, 2]))
print(remove_duplicates([1, 2, 3, 4, 5]))