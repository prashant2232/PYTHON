menu = {"pizza": 99,
        "pasta": 49,
        "burger": 39,
        "salad": 69,
        "coffee": 59}
print("Welcome to the Cafe. Here's the menu: ")
print("Pizza: Rs99\nPasta: Rs49\nBurger: Rs39\nSalad: Rs69\nCoffee: Rs59\n")

order_total = 0

item_1 = input("Enter your first item you want to order: ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"order of {item_1} has been added")
else:
    print(f"Ordered item {item_1} not available in the menu")
a = input("Do you want to order anything else? (yes/no)")
if(a == "yes"):
    item_2 = input("Enter your second item you want to order: ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"order of {item_2} has been added")
    else:
        print(f"Ordered item {item_2} not available in the menu")
else:
    print("Thank You for Ordering!!")
print(f"The total price to pay is {order_total}")
