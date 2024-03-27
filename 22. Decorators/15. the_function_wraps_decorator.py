import functools

def be_nice(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you!")
        result = fn(*args, **kwargs)
        print("It was my pleasure executing your function! Have a nice day!")
        return result
        
    return inner

@be_nice
def complex_bussiness_logic(a, b):
    "Adds to numbers together"
    return a + b

help(complex_bussiness_logic)



