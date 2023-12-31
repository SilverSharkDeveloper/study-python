#list_task.py의 카페 로직을 dict 자료 구조로 변경


# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
dict_products = {}

title = "gongcha"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

append_error_message = "추가 실패(중복된 상품명)"
update_error_message = "수정 실패(존재하지 않는 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    choice = int(input(title + "\n" + menu))

    # 추가
    if choice == 1:
        new_name, new_price = input(append_message).split(" ")
        if new_name not in dict_products.keys():
            dict_products[new_name] = int(new_price)
        else:
            print(append_error_message)
    # 수정
    elif choice == 2:
        name = input(search_name_message_for_update)
        if name in dict_products.keys():

            new_name, new_price = input(update_message).split(" ")
            dict_products[new_name] = int(new_price)
        else:
            print(update_error_message)
    # 삭제
    elif choice == 3:
        name = input(delete_message)
        if name in dict_products.keys():
           del dict_products[name]
        else:
            print(delete_error_message)

    # 검색
    elif choice == 4:
        choice = int(input(search_menu))
        # 상품명으로 검색
        if choice == 1:
            name = input(search_name_message)
            if name in dict_products.keys():
                print(f"{name} 의 가격은 {dict_products[name]}원 입니다.")
            else:
                print(search_name_error_message)

        # 가격으로 검색
        elif choice == 2:
            check = False
            price = int(input(search_price_message))
            min = price * 0.5
            max = price * 1.5

            for name,price in dict_products.items():

                if min <= price<= max:
                    check = True
                    print(f'{name} - {price}')

            if not check:
                print(search_error_message)

        # 그 외
        else:
            print(error_message)
        pass

    # 목록
    elif choice == 5:
        if len(dict_products) == 0:
            print(no_item_message)
            continue

        for name,price in dict_products.items():
            print(f'{name} - {price}')

    # 나가기
    elif choice == 6:
        break

    # 그 외
    else:
        print(error_message)