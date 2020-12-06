from flask import Flask, render_template, request
import os
import json
import requests
import urllib

import owner_model
from server import evolve_pokemon
from trainer_model import get_pokimons_by_name
from mako.template import Template
from to_html import write_list_html
from to_htnl_trainers import write_list_html_t
from trainer_model import get_trainers

app = Flask(__name__, static_url_path='', 
              static_folder='static', 
              template_folder='templates')

@app.route('/')
def root():return render_template('index.html')

@app.route('/select_pokemons')
def pokemon():
    food.trainer_name=request.args.get('trainer')
    write_list_html(get_pokimons_by_name(food.trainer_name))
    profilepic_filename = os.path.join(f"{food.pokemon_name}.png")
    return render_template("pokemons.html" ,profilepic_filename =profilepic_filename)


@app.route('/select_trainer')
def trainer():
    # profilepic_filename = os.path.join(f"{food.pokemon_name}.png")
    write_list_html_t(get_trainers())
    return render_template("trainers.html" )
#,profilepic_filename =profilepic_filename
@app.route('/food')
def food():
    food.pokemon_name=request.args.get('pokemon_name')
    food.counter=owner_model.get_satiety_level(food.pokemon_name,food.trainer_name)
    profilepic_filename = os.path.join(f"{food.pokemon_name}.png")
    return render_template("food.html" ,profilepic_filename=profilepic_filename)

@app.route('/potatoe')
def potato():
    food.counter += 1
    profilepic_filename = os.path.join(f"{food.pokemon_name}.png")
    if food.counter %16 ==0:
        evolve_pokemon(food.pokemon_name,food.trainer_name)
        return render_template("pokemons.html" ,profilepic_filename  =profilepic_filename)
    return render_template("food.html" ,profilepic_filename  =profilepic_filename)

@app.route('/pizza')
def pizza():
    profilepic_filename = os.path.join(f"{food.pokemon_name}.png")
    food.counter +=2
    if food.counter %16 ==0:
        evolve_pokemon(food.pokemon_name,food.trainer_name)
        return render_template("pokemons.html" ,profilepic_filename  =profilepic_filename)
    return render_template("food.html" ,profilepic_filename  =profilepic_filename)

@app.route('/fish')
def fish():
    profilepic_filename = os.path.join(f"{food.pokemon_name}.png")
    food.counter += 3
    if food.counter %16 ==0:
        evolve_pokemon(food.pokemon_name,food.trainer_name)
        return render_template("pokemons.html" ,profilepic_filename  =profilepic_filename)
    return render_template("food.html" ,profilepic_filename  =profilepic_filename)

@app.route('/save_eat')
def save():
    profilepic_filename = os.path.join(f"{food.pokemon_name}.png")
    owner_model.update_satiety_level(food.pokemon_name,food.trainer_name,food.counter)
    return render_template("pokemons.html" ,profilepic_filename  =profilepic_filename)

@app.route('/finish_pokimon')
def finish_pokimon():
    profilepic_filename = os.path.join(f"{food.pokemon_name}.png")
    return render_template("trainers.html" ,profilepic_filename  =profilepic_filename)

@app.route('/shaw')
def show_image():
    try:
        food.pokemon_name=request.args.get('pokemon_name')
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(food.pokemon_name)
        pokemon = requests.get(url=pokemon_url, verify=False).json()
        # image_url = pokemon["sprites"]["other"]["official-artwork"]["front_default"]
        image_url = pokemon["sprites"]["front_default"]
        # webbrowser.open_new(image_url)
        fullfilename = os.path.join("static", f"{food.pokemon_name}.png")
        # urllib.urlretrieve(url, fullfilename)
        urllib.request.urlretrieve(image_url, fullfilename)
        profilepic_filename = os.path.join(f"{food.pokemon_name}.png")
        return render_template("food.html" ,profilepic_filename  =profilepic_filename)
    except Exception as e:
        return json.dumps(e), 500
        
if __name__ == '__main__':
    food.counter = 0
    food.trainer_name=""
    food.pokemon_name=""
    food.pokimons_trainer=[]
    app.run(port=3000)