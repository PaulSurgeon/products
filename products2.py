#讀取檔案

with open("products.csv", "r") as f:
    for line in f:
        s = line.strip().split(",")
        print(s)

#另一種寫法
products2 = []
with open("products.csv", "r") as f:
    for line in f:
        name, price = line.strip().split(",")
        products2.append([name, price])

print(products2)

# 去除標題列，使用continue功能。
products3 = []
with open("products.csv", "r") as f:
    for line in f:
        if "商品,價格" in line:
            continue
        name, price = line.strip().split(",")
        products3.append([name, price])

print(products3)
