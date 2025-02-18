import logging
import os
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config['ENV'] = os.getenv('FLASK_ENV')
app.config['DEBUG'] = app.config['ENV'] == "development"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['LOG_FILE'] = os.getenv('LOG_FILE')

mongo = PyMongo(app)
bcrypt = Bcrypt(app)


def serializer(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }


def setup_logging():
    os.makedirs("logs", exist_ok=True)

    with open(app.config['LOG_FILE'], "w"):
        pass

    file_handler = RotatingFileHandler(app.config['LOG_FILE'], maxBytes=10000, backupCount=3)
    file_handler.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)

    logging.basicConfig(level=logging.INFO, handlers=[file_handler, stream_handler])


setup_logging()

logging.info("Application started successfully.")

from app.routes import user_routes

app.register_blueprint(user_routes)
