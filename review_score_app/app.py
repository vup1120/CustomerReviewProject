from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)

# enter path to the sqlite file here. 
flask_app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AmazonDB'


db = SQLAlchemy(flask_app)

# register models
from review_score_app import models
