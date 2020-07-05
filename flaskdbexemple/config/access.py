#https://flask-jwt-extended.readthedocs.io/en/stable/changing_default_behavior/
#https://flask-jwt-extended.readthedocs.io/en/stable/custom_decorators/
#https://flask-jwt-extended.readthedocs.io/en/stable/optional_endpoints/
#https://flask-jwt-extended.readthedocs.io/en/stable/
#https://flask-jwt-extended.readthedocs.io/en/stable/tokens_from_complex_object/
#https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage/

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    verify_jwt_in_request,
    get_jwt_identity, get_jwt_claims
)
from config.settings import jsonify, init_app
from functools import wraps

import datetime

roles = ['accessLevel1','accessLevel2', 'accessLevel3', 'accessLevel4', 'accessLevel5']


# This is an example of a complex object that we could build
# a JWT from. In practice, this will likely be something
# like a SQLAlchemy instance.
class UserObject:
    def __init__(self, privateCode, roles, origin):
        self.privateCode = privateCode
        self.roles = roles
        self.origin = origin

# Create a function that will be called whenever create_access_token
# is used. It will take whatever object is passed into the
# create_access_token method, and lets us define what the identity
# of the access token should be.
@init_app.jwt.user_identity_loader
def user_identity_lookup(userObject):
    return {"username":userObject.privateCode, "origin": userObject.origin}


# Create a function that will be called whenever create_access_token
# is used. It will take whatever object is passed into the
# create_access_token method, and lets us define what custom claims
# should be added to the access token.
@init_app.jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'roles': user.roles}

# Here is a custom decorator that verifies the JWT is present in
# the request, as well as insuring that this user has a role of
# `accessLevel1` in the access token
def accessLevel1_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if roles[0] not in claims['roles']:
            return jsonify(msg='accessLevel1 only!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper

# Here is a custom decorator that verifies the JWT is present in
# the request, as well as insuring that this user has a role of
# `accessLevel2` in the access token
def accessLevel2_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if roles[1] not in claims['roles']:
            return jsonify(msg='accessLevel2 only!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper


# Here is a custom decorator that verifies the JWT is present in
# the request, as well as insuring that this user has a role of
# `accessLevel3` in the access token
def accessLevel3_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if roles[2] not in  claims['roles']:
            return jsonify(msg='accessLevel3 only!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper


# Here is a custom decorator that verifies the JWT is present in
# the request, as well as insuring that this user has a role of
# `accessLevel4` in the access token
def accessLevel4_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if roles[3] not in claims['roles']:
            return jsonify(msg='accessLevel4 only!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper

# Here is a custom decorator that verifies the JWT is present in
# the request, as well as insuring that this user has a role of
# `accessLevel5` in the access token
def accessLevel5_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if roles[4] not in claims['roles']:
            return jsonify(msg='accessLevel5 only!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper


def create_limit_token(authgradeService, authjwt):
    #time = 366 if authjwt.expiredTime <2 else 365*2+1 if int(round(authjwt.expiredTime)) < 3 else 365*3+1

    expires = datetime.timedelta(days= int(round(authjwt.expiredTime)) + 1, hours=0, seconds=0, minutes=0)
    #expires = datetime.time(30*24)
    userObject = UserObject(authgradeService.hash_password(authjwt.privateCode),
                            authjwt.policy.split(';'),
                            authgradeService.hash_password(authjwt.origin))

    token = create_access_token(identity= userObject, expires_delta=expires)
    return token

def create_api_token(authgradeService, authjwt):
    #username = get_jwt_identity()
    userObject = UserObject(authgradeService.hash_password(authjwt.privateCode),
                            authjwt.policy.split(';'),
                            authgradeService.hash_password(authjwt.origin))
    token = create_access_token(identity=userObject, expires_delta=False)
    return token


def user_connected():
     info = {
        'current_identity': get_jwt_identity(),  # test
        'current_roles': get_jwt_claims()['roles']  # ['foo', 'bar']
        }
     return info