import unittest

from app.config.settings import  db, init_app

init_app.change_env("testing")
init_app.app.app_context().push()

#print(f"{envs['test']} {app_param['env']}")

from app.models.models import *

from app.controllers import homeController , studentContoller, professorContoller, productContoller, authgradeContoller


class BaseModel(unittest.TestCase):

    def setUp(self):
        self.auth = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTM3NjUyMDIsIm5iZiI6MTU5Mzc2NTIwMiwianRpIjoiYThjZTBjNzAtY2RmZS00NzU4LTkxZTYtZjlhOTVlMTlkODhkIiwiZXhwIjoxNjI1Mzg3NjAyLCJpZGVudGl0eSI6eyJ1c2VybmFtZSI6InNoYTI1NiR4ZWpBZUVxcyQwOWVjOTQxNjdjOTgzOTY3YWI4M2FhMmRkODRkM2U1M2FhY2Q4ODVlNzIxNTU1ZTk4NGZiY2MwYWNmY2VhYzU0Iiwib3JpZ2luIjoic2hhMjU2JDBHbkNtSmhsJDg4MDcyYjYxY2NkZjQ2ODFkODhhMjA2MmY1YWI2MjcxNDZkMjcxZjIyODNhMTgyMmZmZmQ5YjNhMjFhZTNiODMifSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIiwidXNlcl9jbGFpbXMiOnsicm9sZXMiOlsiYWNjZXNzTGV2ZWwxIiwiYWNjZXNzTGV2ZWwyIiwiYWNjZXNzTGV2ZWwzIiwiYWNjZXNzTGV2ZWw0IiwiYWNjZXNzTGV2ZWw1Il19fQ.YYddKp3QSBYQVkhE5dt8F7Sc11siSzm7XBoI4PrS90Q"
        #self.app = init_app.app
        #self.client = init_app.app.test_client()
        #self.db = db
        #print("---------------run main ------------------")

        # binds the app to the current context
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
        init_app.change_env("development")