import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlite3
import csv
from collections import defaultdict
import json

from flask import Flask, jsonify, render_template, url_for
from flask_cors import CORS

#connect to the database
engine = create_engine("sqlite:///new.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
#reference db table
Parks = Base.classes.parks
Species = Base.classes.species

#open DB connection for query
session = Session(engine)
parks_data = session.query(Parks.ParkCode, Parks.ParkName, \
    Parks.State, Parks.Acres, Parks.Latitude, Parks.Longitude).all()
species_data = session.query(Species.SpeciesID, Species.ParkName, \
    Species.Category, Species.Order, Species.Family, Species.ScientificName)
session.close()
# Dump Parks data to json files
all_parks_data = []
for ParkCode, ParkName, State, Acres, Latitude, Longitude in parks_data:
    s_dict = {}
    s_dict["ParkCode"] = ParkCode
    s_dict["ParkName"] = ParkName
    s_dict["State"] = State
    s_dict["Acres"] = Acres
    s_dict["Latitude"] = Latitude
    s_dict["Longitude"] = Longitude
    all_parks_data.append(s_dict)

mydict_ = defaultdict(list)

for x in all_parks_data:
    for k, v in x.items():
        mydict_[k].append(v)
mydict = dict(mydict_)


jsonfile = r'data/parks.json'
with open(jsonfile, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(mydict, indent=4))

#Dump species data to json file
# Dump Parks data to json files
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

mydict_ = defaultdict(list)

for x in all_species_data:
    for k, v in x.items():
        mydict_[k].append(v)
mydict = dict(mydict_)


jsonfile = r'data/species.json'
with open(jsonfile, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(mydict, indent=4))


#set up flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index2.html')
@app.route("/api/v1.0/parks")
def parks():
    return jsonify(parks_data)
# @app.route("/api/v1.0/species")
# def species():

#     all_species_data = []
# for SpeciesID, ParkName, Category, Order, Family, ScientificName in species_data:
#     s_dict = {}
#     s_dict["SpeciesID"] = SpeciesID
#     s_dict["ParkName"] = ParkName
#     s_dict["Category"] = Category
#     s_dict["Order"] = Order
#     s_dict["Family"] = Family
#     s_dict["ScientificName"] = ScientificName
#     all_species_data.append(s_dict)

#  mydict_ = defaultdict(list)

# for x in all_species_data:
#     for k, v in x.items():
#         mydict_[k].append(v)
#     mydict = dict(mydict_)
# return jsonify(mydict)

if __name__ == "__main__":
    app.run(debug=True)