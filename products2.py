#讀取檔案

with open("products.csv", "r") as f:
    for line in f:
        s = line.strip().split(",")
        print(s)

products2 = []
with open("products.csv", "r") as f:
    for line in f:
        name, price = line.strip().split(",")
        products2.append([name, price])

print(products2)