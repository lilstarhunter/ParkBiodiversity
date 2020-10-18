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


@app.route("/parkmap/animal")
def animal_map():
    with engine.connect() as connection:
        result = connection.execute("SELECT ParkName, Category FROM species WHERE Category = 'Mammal'")
        results_as_list = result.fetchall()

        animal_data = []
    for ParkName, Category  in results_as_list:
        p_dict = {}
        p_dict["ParkName"] = ParkName
        p_dict["Category"] = Category
        animal_data.append(p_dict)

    return jsonify(animal_data)

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

# @app.route("/api/v1.0/insect_biodiv")
# def insect_biodiv():
#     with engine.connect() as connection:
#         result = connection.execute("SELECT state, category  FROM merge WHERE category IN ('Vascular Plant', 'Nonvascular Plant') Order BY state")
#         results_as_list = result.fetchall()

#         plant_biodiv_data = []
#     for state, category  in results_as_list:
#         p_dict = {}
#         p_dict["State"] = state
#         p_dict["Category"] = category
#         plant_biodiv_data.append(p_dict)

#     return jsonify(plant_biodiv_data)

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
