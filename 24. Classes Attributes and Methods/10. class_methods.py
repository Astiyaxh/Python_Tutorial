class SushiPlatter():
    def __init__(self, salmon, tuna, shrimp, squid):
        self.salmon = salmon
        self.tuna   = tuna
        self.shrimp = shrimp
        self.squid  = squid
    
    @classmethod
    def lunch_special_A(cls):
        return cls(salmon=2, tuna=2, shrimp=2, squid=0)

    @classmethod
    def tuna_lover(cls):
        return cls(salmon=0, tuna=10, shrimp=0, squid=1)

ariyan = SushiPlatter(salmon = 8, tuna = 4, shrimp = 5, squid = 10)
print(ariyan.salmon)

lunch_eater = SushiPlatter.lunch_special_A()
print(lunch_eater.salmon)
print(lunch_eater.squid)

tuna_fan = SushiPlatter.tuna_lover()
print(tuna_fan.salmon)
print(tuna_fan.tuna)


from datetime import date

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    @classmethod
    def calcaulate_age(cls, name, birth_year):
         return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))



ariyan = Student("Ariyan", 20)
ariyan.show()


john = Student.calcaulate_age("John", 2000)
john.show()


