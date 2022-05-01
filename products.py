# 輸入商品名稱與價格程式

products = []
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
