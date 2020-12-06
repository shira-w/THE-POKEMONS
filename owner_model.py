from connect_to_sql import connection
from connect_to_sql import execute_connection_and_query
import pokimon_model
import trainer_model
from pymysql import IntegrityError


def delete_pokemon_from_trainer(pokimon_name, trainer_name):
    trainer_id=trainer_model.get_id_by_name(trainer_name)
    pokimon_id=pokimon_model.get_id(pokimon_name)
    query_string=f"DELETE FROM Ownedby\
        WHERE trainer_id='{trainer_id}' and \
            pokimon_id='{pokimon_id}'"
    execute_connection_and_query(query_string,True)
    
  
def update(trainer_name, pokemon_name,envalved_id):
    try:
        pokemon_id=pokimon_model.get_id(pokemon_name)
        trainer_id=trainer_model.get_id_by_name(trainer_name)
        query_string= f"UPDATE OwnedBy SET pokimon_id ={envalved_id} \
                        WHERE pokimon_id={pokemon_id} and trainer_id ={trainer_id} "
        execute_connection_and_query(query_string,True)
    except IntegrityError:
        return ("9 - Couldn't find the pokemon or the trainer")

def get_satiety_level(pokemon_name,trainer_name):
    pokemon_id=pokimon_model.get_id(pokemon_name)
    trainer_id=trainer_model.get_id_by_name(trainer_name)
    query_string=f"SELECT satiety_level FROM Ownedby \
        WHERE pokimon_id='{pokemon_id}' \
            and trainer_id='{trainer_id}'"
    satiety_level=execute_connection_and_query(query_string)[0]["satiety_level"]
    return satiety_level

def update_satiety_level(pokemon_name,trainer_name,satiety_level):
    pokemon_id=pokimon_model.get_id(pokemon_name)
    trainer_id=trainer_model.get_id_by_name(trainer_name)
    query_string=f"UPDATE Ownedby SET satiety_level={satiety_level} \
        WHERE pokimon_id='{pokemon_id}'\
            and trainer_id='{trainer_id}'"
    execute_connection_and_query(query_string,True)

