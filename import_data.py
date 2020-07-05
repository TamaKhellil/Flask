#!/usr/bin/env python
# coding: utf-8




# This script transfers a csv data file to an SQL database 
# configuration is stored in the "config.yml" file





# import libs
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import yaml
import traceback





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





# transfer data to an SQL database
try:
    df = pd.read_csv(cfg["file_name"])
    df.to_sql(cfg["table_name"], engine, index=False, if_exists="replace")

except FileNotFoundError as fnf_error:
    print(fnf_error)
except NameError as n_error:
    print(n_error)
except Exception:
    print(traceback.print_exc())

