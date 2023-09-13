import pymysql
from pymysql.cursors import Cursor


def connect():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='app', charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor


def execute_crud(execute):
    result = None

    def manage(*args):
        nonlocal result
        conn, cursor = connect()
        try:
            result = execute(cursor, *args)
            conn.commit()
        except Exception as e:
            print(e.__str__())
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

        return result

    return manage


@execute_crud
def save_with_seq(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
    cursor.execute('select last_insert_id() seq')
    return cursor.fetchone()


@execute_crud
def save(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)


@execute_crud
def find_all(cursor: Cursor, query: str):
    cursor.execute(query)
    return cursor.fetchall()


@execute_crud
def find_by_id(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
    return cursor.fetchone()


@execute_crud
def find_all_by_id(cursor: Cursor, query: str, parent_id: int):
    print(type(parent_id))
    cursor.execute(query, parent_id)
    return cursor.fetchall()


@execute_crud
def find_by_member_id(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
    return cursor.fetchone()


@execute_crud
def find_by_member_email(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
    return cursor.fetchone()


@execute_crud
def find_count_apply(cursor: Cursor, query: str):
    cursor.execute(query)
    return cursor.fetchall()


@execute_crud
def get_count(cursor: Cursor, query: str):
    cursor.execute(query)
    return cursor.fetchone()


@execute_crud
def login(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
    return cursor.fetchone()


@execute_crud
def update(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)


@execute_crud
def delete(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)