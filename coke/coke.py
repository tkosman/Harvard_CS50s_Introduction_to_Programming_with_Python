amount_due = 50
amount_inserted = 0
while amount_due > amount_inserted:
    print("Amount due:", amount_due - amount_inserted)
    insert = int(input("Insert coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        amount_inserted += insert

print("Change owed:", amount_inserted - amount_due)