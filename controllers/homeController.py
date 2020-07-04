from flask_jwt_extended import jwt_optional

from config.settings import  init_app, Resource


class HomeController(Resource):

    @init_app.app.route('/home', methods=['GET'])
    @init_app.api.doc('Home page')
    def main_page():
        return "<h1> Welcome to rest api </h1>"

    @init_app.app.route('/<name>', methods=['GET'])
    @init_app.api.doc('Hello page')
    @jwt_optional
    def hello_name(name):
        return f"<h1> Welcome to rest api {name} </h1>"