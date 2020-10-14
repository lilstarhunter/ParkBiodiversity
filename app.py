import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlite3
import csv

from flask import Flask, jsonify, render_template, url_for
from flask_cors import CORS


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///new.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Coi_data = Base.classes.coi_data

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
#     con = sqlite3.connect("new.sqlite")  
#     con.row_factory = sqlite3.Row  
#     cur = con.cursor()  
#     cur.execute("select * from survive")  
#     rows = cur.fetchall()  
#     return render_template("index2.html",rows = rows)  
    return render_template('index.html')


# @app.route("/api/v1.0/names")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)


@app.route("/api/v1.0/survivors")
def survivors():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # data = engine.execute("SELECT * FROM survive")

    # """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    coi_data = session.query(Coi_data._id, Coi_data.geoid, Coi_data.year, Coi_data.in100, Coi_data.msaid15).all()
        #  Coi_data.msaname15, Coi_data.statefips, Coi_data.stateusps, Coi_data.pop, Coi_data.z_HE_nat,\
        #       Coi_data.z_COI_nat, Coi_data.c5_HE_nat, Coi_data.c5_COI_nat, Coi_data.c5_HE_stt, Coi_data.c5_COI_stt ).all()
    print(coi_data)
    session.close()  

    # Create a dictionary from the row data and append to a list of all_passengers
    all_coi_data = {}
    for _id, geoid, year, in100, msaid15 in coi_data:
        s_dict = {}
        s_dict["_id"] = _id
        s_dict["geoid"] = geoid
        s_dict["year"] = year
        s_dict["in100"] = in100
        s_dict["msaid15"] = msaid15
        all_coi_data.append(s_dict)

    # for a in all_coi_data:
    #     print(a)
    return jsonify(all_coi_data)


if __name__ == '__main__':
    app.run(debug=True)
