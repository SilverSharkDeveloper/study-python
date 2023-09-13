from crud import save, find_all, update, delete,find_by_id,find_all_by_name
#
insert_query = "insert into tbl_member(member_id, member_password, member_name)" \
               "values(%s, %s, %s)"

insert_param = ['hds1234', '1234', '한동석']

info = save(insert_query, insert_param)

#
# # 전체 조회
# find_all_query = "select * from tbl_member"

# infos = find_all(find_all_query)
# print(infos)

# 아이디가 'hds1234'인 회원의 이름을 '한동숙'으로 수정
# update_query = "update tbl_member set member_name = %s where member_id = %s"
# updqte_params = ['한동숙','hds1234']
#
# update(update_query,updqte_params)
#
# infos = find_all(find_all_query)
# print(infos)
#
# # 이름이 '이순신'인 회원 삭제
# delete_query = "delete from tbl_member where member_name = %s"
# delete_params = ['한동숙']
#
# delete(delete_query,delete_params)
# 회원 번호로 한 명 조회

# find_one_query = "select * from tbl_member where id = %s"
# find_one_params = ["4"]
#
# info = find_by_id(find_one_query,find_one_params)
#
# print(info)





find_all_by_name_query = "select * from tbl_member where member_name = %s"
find_all_by_name_params = ["한동석"]

info = find_all_by_name(find_all_by_name_query,find_all_by_name_params)
print(info)

