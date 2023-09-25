from flask import Flask
from dotenv import load_dotenv, os

load_dotenv()

SECRET_KEY = os.getenv("chave_secreta")
DATABASE_URL = os.getenv("postgresql://cesar:123456@localhost/cadastro_de_usuario")
DEBUG = os.getenv("DEBUG")