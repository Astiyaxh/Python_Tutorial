stocks = {"MSFT", "FB", "IBM", "FB"}
print(type(stocks))
print(stocks)

prices = {1, 2, 3, 4, 5, 3, 4, 2}
print(prices)

lottery_numbers = {(1, 2, 3), (4, 5, 6), (1, 2, 3)}
print(lottery_numbers)

print(len(stocks))
print(len(prices))
print(len(lottery_numbers))

print("MSFT" in stocks)
print("IBM" in stocks)
print("GOOG" in stocks)

for number in prices:
    print(number)
