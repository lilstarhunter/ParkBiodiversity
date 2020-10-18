import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlite3
import csv
from collections import defaultdict
import json

from flask import Flask, jsonify, render_template


#################################################
# Database Setup
#################################################

# connect to the database
engine = create_engine("sqlite:///new.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# reference db table
Parks = Base.classes.parks
Species = Base.classes.species

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return render_template('index_park.html')


# Map #1 State Parks radius based on acres
@app.route("/parkmap")
def park_map():
    session = Session(engine)
    # return all results
    parks_data = session.query(Parks.ParkCode, Parks.ParkName,
                               Parks.State, Parks.Acres, Parks.Latitude, Parks.Longitude).all()

    session.close()

    all_parks_data = []
    for ParkCode, ParkName, State, Acres, Latitude, Longitude in parks_data:
        p_dict = {}
        p_dict["ParkCode"] = ParkCode
        p_dict["ParkName"] = ParkName
        p_dict["State"] = State
        p_dict["Acres"] = Acres
        p_dict["Latitude"] = Latitude
        p_dict["Longitude"] = Longitude
        all_parks_data.append(p_dict)

    return jsonify(all_parks_data)

# Map #2 Animal Biodiversity
@app.route("/api/v1.0/animal_biodiv")
def animal_biodiv():
    with engine.connect() as connection:
        result = connection.execute("SELECT state, category  FROM merge WHERE category IN ('Mammal', 'Bird', 'Reptile', 'Amphibian', 'Fish', 'Crab/Lobster/Shrimp', 'Invertebrate') Order BY state")
        results_as_list = result.fetchall()

        animal_biodiv_data = []
    for ParkName, Category  in results_as_list:
        p_dict = {}
        p_dict["ParkName"] = ParkName
        p_dict["Category"] = Category
        animal_biodiv_data.append(p_dict)

    return jsonify(animal_biodiv_data)
# Map #3 Plant Biodiversity
@app.route("/api/v1.0/plant_biodiv")
def plant_biodiv():
    with engine.connect() as connection:
        result = connection.execute("SELECT state, category  FROM merge WHERE category IN ('Vascular Plant', 'Nonvascular Plant') Order BY state")
        results_as_list = result.fetchall()

        plant_biodiv_data = []
    for state, category  in results_as_list:
        p_dict = {}
        p_dict["State"] = state
        p_dict["Category"] = category
        plant_biodiv_data.append(p_dict)

    return jsonify(plant_biodiv_data)
# Map #4 Insect Biodiversity
@app.route("/api/v1.0/insect_biodiv")
def insect_biodiv():
    with engine.connect() as connection:
        result = connection.execute("SELECT state, category  FROM merge WHERE category IN ('Spider/Scorpion', 'Insect', 'Slug/Snail' ) Order BY state")
        results_as_list = result.fetchall()

        insect_biodiv_data = []
    for state, category  in results_as_list:
        p_dict = {}
        p_dict["State"] = state
        p_dict["Category"] = category
        insect_biodiv_data.append(p_dict)

    return jsonify(insect_biodiv_data)
# Map #5 Fungi Biodiversity
@app.route("/api/v1.0/fungi_biodiv")
def fungi_biodiv():
    with engine.connect() as connection:
        result = connection.execute("SELECT state, category  FROM merge WHERE category IN ('Fungi', 'Algae') Order BY state")
        results_as_list = result.fetchall()

        fungi_biodiv_data = []
    for state, category  in results_as_list:
        p_dict = {}
        p_dict["State"] = state
        p_dict["Category"] = category
        fungi_biodiv_data.append(p_dict)

    return jsonify(fungi_biodiv_data)
# Scatter Plot #1 Park Acres x Total # Animals
@app.route("/api/v1.0/scatter_animals")
def scatter_animals():
    with engine.connect() as connection:
        result = connection.execute("SELECT name, category  FROM merge WHERE category IN ('Mammal', 'Bird', 'Reptile', 'Amphibian', 'Fish', 'Crab/Lobster/Shrimp', 'Invertebrate') Order BY name")
        results_as_list = result.fetchall()

        scatter_animals_data = []
    for name, category  in results_as_list:
        p_dict = {}
        p_dict["Name"] = name
        p_dict["Category"] = category
        scatter_animals_data.append(p_dict)

    return jsonify(scatter_animals_data)
# Scatter Plot #2 Park Acres x Total # Plants
@app.route("/api/v1.0/scatter_plants")
def scatter_plants():
    with engine.connect() as connection:
        result = connection.execute("SELECT name, category  FROM merge WHERE category IN ('Vascular Plant', 'Nonvascular Plant') Order BY name")
        results_as_list = result.fetchall()

        scatter_plants_data = []
    for name, category  in results_as_list:
        p_dict = {}
        p_dict["Name"] = name
        p_dict["Category"] = category
        scatter_plants_data.append(p_dict)

    return jsonify(scatter_plants_data)

# Scatter Plot #3 Park Acres x Total # Insects
@app.route("/api/v1.0/scatter_insects")
def scatter_insects():
    with engine.connect() as connection:
        result = connection.execute("SELECT name, category  FROM merge WHERE category IN ('Spider/Scorpion', 'Insect', 'Slug/Snail') Order BY name")
        results_as_list = result.fetchall()

        scatter_insects_data = []
    for name, category  in results_as_list:
        p_dict = {}
        p_dict["Name"] = name
        p_dict["Category"] = category
        scatter_insects_data.append(p_dict)

    return jsonify(scatter_insects_data)
# Scatter Plot #4 Park Acres x Total # Fungi
@app.route("/api/v1.0/scatter_fungi")
def scatter_fungi():
    with engine.connect() as connection:
        result = connection.execute("SELECT name, category  FROM merge WHERE category IN ('Fungi', 'Algae') Order BY name")
        results_as_list = result.fetchall()

        scatter_fungi_data = []
    for name, category  in results_as_list:
        p_dict = {}
        p_dict["Name"] = name
        p_dict["Category"] = category
        scatter_fungi_data.append(p_dict)

    return jsonify(scatter_fungi_data)


@app.route("/api/v1.0/scatter_fungi")
def scatter_fungi():
    with engine.connect() as connection:
        result = connection.execute("SELECT name, category  FROM merge WHERE category IN ('Fungi', 'Algae') Order BY name")
        results_as_list = result.fetchall()

        scatter_fungi_data = []
    for name, category  in results_as_list:
        p_dict = {}
        p_dict["Name"] = name
        p_dict["Category"] = category
        scatter_fungi_data.append(p_dict)

    return jsonify(scatter_fungi_data)

@app.route("/api/v1.0/parks")
# MAP_PARK.HTML
def parks():
    session = Session(engine)
    # return all results
    parks_data = session.query(Parks.ParkCode, Parks.ParkName,
                               Parks.State, Parks.Acres, Parks.Latitude, Parks.Longitude).all()

    session.close()

    all_parks_data = []
    for ParkCode, ParkName, State, Acres, Latitude, Longitude in parks_data:
        p_dict = {}
        p_dict["ParkCode"] = ParkCode
        p_dict["ParkName"] = ParkName
        p_dict["State"] = State
        p_dict["Acres"] = Acres
        p_dict["Latitude"] = Latitude
        p_dict["Longitude"] = Longitude
        all_parks_data.append(p_dict)

    return jsonify(all_parks_data)


@app.route("/api/v1.0/species")
def species():
    session = Session(engine)
    # return all results
    species_data = session.query(Species.SpeciesID, Species.ParkName,
                                 Species.Category, Species.Order, Species.Family, Species.ScientificName).all()

    session.close()

    all_species_data = []
    for SpeciesID, ParkName, Category, Order, Family, ScientificName in species_data:
        s_dict = {}
        s_dict["SpeciesID"] = SpeciesID
        s_dict["ParkName"] = ParkName
        s_dict["Category"] = Category
        s_dict["Order"] = Order
        s_dict["Family"] = Family
        s_dict["ScientificName"] = ScientificName
        all_species_data.append(s_dict)

    return jsonify(all_species_data)


# open DB connection for query
# session = Session(engine)

# session.close()


# JIM CODE
# # Dump Parks data to json files


# mydict_ = defaultdict(list)

# for x in all_parks_data:
#     for k, v in x.items():
#         mydict_[k].append(v)
# mydict = dict(mydict_)


# jsonfile = r'data/parks.json'
# with open(jsonfile, 'w', encoding='utf-8') as jsonf:
#     jsonf.write(json.dumps(mydict, indent=4))

# # Dump species data to json file
# # Dump Parks data to json files

# mydict_ = defaultdict(list)

# for x in all_species_data:
#     for k, v in x.items():
#         mydict_[k].append(v)
# mydict = dict(mydict_)


# jsonfile = r'data/species.json'
# with open(jsonfile, 'w', encoding='utf-8') as jsonf:
#     jsonf.write(json.dumps(mydict, indent=4))


# # set up flask
# app = Flask(__name__)


# @app.route("/test")
# def test():
#     return render_template('basic.html')


# @app.route("/api/v1.0/species")
# def species():
#     return jsonify(species_data)
# # @app.route("/api/v1.0/species")
# # def species():

# #     all_species_data = []
# # for SpeciesID, ParkName, Category, Order, Family, ScientificName in species_data:
# #     s_dict = {}
# #     s_dict["SpeciesID"] = SpeciesID
# #     s_dict["ParkName"] = ParkName
# #     s_dict["Category"] = Category
# #     s_dict["Order"] = Order
# #     s_dict["Family"] = Family
# #     s_dict["ScientificName"] = ScientificName
# #     all_species_data.append(s_dict)

# #  mydict_ = defaultdict(list)

# # for x in all_species_data:
# #     for k, v in x.items():
# #         mydict_[k].append(v)
# #     mydict = dict(mydict_)
# # return jsonify(mydict)


if __name__ == "__main__":
    app.run(debug=True)
