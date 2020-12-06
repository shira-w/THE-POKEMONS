import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="sql_intro",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")


def execute_connection_and_query(query_string, insert=False):
    with connection.cursor() as cursor:
        cursor.execute(query_string)
        if insert:
            connection.commit()
        else:
            result = cursor.fetchall()
            return result
