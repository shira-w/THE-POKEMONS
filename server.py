import json

import trainer_model
import pokimon_model
import owner_model
import type_model

from flask import Flask,request, Response
app=Flask(__name__)

@app.route('/')
def wellcome():
    return ("POKIMONS===================Yes. We. Here")
    

@app.route('/evolve/<pokemon_name>/<trainer_name>',methods=["PATCH"])
def evolve_pokemon(pokemon_name,trainer_name):
    exist = trainer_model.is_pokemon_belong_trainer(pokemon_name, trainer_name)
    if not exist:
        return ("1 - not belong to this trainer")
    evolved_name, evolved_id = pokimon_model.get_evolved_pokemon(pokemon_name)
    exist = trainer_model.is_pokemon_belong_trainer(evolved_name, trainer_name)
    if exist:
        owner_model.delete_pokemon_from_trainer(pokemon_name, trainer_name)
        return("2 - the trainer already have this pokemon and deleted")   

    exist = pokimon_model.is_pokemon_exist(evolved_name)
    if not exist:
        pokemon_info = pokimon_model.get_pokemon_info(evolved_name)
        pokimon_model.insert_pokemon(pokemon_info)
        type_model.insert_type(pokemon_info["types"])
    owner_model.update(trainer_name,pokemon_name,evolved_id)
    return ("3 - the pokemon evolved successfully"),200

# @app.route('/types/<pokimon_name>', methods=["PATCH"])
# def update_types(pokimon_name):
#     # url="https://pokeapi.co/api/v2/pokemon/"
#     pass


# Get pokemons by trainer: get all the pokemons of a given owner
@app.route('/pokimons/trainer_name/<trainer_name>')
def pokimons_of_trainer(trainer_name):
    trainer_city=request.args.get('city')
    if trainer_city:
        trainer_id=trainer_model.get_id(trainer_name,trainer_city)
        return json.dumps({"pokimons:":trainer_model.get_pokimons_by_id(trainer_id)})
    else:
        return json.dumps({"pokimons:":trainer_model.get_pokimons_by_name(trainer_name)})

# Get trainers of a pokemon: get all the trainers of a given pokemon
@app.route('/trainers/pokimon_name/<pokimon_name>')
def trainers_of_pokimon(pokimon_name):
    return json.dumps({"trainers:":pokimon_model.get_trainers(pokimon_name)})

# @app.route('/pokemon', methods=["POST"])
# def add_pokemon():
#     new_pokemon = request.get_json()
#     try:
#         pokimon.insert_pokemon(new_pokemon)
#     except ValueError as e:
#         return Response(str(e)), 403
#     try:
#         pokimon.insert_type(new_pokemon["types"], new_pokemon["name"]) 
#     except Exception as e:
#         return Response(str(e)), 500
#     return Response("12 - The pokemon added successfully"), 201

@app.route('/delete/<pokemon_name>/<trainer_name>', methods=["DELETE"])
def delete_pokemon(pokemon_name, trainer_name):
    try:
        owner_model.delete_pokemon_from_trainer(pokemon_name, trainer_name)
        return Response("11 - The Pokemon deleted successfully"), 202
    except Exception as e:
        return Response(str(e)), 500




# @app.route('/careOfPokemon/<pokemon_id>/<trainer_name>/<action>', methods=['PATCH'])
# def careOfPokemon(pokemon_id, trainer_name):
#     care = 0
#     exist = trainer_model.is_pokemon_belong_trainer(pokemon_id, trainer_name)
#     if not exist:
#         return ("not belong to this trainer"), 400
#         care = owner_model.get_care(pokemon_id, trainer_name)
    
    
#         owners.increase_care(pokemon_id, trainer_name, action, care)

#     if care > 10:
#         evolve_pokemon(pokemon_id, trainer_name)
#         return Response("great!! Your Pokemon has evolved it is stronger now !!")
#     return Response("good!! continue care about your pokemon!!")

port_numbers = 3000
if __name__ == "__main__":
    app.run(port=port_numbers)