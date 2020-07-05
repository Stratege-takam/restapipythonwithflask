import unittest

from config.settings import  db, init_app

init_app.change_env("testing")
init_app.app.app_context().push()

#print(f"{envs['test']} {app_param['env']}")

from models.models import *

from controllers import homeController , studentContoller, professorContoller, productContoller, authgradeContoller


class BaseModel(unittest.TestCase):

    def setUp(self):
        self.auth = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTM5NTkyMjksIm5iZiI6MTU5Mzk1OTIyOSwianRpIjoiNGNmYTg1ZTYtZmI3Ni00YmUyLWJmZTYtM2JkNzEzZDA4ZmVmIiwiZXhwIjoxNjI1NTgxNjI5LCJpZGVudGl0eSI6eyJ1c2VybmFtZSI6InNoYTI1NiRmOTljVzRMdSQ1NmJmYmYxZWU4YjM4ZjRjNmNkNDExNzlkMTRlODZmOTZiOWZkZTZiN2RiMWFlOTQ5NGNhZGUyN2Y0MDgzMjE3Iiwib3JpZ2luIjoic2hhMjU2JE45OUZ6anB1JGJjOTVkMmE2OTYwNWFjNDI1MDhjMmVkODA1N2JmYzE5OTk1ZTBjN2RmMTdhNmM0ZDdhNmQyZDE0OWFiMTljMjcifSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIiwidXNlcl9jbGFpbXMiOnsicm9sZXMiOlsiYWNjZXNzTGV2ZWwxIiwiYWNjZXNzTGV2ZWwyIiwiYWNjZXNzTGV2ZWwzIiwiYWNjZXNzTGV2ZWw0IiwiYWNjZXNzTGV2ZWw1Il19fQ.Wdd5vg-_zYrl8ONu24yzpIqD4bWvXM5XwzTNGVn9ePk"
        #self.flaskdbexemple = init_app.flaskdbexemple
        #self.client = init_app.test_client()
        #self.db = db
        #print("---------------run main ------------------")

        # binds the flaskdbexemple to the current context
        with init_app.app.app_context():
            # create all tables
            db.create_all()
            #print("---------------create database ------------------")



    #end test
    def tearDown(self):
        """teardown all initialized variables."""
        with init_app.app.app_context():
            #drop all tables
            db.session.remove()
            db.drop_all()
        #print("---------------end main ------------------")
        #init_app.change_env("development")