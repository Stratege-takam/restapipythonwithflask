from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime
import string
import random
from config.settings import request, jsonify, jwt
from werkzeug.security import generate_password_hash, check_password_hash
from models.authjwt import *


#import hashlib
#print(hashlib.md5("whatever your string is".encode('utf-8')).hexdigest())

class AuthGradeService():

    def __id_generator(self, length, chars):
        return ''.join(random.choice(chars) for _ in range(length))

    def unique_id(self, length = 12, isNumeric = False):
        st = str(uuid.uuid4()).replace("-", "").upper()
        return self.__id_generator(length, st)

    def hash_password(self, password):
        return generate_password_hash(password, method='sha256')

    def check_password(self, password, compare_password):
        return check_password_hash(password, compare_password)

    def generate_token(self,  authjwt):
        token = jwt.encode(
            {'privateCode': self.hash_password(authjwt.privateCode),
             'origin': self.hash_password(authjwt.origin),
             'policy': authjwt.policy,
             'exp': datetime.datetime.utcnow() + datetime.timedelta(days=authjwt.expiredTime)},
            app.config['SECRET_KEY'])
        return token

    def create_an_application(self, authjwt):
        authjwt_schema = AuthJwtSchema()
        authjwt = authjwt_schema.load(authjwt)
        #return authjwt_schema.dump(authjwt)
        db.session.add(authjwt)
        db.session.commit()
        result = authjwt_schema.dump(authjwt)
        return result
