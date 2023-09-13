import u_mysql.crud as db
import random

# 음료수 등록
for i in range(10):
    soft_drink_insert_query = "insert into tbl_soft_drink(soft_drink_name,soft_drink_price)values(%s,%s)"
    soft_drink_insert_params = [f'음료수{i+1}',(i+1)*1000]
    db.save(soft_drink_insert_query,soft_drink_insert_params)

# 상품 등록
for i in range(5):
    product_insert_query = "insert into tbl_product(product_name)values(%s)"
    product_insert_params = [f'상품{i+1}']
    db.save(product_insert_query,product_insert_params)

# 당첨 번호 등록
for i in range(23):
    product_select_random_query = "select * from tbl_product where product_name = %s"
    random_name = f"상품{random.randint(1,5)}"
    product = db.find_one(product_select_random_query,random_name)

    lottery_insert_query = "insert into tbl_lottery(product_id)values(%s)"

    db.save(lottery_insert_query,product.get("id"))

# 100개 유통
for i in range(100):
    soft_drinks_query = "select id from tbl_soft_drink"
    soft_drink_ids = db.find_all(soft_drinks_query)
    random_soft_drink_id=random.sample([i.get("id") for i in soft_drink_ids],1)[0]

    lottery_query = "select id from tbl_lottery"
    lottery_ids = db.find_all(lottery_query)
    random_lottery_id = random.sample([i.get("id")for i in lottery_ids] + [None for i in range(70)],1)[0]

    circulation_insert_query = "INSERT INTO app.tbl_circulation(lottery_id, soft_drink_id)VALUES(%s, %s)"
    db.save(circulation_insert_query,[random_lottery_id,random_soft_drink_id])




