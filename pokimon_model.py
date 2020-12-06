from connect_to_sql import connection
from connect_to_sql import execute_connection_and_query
import requests
from pymysql import IntegrityError
import json

def get_trainers(pokimon_name):
    query_string=f"SELECT Trainer.name \
        FROM Ownedby Join Pokimon On pokimon_id=Pokimon.id\
            Join Trainer On trainer_id=Trainer.id\
        WHERE Pokimon.name='{pokimon_name}'"
    result=execute_connection_and_query(query_string)
    trainers_names=list(map(lambda x: x["name"],result))
    return trainers_names

def get_id(name):
    query_string=f"SELECT id FROM Pokimon \
        WHERE name='{name}'"
    id=execute_connection_and_query(query_string)[0]["id"]
    return id

def get_evolved_pokemon(pokemon_name):
    try:
        pokemon_info_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        pokemon_species_url = requests.get(url=pokemon_info_url, verify=False).json()["species"]["url"]
        evolution_chain_url = requests.get(url=pokemon_species_url, verify=False).json()["evolution_chain"]["url"]
        evolved = requests.get(url=evolution_chain_url, verify=False).json()
        if not evolved["chain"]["evolves_to"]:
            return ("the pokemon is not evolve")
        evolved_name = evolved["chain"]["evolves_to"][0]["species"]["name"]
        evolved_id = evolved["chain"]["evolves_to"][0]["species"]["url"]
        evolved_id = evolved_id[-3:-1:]
        return evolved_name, int(evolved_id[1:])
    except Exception:
        return ("5 - Couldn't find this pokemon")


def is_pokemon_exist(pokemon_name):
    try:
        query_string = f"SELECT id FROM Pokimon WHERE name = '{pokemon_name}'"
        result=execute_connection_and_query(query_string)
        if not result:
            return False
        return True
    except IntegrityError:
        raise ValueError("7 - Couldn't find the pokemon")

def get_pokemon_info(evolved_name):
    try:
        pokemon_info_url = f"https://pokeapi.co/api/v2/pokemon/{evolved_name}"
        pokemon_info = requests.get(url=pokemon_info_url, verify=False).json()
        print("pokemon_info")
        return pokemon_info
    except Exception:
        return "error"


def insert_pokemon(new_pokemon):
    try:
        query_string = f"INSERT INTO Pokemon(p_id, p_name, height, weight)\
                        Values('{new_pokemon['id']}', '{new_pokemon['name']}',\
                             '{new_pokemon['types'][0]}', '{new_pokemon['height']}',\
                                  '{new_pokemon['weight']}')"
        execute_connection_and_query(query_string,True)
    except IntegrityError:
        return("15 - The Pokemon alreadt exist")