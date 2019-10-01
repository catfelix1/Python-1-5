Freeshipping = False
print("Welcome to Adams Kiwi Mart")
print("What is your first items price")
item1 = float(input("first item"))
print("What is your second items price")
item2 = float(input("second item"))
print("What is your third items price")
item3 = float (input("third item"))
Shippingcost = (item1*1.12)+(item2*1.12)+(item3*1.12)
if Shippingcost >= 100:
    print("You will recive free shipping")
    Freeshipping = True
print("Shippingcost = ${0:.2f} ".format(Shippingcost))
