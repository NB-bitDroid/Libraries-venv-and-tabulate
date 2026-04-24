from tabulate import tabulate
import json
num = 0


with open("data.json") as u:
    d = json.load(u)
    customers = (d["customers"])
    products = (d["products"])

for c in customers:
    print(c["name"])
    el = []
    #declare empty list
    for idx, qty in enumerate(c["orders"]):
        dic = {'Item Purchased':(products[idx]["name"]),
                'Selling Price':(products[idx]["price"]),
                'Quantity':(qty),
                'Item Cost to Produce':(products[idx]["costToProduce"]),
                'Total Item Profit':((int(products[idx]["price"])) - (int(products[idx]["costToProduce"]))),
                'Subtotal':()
                }
        #create dictionary of all data needed (item purchased, selling price......)
        el.append(dic)
        #add dictionary to list
    #print tabulated list
    print(tabulate(el, headers="keys"))
    print()
