amount = 50
while amount > 50:
    print("Amount Due: ", amount)
    coin = int(input("Insert coin: "))
    if coin in [25, 10, 5]:
        amount -= coin
change = abs(amount)
print("Change owed: ", change)