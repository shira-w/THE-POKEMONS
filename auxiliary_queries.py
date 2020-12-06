from connect_to_sql import connection
from connect_to_sql import execute_connection_and_query

def get_type_id(type_):
    query_string=f"SELECT id FROM Type WHERE name='{type_}'"
    id=execute_connection_and_query(query_string)[0]["id"]
    return id



