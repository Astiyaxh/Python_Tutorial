cryptocurrency_prices = {
    "Bitcoin": 400000,
    "Ethereum": 7000,
    "Ripple": 10,
    "Litecoin": 1000,
    "Dogecoin": 1
}


# print(cryptocurrency_prices.keys())
# print(type(cryptocurrency_prices.keys()))

# print(cryptocurrency_prices.values())
# print(type(cryptocurrency_prices.values()))

for currency in cryptocurrency_prices.keys():
    print(f"The next currency is {currency}")
    
for price in cryptocurrency_prices.values():
    print(f"The next price is {price}")
    


print("Bitcoin" in cryptocurrency_prices.keys())
print("shitcoin" in cryptocurrency_prices.keys())

print(400000 in cryptocurrency_prices.values())
print(5000 in cryptocurrency_prices.values())


print(len(cryptocurrency_prices.keys()))
print(len(cryptocurrency_prices.values()))
print(len(cryptocurrency_prices))
