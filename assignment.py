from tabulate import tabulate
import json
num = 0


with open("data.json") as u:
    d = json.load(u)
    customers = (d["customers"])
    products = (d["products"])

total_items_sold = 0
for c in customers:
    print(f"Customer: {c["name"]}")
    el = []
    total_profit = 0
    #declare empty list
    for idx, qty in enumerate(c["orders"]):
        dic = {'Item Purchased':(products[idx]["name"]),
                'Selling Price':(products[idx]["price"]),
                'Quantity':(qty),
                'Item Cost to Produce':(products[idx]["costToProduce"]),
                'Total Item Profit':((((int(products[idx]["price"]))*(qty))) - ((int(products[idx]["costToProduce"]))*(qty))),
                'Customers': (customers[idx]["name"]),
                'Subtotal': ((((products[0]["price"])*(customers[idx]['orders'][0]))+((products[1]["price"])*(customers[idx]['orders'][1]))+((products[2]["price"])*(customers[idx]['orders'][2]))+((products[3]["price"])*(customers[idx]['orders'][3])))),
                'Tax': (0.06*(((products[0]["price"])*(customers[idx]['orders'][0]))+((products[1]["price"])*(customers[idx]['orders'][1]))+((products[2]["price"])*(customers[idx]['orders'][2]))+((products[3]["price"])*(customers[idx]['orders'][3])))),
                'Processing Fee': (customers[idx]["processingFee"]),
                'Order Total': ((customers[idx]["processingFee"])+(0.06*(((products[0]["price"])*(customers[idx]['orders'][0]))+((products[1]["price"])*(customers[idx]['orders'][1]))+((products[2]["price"])*(customers[idx]['orders'][2]))+((products[3]["price"])*(customers[idx]['orders'][3]))))+((((products[0]["price"])*(customers[idx]['orders'][0]))+((products[1]["price"])*(customers[idx]['orders'][1]))+((products[2]["price"])*(customers[idx]['orders'][2]))+((products[3]["price"])*(customers[idx]['orders'][3])))))
                }
        
        #create dictionary of all data needed (item purchased, selling price......)
        el.append(dic)
        total_items_sold += qty
        total_profit += dic['Order Total']
        #add dictionary to list
    #print tabulated list
    print(tabulate(el, headers="keys"))
    print()
print(f"Total Orders Processed: {len(customers)}")
print(f"Total Items Sold: {total_items_sold}")
print(f"total Profit Processed: {total_profit}")