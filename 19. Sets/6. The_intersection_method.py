candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reeses Pieces", "Snickers"}

print(candy_bars.intersection(sweet_things))
print(candy_bars & sweet_things)


value = {3.0, 4.0, 5.0}
more_value = {3, 4, 5}

print(value & more_value)
print(more_value & value)
print(value.intersection(more_value))
print(more_value.intersection(value))