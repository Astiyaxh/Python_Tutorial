a = 1

def modify_a(value):
    global a
    a = value

print(a)
modify_a(50)
print(a)
