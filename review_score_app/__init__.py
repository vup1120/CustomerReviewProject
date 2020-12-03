from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(module)s: :: %(levelname)s :: %(message)s')


app = Flask(__name__)

# enter path to the sqlite file here. 
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AmazonDB'
app.config['CORS_HEADERS'] = 'Content-Type'


db = SQLAlchemy(app)

# register models
from review_score_app import models
from review_score_app import views
