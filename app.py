from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlite3
import csv
from collections import defaultdict
import json
from sqlalchemy import or_

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
Merge = Base.classes.merge

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes FRONT END
#################################################
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/parks_info")
def parkdata():
    return render_template('parkdata.html')


@app.route("/biodiversity")
def biodiversity():
    return render_template('biodiversity.html')


@app.route("/analysis")
def analysis():
    return render_template('analysis.html')


@app.route("/table")
def table():
    return render_template('table.html')

#################################################
# Flask Routes BACKEND
#################################################
# Map #1 State Parks radius based on acres


@app.route("/api/v1.0/analysis")
def biodiv_analysis():
    session = Session(engine)
    sel = [Merge.state, Merge.name, Merge.acres,
           Merge.category, func.count(Merge.category)]
    results = session.query(*sel)\
        .group_by(Merge.name).group_by(Merge.category)\
        .all()

    session.close()
    park_biodiv = []
    for state, name, acres, category, count in results:
        p_dict = {}
        p_dict["State"] = state
        p_dict["Park Name"] = name
        p_dict["Acres"] = acres
        p_dict["Category"] = category
        p_dict["Biodiversity Count"] = count
        park_biodiv.append(p_dict)
    return jsonify(park_biodiv)


@app.route("/api/v1.0/parkdata")
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

### BIODIVERSITY.HTML ###
# Map #2 Animal Biodiversity


@app.route("/api/v1.0/animal_biodiv")
def animal_biodiv():
    session = Session(engine)
    sel = [Merge.name, Merge.state, Merge.lat, Merge.lon,
           Merge.category, func.count(Merge.category)]
    results = session.query(*sel)\
        .group_by(Merge.name).filter(or_(Merge.category == 'Mammal', Merge.category == 'Bird', Merge.category == 'Reptile', Merge.category == 'Amphibian', Merge.category == 'Fish', Merge.category == 'Crab/Lobster/Shrimp', Merge.category == 'Invertebrate')).all()

    session.close()

    animal_biodiv = []
    for name, state, lat, lon, category, count in results:
        p_dict = {}
        p_dict["Park Name"] = name
        p_dict["State"] = state
        p_dict["lat"] = lat
        p_dict["lon"] = lon
        p_dict["Category"] = category
        p_dict["Biodiversity Count"] = count
        animal_biodiv.append(p_dict)
    return jsonify(animal_biodiv)

# Map #3 Plant Biodiversity


@ app.route("/api/v1.0/plant_biodiv")
def plant_biodiv():
    with engine.connect() as connection:
        result = connection.execute(
            "SELECT state, category  FROM merge WHERE category IN ('Vascular Plant', 'Nonvascular Plant') Order BY state")
        results_as_list = result.fetchall()

        plant_biodiv_data = []
    for state, category in results_as_list:
        p_dict = {}
        p_dict["State"] = state
        p_dict["Category"] = category
        plant_biodiv_data.append(p_dict)

    return jsonify(plant_biodiv_data)
# Map #4 Insect Biodiversity


@ app.route("/api/v1.0/insect_biodiv")
def insect_biodiv():
    with engine.connect() as connection:
        result = connection.execute(
            "SELECT state, category  FROM merge WHERE category IN ('Spider/Scorpion', 'Insect', 'Slug/Snail' ) Order BY state")
        results_as_list = result.fetchall()

        insect_biodiv_data = []
    for state, category in results_as_list:
        p_dict = {}
        p_dict["State"] = state
        p_dict["Category"] = category
        insect_biodiv_data.append(p_dict)

    return jsonify(insect_biodiv_data)

# Map #5 Fungi Biodiversity


@ app.route("/api/v1.0/fungi_biodiv")
def fungi_biodiv():
    with engine.connect() as connection:
        result = connection.execute(
            "SELECT state, category  FROM merge WHERE category IN ('Fungi', 'Algae') Order BY state")
        results_as_list = result.fetchall()

        fungi_biodiv_data = []
    for state, category in results_as_list:
        p_dict = {}
        p_dict["State"] = state
        p_dict["Category"] = category
        fungi_biodiv_data.append(p_dict)

    return jsonify(fungi_biodiv_data)

# Scatter Plot #1 Park Acres x Total # Animals


@ app.route("/api/v1.0/scatter_animals")
def scatter_animals():
    with engine.connect() as connection:
        result = connection.execute(
            "SELECT name, category, acres  FROM merge WHERE category IN ('Mammal', 'Bird', 'Reptile', 'Amphibian', 'Fish', 'Crab/Lobster/Shrimp', 'Invertebrate') Order BY name")
        results_as_list = result.fetchall()

        scatter_animals_data = []
    for name, category, acres in results_as_list:
        p_dict = {}
        p_dict["Name"] = name
        p_dict["Category"] = category
        p_dict["Acres"] = acres
        scatter_animals_data.append(p_dict)

    return jsonify(scatter_animals_data)

# Scatter Plot #2 Park Acres x Total # Plants


@ app.route("/api/v1.0/scatter_plants")
def scatter_plants():
    with engine.connect() as connection:
        result = connection.execute(
            "SELECT name, category, acres  FROM merge WHERE category IN ('Vascular Plant', 'Nonvascular Plant') Order BY name")
        results_as_list = result.fetchall()

        scatter_plants_data = []
    for name, category, acres in results_as_list:
        p_dict = {}
        p_dict["Name"] = name
        p_dict["Category"] = category
        p_dict["Acres"] = acres
        scatter_plants_data.append(p_dict)

    return jsonify(scatter_plants_data)

# Scatter Plot #3 Park Acres x Total # Insects


@ app.route("/api/v1.0/scatter_insects")
def scatter_insects():
    with engine.connect() as connection:
        result = connection.execute(
            "SELECT name, category, acres  FROM merge WHERE category IN ('Spider/Scorpion', 'Insect', 'Slug/Snail') Order BY name")
        results_as_list = result.fetchall()

        scatter_insects_data = []
    for name, category, acres in results_as_list:
        p_dict = {}
        p_dict["Name"] = name
        p_dict["Category"] = category
        p_dict["Acres"] = acres
        scatter_insects_data.append(p_dict)

    return jsonify(scatter_insects_data)

# Scatter Plot #4 Park Acres x Total # Fungi


@ app.route("/api/v1.0/scatter_fungi")
def scatter_fungi():
    with engine.connect() as connection:
        result = connection.execute(
            "SELECT name, category,acres  FROM merge WHERE category IN ('Fungi', 'Algae') Order BY name")
        results_as_list = result.fetchall()

        scatter_fungi_data = []
    for name, category, acres in results_as_list:
        p_dict = {}
        p_dict["Name"] = name
        p_dict["Category"] = category
        p_dict["Acres"] = acres
        scatter_fungi_data.append(p_dict)

    return jsonify(scatter_fungi_data)

# LMS UPDATE TABLE


# @app.route("/api/v1.0/tabledata")
# def table():
#      with engine.connect() as connection:
#         result = connection.execute(
#             "SELECT name, category,acres  FROM merge WHERE category IN ('Fungi', 'Algae') Order BY name")
#         results_as_list = result.fetchall()

#         scatter_fungi_data = []
#     for name, category, acres in results_as_list:
#         p_dict = {}
#         p_dict["Name"] = name
#         p_dict["Category"] = category
#         p_dict["Acres"] = acres
#         scatter_fungi_data.append(p_dict)

#     return jsonify(scatter_fungi_data)

if __name__ == "__main__":
    app.run(debug=True)
