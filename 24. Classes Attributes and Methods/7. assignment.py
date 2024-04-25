class PizzaPie():
    def __init__(self, total_slices):
        self.total_slices = total_slices
        self._slices_eaten = 0

    @property
    def slices_eaten(self):
        return self._slices_eaten

    @slices_eaten.setter
    def slices_eaten(self, slices_eaten):
        if slices_eaten <= self.total_slices:
            self._slices_eaten = slices_eaten

    @property
    def percentage(self):
        return self._slices_eaten / self.total_slices

chesse = PizzaPie(8)
chesse.slices_eaten = 2
print(chesse.percentage)

chesse.slices_eaten = 4
print(chesse.percentage)

chesse.slices_eaten = 10
print(chesse.percentage)

# Error --- attributeError: can't set attribute
# chesse.percentage = 0.5