from flask import Flask, redirect, request, url_for

import requests

from flask import request
from flask import Flask, render_template

from jinja2 import Template
import secrets

import base64
import json
import os


from flask import session


app = Flask(__name__)

app.secret_key = secrets.token_hex() 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, ForeignKey, String

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    },
     'file.handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'ShawnsPC.log',
            'maxBytes': 10000000,
            'backupCount': 5,
            'level': 'DEBUG',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file.handler']
    }
})


# SQLite Database creation for the website
Base = declarative_base()
engine = create_engine("sqlite:///ShawnsPC.db", echo=True, future=True)
DBSession = sessionmaker(bind=engine)


#Creates the table for the session.
#holds the customers order.
@app.before_first_request
def create_tables():
    Base.metadata.create_all(engine)



# Logs a user into the site.
# Allows them to purchase item.
# users can have the same username but not the same password
# passwords must be hidden in the SQL
#FEATURES:
    # see order progress
    # cancel order before it is done.
def login():
    
    return

# Handles the user buying the computer.
# needs to update the log (dbsession)?.
# need to find long term storage...
def buy_computer():
    
    return

# Will allow admin to see orders.
# Will place it out on a list.
# FEATURES:
    # Allow admin to say a order is ready.
    # sees all order history
def admin():
    
    return

# will get all the orders that were made.
# will probably need to be split up between (completed, canceled, pending)
def get_orders():
    
    return

















if __name__ == "__main__":

    app.debug = False
    app.logger.info('Portal started...')
    app.run(host='0.0.0.0', port=5010) 
