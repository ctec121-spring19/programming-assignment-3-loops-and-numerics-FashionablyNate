# Module 2
#   Programming Assignment 3
#     Prob-5.py

# Nathan Spelts

def main():
    print()
    print("\t    PyMart")
    print()
# Prices
    pizza = 2.00
    LDrink = 1.50
    donut = 0.56
# Item List
    print("x2 Pizza:\t\t", "$", pizza * 2)
    print("x1 Large Drink:\t\t", "$", LDrink)
    print("x2 Donut:\t\t", "$", donut * 2)
    print("---------------------------------")
# Totals
    subtotal = pizza * 2 + LDrink + donut * 2
    print("Subtotal:\t\t", "$", subtotal)

    tax = subtotal * 0.084
    print("Tax:\t\t\t", "$", round(tax, 2))
    print()

    total = subtotal + tax
    print("Total:\t\t\t", "$", round(total, 2))
    print()
# Payment
    tender = eval(input("Please enter an amount:  $ "))
    print("Tendered:\t\t", "$", tender + 0.00)

    change = tender - total
    print("Change:\t\t\t", "$", round(change, 2))
    print()
    print("Thank you for shopping at PyMart!")
    print()
main()