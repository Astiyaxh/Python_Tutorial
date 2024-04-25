class Currency():
    def __init__(self, dollar):
        self._cents = dollar * 100

    @property
    def dollars(self):
        return self._cents / 100

    @dollars.setter
    def dollars(self, dollar):
        if dollar >= 0:
            self._cents = dollar * 100
    
bank_account = Currency(50000)
print(bank_account.dollars)

bank_account.dollars = 100000
print(bank_account.dollars)

bank_account.dollars = -20000
print(bank_account.dollars)
