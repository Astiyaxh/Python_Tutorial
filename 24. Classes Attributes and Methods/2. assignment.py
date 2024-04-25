class Musician():
    def __init__(self, age, income):
        self.age = age
        self.income = income

    def enter_club(self):
        if self.age < 21:
            return "Access denied!"
        else:
            return "Access granted!"
        
    def play_show(self):
        self.income += 5


cliff = Musician(age = 27, income = 0)
print(cliff.age)
print(cliff.enter_club())
print(cliff.income)
cliff.play_show()
print(cliff.income)
cliff.play_show()
print(cliff.income)