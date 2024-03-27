def outer():
    def inner():
        return 5
    
    return inner
    
print(outer()())