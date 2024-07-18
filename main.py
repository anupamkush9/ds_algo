def minimum_number_of_coins(indian_currency, amount):
    required_coins = []
    for currency in indian_currency[::-1]:
        while amount >= currency:
            required_coins.append(currency)
            amount -= currency
    return required_coins
            
indian_currency = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
amount = 121
required_coins = minimum_number_of_coins(indian_currency, amount)
print("coins_count:::",required_coins)


# ref : https://takeuforward.org/data-structure/find-minimum-number-of-coins/
# ref : https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1
