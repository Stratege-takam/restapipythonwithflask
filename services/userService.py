from services.iuserService import *
from models.user import *
from services.authgradeService import AuthGradeService

class UserService(IUserService, AuthGradeService):

    def get_all_users(self):
        get_users = User.query.all()
        user_schema = UserSchema(many=True)
        users = user_schema.dump(get_users)
        return users

    def get_user_by_id(self,id):
        get_user = User.query.get(id)
        user_schema = UserSchema()
        user = user_schema.dump(get_user)
        return user

    def update_user_by_id(self, user):
        get_user = User.query.get(user.id)

        get_user.username = user.username
        get_user.fullname = user.fullname
        get_user.password = user.password
        get_user.token = user.token
        db.session.add(get_user)

        db.session.commit()
        user_schema = UserSchema(only=['id', 'username', 'fullname', 'password', 'token'])
        user = user_schema.dump(get_user)
        return user


    def delete_user_by_id(self,id):
        get_user = User.query.get(id)
        db.session.delete(get_user)
        db.session.commit()
        return True

    def create_user(self, user):
        user_schema = UserSchema()
        user = user_schema.load(user)
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return result
