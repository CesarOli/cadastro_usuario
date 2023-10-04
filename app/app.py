
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("chave_secreta")
DATABASE_URL = os.getenv("DATABASE_URL")
DEBUG = os.getenv("DEBUG")


app = Flask(__name__)

app.config.from_object('config.Config')

db = SQLAlchemy(app)
