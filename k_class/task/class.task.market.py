# 마켓은 손님 한 명에게 한 개의 상품을 판매한다.
# 손님마다 할인율이 다르다
# 마켓에서 판매 시 손님의 할인율을 적용하여 판매한다.


class Market:
    # 상품명, 상품가격, 상품 재고
    def __init__(self,product_name,product_price,product_stock):
        self.product_name = product_name
        self.product_price = product_price
        self.product_stock = product_stock

    def sales(self,customer):
        price = self.product_price*customer.discount*0.01
        self.product_stock-=1
        customer.money-=price
        return price,customer.money



class Customer:
    # 이름, 나이, 할인율
    def __init__(self,name,age,discount,money):
        self.name= name
        self.age = age
        self.discount =discount
        self.money = money



lotte = Market("새우깡",5000,100)

ey = Customer("ey",15,50,10000)

price,rest = lotte.sales(ey)

print(price,rest)