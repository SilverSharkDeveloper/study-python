# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = "gongcha"
menu = "1추가하기\n2수정하기\n3삭제하기\n4검색하기\n5목록보기\n6나가기\n"



while True :
    is_exist = False;
    choice = int(input(menu))
    if choice==1 :
        new_menu = input("추가할 메뉴를 입력해주세요 : ")
        for name in name_list :
            if(name == new_menu) :
                print("이미 존재하는 메뉴 입니다. 메뉴로 돌아갑니다.")
                is_exist = True
                break
        if not is_exist :
            price = int(input("메뉴의 가격을 정해주세요 : "))
            name_list.append(new_menu)
            price_list.append(price)
            print("추가가 완료되었습니다.")
    elif choice==2 :
        search_menu = input("수정할 상품명을 적어주세요!")
        for name in name_list :
            if name == search_menu :
                new_name = input("새로운 상품명과 가격을 입력해주세요!\n수정할 상품명 :")
                #중복처리
                for already_name in name_list :
                    if already_name == new_name :
                        print("이미 존재하는 상품명입니다.")
                        is_exist = True
                        break

                if not is_exist :
                    new_price = int(input("수정할 가격"))
                    price_list[name_list.index(name)] = new_price
                    name_list[name_list.index(name)] = new_name

                    print("수정이 완료되었습니다.")

                    is_exist = True
                    break
        if not is_exist :

            print("존재하지 않는 메뉴입니다!")

    elif choice==3 :
        del_menu = input("삭제할 상품명을 입력해주세요 : ")
        for name in name_list:
            if (del_menu == name):
                del (price_list[name_list.index(name)])
                name_list.remove(name)

                print(f"{del_menu}삭제에 성공했습니다! 메뉴로 돌아갑니다.")
                is_exist = True
                break
        if not is_exist:

            print("존재하지 않는 상품입니다.")

    elif choice==4 :
        choice2 = int(input("어떤 걸로 검색하실래요?\n1.상품명\n2.가격"))
        if choice2 == 1 :
            search_menu = input("검색할 상품명을 적어주세요 : ")
            for name in name_list :
                if search_menu == name :
                    print(f"{search_menu}는 {price_list[(name_list.index(search_menu))]}원 입니다.")
                    is_exist =True
                    break
            if not is_exist :
                print("검색하신 상품이 존재하지 않습니다. 메뉴로 돌아갑니다.")
        else :
            search_price = int(input("상품 가격을 적어주세요! +=50%까지 모든 상품이 검색됩니다."))
            index = 0
            search_price_list =[]
            for price in price_list:
                if search_price/2 <= price <= search_price*1.5:
                    search_price_list.append(name_list[index])
                index +=1
            print(f"{search_price/2}~{search_price*1.5}사이 가격인 상품들은 다음과 같습니다.\n"
                  f"{search_price_list}\n"
                  f"메인 메뉴로 돌아갑니다.")
    elif choice==5 :
        for name in name_list :
            print(f"{name} : {price_list[name_list.index(name)]}")
            is_exist = True
        if not is_exist :
            print("상품이 하나도 없습니다 추가해주세요!")
    elif choice==6 :

        print("프로그램을 종료합니다.")
        break
    else :
        print("잘못 입력하셨습니다. 다시 선택해주세요")


