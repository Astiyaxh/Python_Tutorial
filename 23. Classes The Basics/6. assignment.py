class Musical():
    def __init__(self, name):
        self.name = name
        
rent = Musical("Rent")
mormon = Musical("Book of Mormon")
chicago = Musical("Chicago")

print(rent.name, ",", mormon.name, ",", chicago.name)


class Shape():
    def __init__(self, sides ):
        self.sides = sides
                
triangle = Shape(3)
square = Shape(4)
decagon = Shape(sides = 10)

print(triangle.sides, ",", square.sides, ",", decagon.sides)


class Skyscraper():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
empire = Skyscraper("Empire State Building", 1931)
print(empire.name, empire.year)

wtc = Skyscraper(name = "One World Trade Center", year = 2014)
print(wtc.name, wtc.year)
