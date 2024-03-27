def be_nice(fn):
    def inner():
        print("Nice to meet you! I'm honored to execute your function for you!")
        fn()
        print("It was my pleasure executing your function! Have a nice day!")
        
    return inner

# def complex_bussiness_logic():
#     print("Something complex!")

# print(be_nice(complex_bussiness_logic))
# result = be_nice(complex_bussiness_logic)
# result()

@be_nice
def complex_bussiness_logic():
    print("Something complex!")

@be_nice
def another_fancy_function():
    print("Goo goo gaga")

# complex_bussiness_logic()
another_fancy_function()



