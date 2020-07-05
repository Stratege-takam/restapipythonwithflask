from flask_jwt_extended import jwt_optional

from config.settings import  init_app, Resource
from services.maillingService import MaillingService


class HomeController(Resource):

    @init_app.app.route('/home', methods=['GET'])
    @init_app.api.doc('Home page')
    def main_page():
        maillingService = MaillingService("test python", ["sdanicktakam@yahoo.fr"], "I am a simple python test")
        result = maillingService.send()
        print(f"mail result : {result}")
        return f"<h1> Welcome to rest api {result} </h1>"

    @init_app.app.route('/<name>', methods=['GET'])
    @init_app.api.doc('Hello page')
    @jwt_optional
    def hello_name(name):
        return f"<h1> Hello {name} </h1>"