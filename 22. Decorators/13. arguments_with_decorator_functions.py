def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you!")
        fn(*args, **kwargs)
        # print(args)
        # print(kwargs)
        print("It was my pleasure executing your function! Have a nice day!")
        
    return inner

@be_nice
def complex_bussiness_logic(stakeholder, position):
    print(f"Something complex for our {position} {stakeholder}!")


complex_bussiness_logic("Astiyaxh", "CEO")
complex_bussiness_logic(stakeholder = "Astiyaxh", position = "CEO")
complex_bussiness_logic("Astiyaxh", position = "CEO")



