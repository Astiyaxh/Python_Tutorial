def plenty_of_arguments(a, b, **kwargs):
    return a + b + sum(kwargs.values()) > 100
    # total = 0
    # for value in kwargs.values():
    #     total += value
    # if total + a + b > 100:
    #     return True
    # else:
    #     return False
    
print(plenty_of_arguments(20, 30))
print(plenty_of_arguments(a = 50, b = 75))
print(plenty_of_arguments(a = 50, b = 25, c = 50))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26))