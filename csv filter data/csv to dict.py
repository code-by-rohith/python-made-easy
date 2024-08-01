import csv

master_product = {}
with open('master_product.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        master_product[row['ID']] = row

product_ids = []
with open('product.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product_ids.append(row['ID'])

with open('output.csv', mode='w', newline='') as file:
    fieldnames = ['ID', 'Product Name', 'Price', 'GST %']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for product_id in product_ids:
        if product_id in master_product:
            writer.writerow(master_product[product_id])

print("Filtered records have been written to output.csv")