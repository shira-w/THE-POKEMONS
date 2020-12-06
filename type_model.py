from connect_to_sql import connection
from connect_to_sql import execute_connection_and_query
from pymysql import IntegrityError

def insert_type(pokemon_types):
    try:
        for type_ in pokemon_types:
            query_string = f"INSERT INTO Type values(null, '{type_}')"
            execute_connection_and_query(query_string)
    except IntegrityError:
        raise ValueError("8 - Error")