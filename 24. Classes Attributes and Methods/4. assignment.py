class Book():
    def __init__(self, author, publisher, page_count):
        self._author     = author
        self._publisher  = publisher
        self.page_count = page_count 

    def copyright(self):
        return f"Copyright {self._author}, {self._publisher}"

    def rip_in_half(self):
        if self.page_count > 1:
            self.page_count /= 2
        else:
            self.page_count = 0



book = Book(author= "Grant Cardone", publisher= "10X Enterprises", page_count= 10)

print(book.copyright())
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
