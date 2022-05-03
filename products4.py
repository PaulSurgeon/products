# 這是一個記帳程式，可以輸入購買商品及價格。
# 儲存之後可以讀取，並繼續輸入下次購買的商品及價格。
# 與 products3 相比，將各段函數化，也就是 refactor.
# 這樣可以簡潔，還可以參數化，同時投入很多個參數，使用同一功能。

import os

# 讀取檔案
def read_file(filename):
    products_new = []
    if os.path.isfile(filename):
        print("耶，找到檔案了。")
        with open(filename, "r") as f:
            for line in f:
                if "商品,價格" in line:
                    continue
                s = line.strip().split(",")
                products_new.append(s)
        print(products_new)
    else:
        print("找不到檔案。")
    return products_new

# 另一種寫法
def read_file2(filename):
    products_new2 = []
    with open(filename, "r") as f:
        for line in f:
            name, price = line.strip().split(",")
            products_new2.append([name, price])
    print(products_new2)
    return products_new2

# 讀取檔案時去除標題列，使用continue功能。
def read_file3(filename):
    products_new3 = []
    with open(filename, "r") as f:
        for line in f:
            if "商品,價格" in line:
                continue
            name, price = line.strip().split(",")
            products_new3.append([name, price])
    print(products_new3)
    return products_new3

# 輸入商品名稱與價格程式
def user_input(products):
    while True:
        name = input("請輸入商品名稱，不再輸入請按q停止: ")
        if name == "q":
            break
        price = input("請輸入商品價格: ")
        p = []
        p.append(name)
        p.append(price)
        products.append(p)
    print(products)
    return products

# 印出購買紀錄
def show_price(products):
    for p in products:
        print(p[0], "的價格是", p[1])

# 將商品及價格寫入csv檔永久儲存
def write_file(filename, products):
    with open(filename, "w") as f:
        f.write("商品,價格\n")
        for p in products:
            f.write(p[0] + "," + p[1] + "\n")

products = read_file("products.csv")
products2 = read_file2("products.csv")
products3 = read_file3("products.csv")
products = user_input(products)
show_price(products)
write_file("products.csv", products)