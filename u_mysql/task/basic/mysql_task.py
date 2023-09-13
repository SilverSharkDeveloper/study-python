
import q_api.sms.sms as sms
import u_mysql.crud as db
import q_api.email_send as em
import q_api.papago as papago
import q_api.ocr as ocr

main_menu = "안녕하세요 silvershark 서비스센터 입니다. 메뉴를 선택해주세요\n1.회원가입\n2.로그인\n3.나가기"
login_menu = "서비스 선택해주세요 \n1.비밀번호 변경 \n2.한국어를 영어로 번역\n3.지금까지 나의 번역 내용 보기\n4.이미지 ocr" \
             "저장하기\n5.내가 저장한 ocr보기\n6.나가기(로그아웃)"

input_id = "아이디 입력해주세여"
input_password = "비밀번호를 입력해주세여"
input_new_password = "새로운 비밀번호를 입력해주세여"
input_name = "이름을 입력해주세여"
input_phone = "핸드폰 번호를 입력해주세여"
input_code = "전송 받은 코드를 입력해주세요"
input_sentence = "번역할 문장을 입력해주세요"
input_ocr = "이미지의 url을 입력해주세요"



email_success = "가입하신 이메일로 인증번호 10자리가 전송되었습니다."
email_permit_success = "인증이 완료되었습니다.."
phone_success = "인증이 완료되었습니다."
join_success = "회원가입이 완료되었습니다."
login_success = "로그인 성공"
change_password_success = "비밀번호 변경 성공했습니다."
papago_success = "번역에 성공했습니다 db에 저장합니다."
ocr_success = "ocr 성공했습니다. db에 저장합니다."


phone_failed = "인증번호가 틀렸습니다. 다시 입력해주세요."
login_failed = "로그인 실패"
email_permit_failed = "인증에 실패하셨습니다."
papago_failed ="번역에 실패했습니다."
ocr_failed ="ocr 불러오기 실패했습니다."


duplicate_error = "이미 가입되어있는 id 입니다."
phone_error = "전송되지 않았습니다, 다시 입력해주세요"


while True:
    choice = int(input(main_menu))

    if choice ==3 :
        break

    elif choice ==2:
        # 로그인
        flag = False
        member_id = None
        in_id = input(input_id)
        in_password = input(input_password)
        query = "select id,member_id, member_password from tbl_member"
        ids = db.find_all(query)
        for id in ids:
            if id["member_id"] == in_id and id["member_password"] == in_password:
                member_id = id["id"]
                flag =True
                print(login_success)
        if flag:
            while True:

                choice = int(input(login_menu))
                if choice== 6:
                    break
                # 회원 비밀번호 변경(EMAIL API) - 랜덤한 인증번호 10자리 발송 후 검사
                elif choice==1:
                    while True:
                        code = em.send_email(in_id)
                        print(email_success)
                        in_code = input(input_code)
                        if in_code == code:
                            print(email_permit_success)
                            new_password = input(input_new_password)
                            query = "update tbl_member set member_password =%s where id = %s"
                            update_param = [new_password, member_id]
                            db.update(query, update_param)
                            print(change_password_success)
                            break
                        else:
                            print(email_permit_failed)
                            continue

                elif choice == 2:
                    # 사용자가 입력한 문장을 영어로 번역
                    sentence = input(input_sentence)
                    result = papago.papago_api(sentence)
                    if not result:
                        print(papago_failed)

                    else:
                        # 한국어와 번역된 문장을 DBMS에 저장
                        query = f"INSERT INTO app.tbl_papago(original_sentence, translated_sentence, member_id)VALUES" \
                                f"(%s, %s,%s);"
                        params = [sentence, result, member_id]
                        db.save(query, params)
                        print(papago_success)
                # 번역 내역 조회
                elif choice ==3:
                    query = "select p.original_sentence ,p.translated_sentence  from tbl_papago p join tbl_member m " \
                            "on p.member_id = m.id and m.id = %s"
                    params = [member_id]
                    results = db.find_all_by_member_id(query,params)
                    for result in results:
                        print(f"번역전 : {result['original_sentence']} 번역후 : {result['translated_sentence']}")

                elif choice ==4:
                    url = input(input_ocr)
                    result = ocr.get_text(url)
                    if result:
                        query = "INSERT INTO app.tbl_ocr(image_url, ocr_texts, member_id)" \
                                "VALUES(%s, %s, %s)"
                        params = [url,result,member_id]
                        db.save(query,params)
                        print(ocr_success)
                    else:
                        print(ocr_failed)

                elif choice ==5:
                    query = "select image_url,ocr_texts from tbl_ocr o join tbl_member m " \
                            "on m.id = o.member_id and m.id = %s"
                    params = [member_id]
                    results = db.find_all_by_member_id(query,params)
                    for result in results:
                        print(f"url : {result['image_url']} \n ocr결과 : {result['ocr_texts']}")


        else:
            print(login_failed)

    # 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)

    elif choice == 1:
        while True:
            # 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
            new_phone = input(input_phone)
            code, response = sms.sms(new_phone)

            if response.status_code != 200:
                print(phone_error)
                continue
            else:
                while True:
                    new_code = input(input_code)
                    if code == new_code:
                        print(phone_success)
                        break
                    else:
                        print(phone_failed)

            while True:
                # 아이디 중복검사
                flag = False
                new_id = input(input_id)
                query = "select member_id from tbl_member"
                ids = db.find_all(query)

                for id in ids:
                    if id["member_id"] == new_id:
                        print(duplicate_error)
                        flag = True
                        break
                if flag:
                    continue
                else:
                    new_password = input(input_password)
                    new_name = input(input_name)
                    insert_query = "insert into tbl_member(member_id, member_password, member_name)" \
                                   "values(%s, %s, %s)"
                    insert_param = [new_id, new_password, new_name]
                    db.save(insert_query, insert_param)
                    break
            print(join_success)
            break
