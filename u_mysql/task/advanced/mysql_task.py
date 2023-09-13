from crud import *
from random import randint

# 학부모 회원가입
# insert_query = "insert into tbl_parent(parent_name, parent_age, parent_address, parent_phone, parent_gender) " \
#                "values(%s, %s, %s, %s, %s)"
# name = input('이름: ')
# age = input('나이: ')
# address = input('주소: ')
# phone = input('핸드폰 번호: ')
# gender = input('성별: ')
#
# parent_datas = [name, age, address, phone, gender]
#
# parent_id = save_with_seq(insert_query, parent_datas).get('seq')
# print(parent_id)
#
# # 아이가 있다면 아이의 정보까지 입력
# insert_query = "insert into tbl_child(child_name, child_age, child_gender, parent_id) " \
#                "values(%s, %s, %s, %s)"
#
# while True:
#     choice = input("아이 정보를 입력하시겠습니까?[y/N]\n")
#     if choice == 'N':
#         break
#     child_name = input("아이 이름: ")
#     child_age = input("아이 나이: ")
#     child_gender = input("아이 성별: ")
#     child_datas = [child_name, child_age, child_gender, parent_id]
#
#     save(insert_query, child_datas)

# 로그인(학부모 이름, 학부모 휴대폰 번호)
# login_query = "select id from tbl_parent where parent_name = %s and parent_phone = %s"
# parent_name = input("학부모 이름: ")
# parent_phone = input("학부모 핸드폰 번호: ")
#
# parent_id = login(login_query, [parent_name, parent_phone]).get('id')
# if parent_id:
# 로그인된 학부모의 아이 정보 출력
# find_by_id_query = "select child_name, child_age, child_gender from tbl_child where parent_id = %s"
# children = find_all_by_id(find_by_id_query, parent_id)
#
# for child in children:
#     print(child)

# 아이의 정보 중 나이를 수정하기(아이 고유 번호를 이용)
#     update_query = "update tbl_child set child_age = %s where id = %s"
#     child_id = int(input("정보를 수정할 아이를 선택하세요."))
#     child_age = int(input("나이: "))
#     update(update_query, [child_age, child_id])

# 새로운 아이 정보 추가
# insert_query = "insert into tbl_child(child_name, child_age, child_gender, parent_id) " \
#                "values(%s, %s, %s, %s)"
#
# while True:
#     choice = input("아이 정보를 입력하시겠습니까?[y/N]\n")
#     if choice == 'N':
#         break
#     child_name = input("아이 이름: ")
#     child_age = input("아이 나이: ")
#     child_gender = input("아이 성별: ")
#     child_datas = [child_name, child_age, child_gender, parent_id]
#
#     save(insert_query, child_datas)


# 인가(Authorization): 권한 부여
# insert_query = "insert into tbl_parent(parent_name, parent_age, parent_address, parent_phone, parent_gender, parent_type) " \
#                "values(%s, %s, %s, %s, %s, %s)"
# name = input('이름: ')
# age = input('나이: ')
# address = input('주소: ')
# phone = input('핸드폰 번호: ')
# gender = input('성별: ')
# type = 'admin'
#
# parent_datas = [name, age, address, phone, gender, type]
#
# save(insert_query, parent_datas)


# 체험학습 등록(관리자만 가능)
# login_query = "select id, parent_type from tbl_parent where parent_name = %s and parent_phone = %s"
# parent_name = input("학부모 이름: ")
# parent_phone = input("학부모 핸드폰 번호: ")
#
# parent = login(login_query, [parent_name, parent_phone])
# parent_id = parent.get('id')
# parent_type = parent.get('parent_type')
#
# if parent_id and parent_type == 'admin':
#     insert_query = "insert into tbl_field_trip(field_trip_title, field_trip_content, field_trip_number) " \
#                    "values(%s, %s, %s)"
#
#     field_trip_title = input("체험학습 제목: ")
#     field_trip_content = input("체험학습 내용: ")
#     field_trip_number = int(input("체험학습 최대 인원 수: "))
#
#     save(insert_query, [field_trip_title, field_trip_content, field_trip_number])

# 체험학습 지원
# login_query = "select id from tbl_parent where parent_name = %s and parent_phone = %s"
# parent_name = input("학부모 이름: ")
# parent_phone = input("학부모 핸드폰 번호: ")
#
# parent_id = login(login_query, [parent_name, parent_phone]).get('id')
# if parent_id:
#     find_all_query = "select id, field_trip_title, field_trip_content, field_trip_number, ifnull(child_count, 0) child_count, ifnull(field_trip_number - a.child_count, field_trip_number) rest_number " \
#                      "from tbl_field_trip ft " \
#                      "left outer join " \
#                      "(" \
#                      "select field_trip_id, count(child_id) child_count " \
#                      "from tbl_apply " \
#                      "group by field_trip_id " \
#                      ") a " \
#                      "on a.field_trip_id = ft.id"
#
#     field_trips = find_all(find_all_query)
#     number = 0

#     for field_trip in field_trips:
#         number += 1
#         print(str(number) + ". " + str(field_trip))
#
#     field_trip_choice = int(input("번호: "))
#     # 지원 가능 검사
#     if field_trips[field_trip_choice - 1].get('rest_number') != 0:
#         field_trip_id = field_trips[field_trip_choice - 1].get('id')
#
#     else:
#         print("모집이 마감된 체험학습입니다.")
#         field_trip_id = None
#
#     if field_trip_id:
#         find_by_id_query = "select id, child_name, child_age, child_gender from tbl_child where parent_id = %s"
#         children = find_all_by_id(find_by_id_query, parent_id)
#         child_ids = []
#         while True:
#             number = 0
#             for child in children:
#                 number += 1
#                 print(str(number) + ". " + str(child))
#
#             choice = input("보낼 아이 번호를 입력하세요[종료: q]\n")
#             if choice == 'q':
#                 break
#
#             choice = int(choice)
#             child_ids.append(children[choice - 1].get('id'))
#
#         # 지원자 수 검사
#         if len(child_ids) <= field_trips[field_trip_choice - 1].get('rest_number'):
#             # 지원
#             for child_id in child_ids:
#                 insert_query = "insert into tbl_apply(child_id, field_trip_id) " \
#                                "values(%s, %s)"
#
#                 save(insert_query, [child_id, field_trip_id])
#
#             print("지원 드디어 완료!")
#
#         else:
#             print("지원 가능 인원 수를 초과하였습니다.")

# 음료수 등록
save_query = "insert into tbl_soft_drink(soft_drink_name, soft_drink_price) " \
             "values(%s, %s)"

for i in range(10):
    save(save_query, [f'음료수{i + 1}', 3000 + i * 200])


# 상품 등록
save_query = "insert into tbl_product(product_name) " \
             "values(%s)"

for i in range(20):
    save(save_query, [f'상품{i + 1}'])

# 당첨 번호 등록
get_count_product_query = "select count(id) product_count from tbl_product"

find_all_query = "select id from tbl_product"
products = find_all(find_all_query)
products_ids = []
for product in products:
    products_ids.append(product.get('id'))

save_query = "insert into tbl_lottery(product_id) " \
             "values(%s)"

for i in range(30):
    index = randint(0, get_count(get_count_product_query).get('product_count') - 1)
    random_product = products_ids[index]
    save(save_query, random_product)

# 100개 유통
# 음료수 랜덤, 당첨번호 랜덤
get_count_soft_drink_query = "select count(id) soft_drink_count from tbl_soft_drink"
get_count_lottery_query = "select count(id) lottery_count from tbl_lottery"

find_all_soft_drink_query = "select id from tbl_soft_drink"
find_all_lottery_query = "select id from tbl_lottery"

soft_drinks = find_all(find_all_soft_drink_query)
lotteries = find_all(find_all_lottery_query)

soft_drink_ids = []
lottery_ids = []

for soft_drink in soft_drinks:
    soft_drink_ids.append(soft_drink.get('id'))

for lottery in lotteries:
    lottery_ids.append(lottery.get('id'))

save_query = "insert into tbl_circulation(soft_drink_id, lottery_id) " \
             "values(%s, %s)"

# 확률
# 단위 정하기: 10단위
rating_box = [0] * 10
rating = 30
for i in range(rating // 10):
    rating_box[i] = 1

for i in range(100):
    random_index = randint(0, 9)
    soft_drink_index = randint(0, get_count(get_count_soft_drink_query).get('soft_drink_count') - 1)
    lottery_index = randint(0, get_count(get_count_lottery_query).get('lotterys_count') - 1)

    random_soft_drink = soft_drink_ids[soft_drink_index]
    random_lottery = lottery_ids[lottery_index]

    # 70% 확률
    if rating_box[random_index] == 0:
        random_lottery = None

    save(save_query, [random_soft_drink, random_lottery])