def delete_keys(my_dict, strings):
    for item in strings:
        if item in my_dict:
            my_dict.pop(item)
    return my_dict

my_dict = {'A': 1, 'B': 2, 'C': 3}
strings = ["A", "B"]
print(delete_keys(my_dict, strings))