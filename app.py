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
Survive = Base.classes.survive

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
    return render_template('index2.html')


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
    survives = session.query(Survive.survival, Survive.organ).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_survivors = []
    for survival, organ in survives:
        s_dict = {}
        s_dict["survival"] = survival
        s_dict["organ"] = organ
        all_survivors.append(s_dict)

    # for record in data:
    #     print(record)
    return jsonify(all_survivors)


if __name__ == '__main__':
    app.run(debug=True)
