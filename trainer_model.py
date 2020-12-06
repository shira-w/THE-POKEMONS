
from connect_to_sql import connection
from connect_to_sql import execute_connection_and_query
from pymysql import IntegrityError
import json

def get_id(name, city):
    query_string=f"SELECT id FROM Trainer \
        WHERE name='{name}'and city='{city}'"
    id=execute_connection_and_query(query_string)[0]["id"]
    return id

def get_id_by_name(name):
    query_string=f"SELECT id FROM Trainer \
        WHERE name='{name}'"
    id=execute_connection_and_query(query_string)[0]["id"]
    return id

def get_pokimons_by_name(trainer_name):
    query_string=f"SELECT Pokimon.name \
        FROM Ownedby Join Pokimon On pokimon_id=Pokimon.id\
             Join Trainer On trainer_id=Trainer.id\
        WHERE Trainer.name='{trainer_name}'"
    result=execute_connection_and_query(query_string)
    pokimons_names=list(map(lambda x: x["name"],result))
    return pokimons_names

def get_pokimons_by_id(trainer_id):
    query_string=f"SELECT name \
        FROM Ownedby Join Pokimon On pokimon_id=Pokimon.id\
        WHERE trainer_id='{trainer_id}'"
    result=execute_connection_and_query(query_string)
    pokimons_names=list(map(lambda x: x["name"],result))
    return pokimons_names


def is_pokemon_belong_trainer(pokemon_name, trainer_name):
    try:
        with connection.cursor() as cursor:
            query_string = f"SELECT Pokimon.name \
        FROM Ownedby Join Pokimon On pokimon_id=Pokimon.id\
             Join Trainer On trainer_id=Trainer.id\
        WHERE Pokimon.name='{pokemon_name}' and Trainer.name='{trainer_name}'"
            cursor.execute(query_string)
            result = cursor.fetchall()
            if not result:
                return False
            return True

    except IntegrityError:
        return json.dumps({"error: IntegrityError"})
        


def get_trainers():
    query_string=f"SELECT name \
        FROM Trainer"
    result=execute_connection_and_query(query_string)
    trainers_names=list(map(lambda x: x["name"],result))
    return trainers_names


