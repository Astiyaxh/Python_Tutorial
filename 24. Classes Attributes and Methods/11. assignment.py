class Chocolate():
    def __init__(self, cacao_content):
        self.cacao_content = cacao_content
    
    @classmethod
    def sweet(cls):
        return cls(30)
    
    @classmethod
    def semisweet(cls):
        return cls(50)

    @classmethod
    def bittersweet(cls):
        return cls(cacao_content = 70)

    @classmethod
    def bitter(cls):
        return cls(cacao_content = 99)