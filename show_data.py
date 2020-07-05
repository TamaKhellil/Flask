#!/usr/bin/env python
# coding: utf-8

# This script shows data from an SQL database in a web application 
# This script records  logging data in an SQL database  
# configuration is stored in the "config.yml" file

# import libs
from datetime import datetime
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import yaml
import traceback
from flask import Flask

# read configuration
try:
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.BaseLoader)

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception:
    print(traceback.print_exc())

# create engine
engine = create_engine(cfg["connect_string"])

# function records logging time in the SQL database
def record_log_time():
    try:
        log_entry = pd.DataFrame(columns=["log time"])
        log_entry = log_entry.append({"log time": datetime.now()}, ignore_index=True)
        log_entry.to_sql(cfg["log_data_table"], engine, index=False, if_exists="append")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except NameError as n_error:
        print(n_error)
    except Exception:
        print(traceback.print_exc())

# get data
try:
    df = pd.read_sql(cfg["table_name"], con=engine)

except NameError as n_error:
    print(n_error)
except Exception:
    print(traceback.print_exc())

# show data in the app
app = Flask(__name__)


@app.route("/")
def index():
    record_log_time()
    return df.to_html()

