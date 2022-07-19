from flask import Flask
from config import Config
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

CORS(app, supports_credentials=True, origins="http://127.0.0.1:3000")

jwt = JWTManager(app)

from app import routes