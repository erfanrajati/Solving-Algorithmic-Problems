# https://quera.org/problemset/193460

inventory = input().split()
inventory[0] = int(inventory[0])
inventory[1] = int(inventory[1])

sword_price = input().split()
sword_price[0] = int(sword_price[0])
sword_price[1] = int(sword_price[1])

rate = int(input())

sword_final_price = sword_price[0] + sword_price[1] * rate
inventory_final = inventory[0] + inventory[1] * rate

if sword_final_price > inventory_final:
    print("No")
else:
    print("Yes")
