# it should iterate while the amount left is not equal to 0
# and only accept 5/10/25 as inputs
# total amount due 50

coin_due_total = 50

while coin_due_total > 0:
    print("Amount due: ", coin_due_total)

    coin_in = int(input("Insert Coin: "))

    if coin_in in [5, 10, 25]:
        coin_due_total -= coin_in


change_owed = abs(coin_due_total)

print("Change Owed:", change_owed)
