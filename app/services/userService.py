from app.services.iuserService import *
from app.models.user import *
from app.services.authgradeService import AuthGradeService

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
       raise NotImplementedError


    def delete_user_by_id(self,id):
        get_user = User.query.get(id)
        db.session.delete(get_user)
        db.session.commit()
        return True

    def create_user(self, user):
        raise NotImplementedError
