#https://www.nintyzeros.com/2019/11/flask-mysql-crud-restful-api.html
#https://sourabhbajaj.com/mac-setup/Python/virtualenv.html
#https://blog.toast38coza.me/adding-a-database-to-a-flask-app/
#https://stackoverflow.com/questions/57984649/flask-marshmallow-sqlalchemy-marshmallow-object-has-no-attribute-modelschem
#https://flask-migrate.readthedocs.io/en/latest/
#https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/inheritance.html
#https://docs.sqlalchemy.org/en/13/orm/relationships.html
#https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#one-to-many
#https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-one
#https://docs.sqlalchemy.org/en/13/orm/inheritance.html
#https://flask-migrate.readthedocs.io/en/latest/
#https://geekflare.com/securing-flask-api-with-jwt/?fbclid=IwAR3rT5BerG7gw0AjIHyxDPSykQffQHXEHHZ271Y9yXDCXInQQx3LHppza3A



#testing
#https://pypi.org/project/unittest2/
#https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
#https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way
#https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/
#https://sqlitebrowser.org/
#https://sqlitebrowser.org/blog/macos-installer-rebuilt-for-3-11-1/
#https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/
#https://medium.com/free-code-camp/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563
#https://geekflare.com/securing-flask-api-with-jwt/
#https://realpython.com/token-based-authentication-with-flask/

from flask import Flask, request, jsonify, make_response, Blueprint
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from sqlalchemy.orm import relationship
from flask_migrate import Migrate, Manager, MigrateCommand
import jwt
from functools import wraps
#from flask_restful import Resource, Api
import json
from pathlib import Path

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@127.0.0.1:8889/flaskdb'
#app.config['SECRET_KEY']='apitest@stratege-takam'
#db = SQLAlchemy(app)
db = SQLAlchemy()



from flask_restplus import Api, Resource
from flask import Blueprint

envs = {'test':"testing",
        "dev":"development",
        "prod":"production"}


class  Init():

    def get_project_root(self) -> Path:
        """Returns project root folder."""
        return Path(__file__).parent.parent

    def __init__(self):
        self.path = f"{self.get_project_root()}/config/config.json"
        self.app = None
        self.jwt = None
        self.api = None

    def create_app(self):
        data = self.read_json_param()
        #print("{0}".format(data))
        conf_name = data["env"]
        self.app = Flask(__name__)
        self.jwt = JWTManager(self.app)
        self.app.config.from_object(app_config[conf_name])
        db.init_app(self.app)
        self.api = Api(app=self.app, version='0.1', title='Books Api', description='', validate=True)
        #return app,jwt

    def change_env(self, new_env):
        data = self.read_json_param()
        data["env"] = new_env
        self.write_json_param(data)
        self.create_app()


    def read_json_param(self):
        with open(self.path) as json_file:
            data = json.load(json_file)
            return data

    def write_json_param(self, data):
        with open(self.path, 'w') as outfile:
            json.dump(data, outfile)


init_app = Init()

app_param = init_app.read_json_param()


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = app_param["secret"]
    SQLALCHEMY_DATABASE_URI = app_param["production"]
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = app_param["development"]


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = app_param["testing"]
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}


init_app.create_app()





#api_bp = Blueprint("api", __name__, url_prefix="/api")
#api = Api(api_bp)



#def token_required(f):
#    @wraps(f)
#    def decorator(*args, **kwargs):

#        token = None

#        if 'Authorization' in request.headers:
#            token = request.headers['Authorization']

#        if not token:
#           return jsonify({'message': 'a valid token is missing'})

#        try:
#            data = jwt.decode(token, app.config['SECRET_KEY'])
#            current_user = User.query.filter_by(privateCode=data['privateCode']).first()
#        except:
#            return jsonify({'message': 'token is invalid'})

#        return f(current_user, *args, **kwargs)

#    return decorator




#db = SQLAlchemy(app)

#1. taper la commande suivante pour créer une référence de la migration
#flask db init

#2. Enregistrer les modifications avec la commande suivante
#flask db migrate -m "Initial migration."

#3. Migrer la bd
#flask db upgrade

#4. voir les commandes
#flask db --help


#$ python manage.py db init
#$ python manage.py db migrate -m "Initial migration."
#$ python manage.py db upgrade
#$ python manage.py db --help
#nose2 -v
#python manage.py run
#python manage.py test
#pip freeze > requirements.txt
#coverage run tests/test_basic.py
#coverage report -m */*.py
#coverage report -m project/users/*.py
#coverage html project/users/*.py