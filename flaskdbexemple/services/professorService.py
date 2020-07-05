

from services.userService import *
from models.professor import *

class ProfessorService(UserService):

    def __init__(self):
        self.__authgradeService = AuthGradeService()

    def get_all_users(self):
        get_professors = Professor.query.all()
        professor_schema = ProfessorSchema(many=True)
        professors = professor_schema.dump(get_professors)
        return professors

    def get_user_by_id(self,id):
        get_professor = Professor.query.get(id)
        professor_schema = ProfessorSchema()
        professor = professor_schema.dump(get_professor)
        return professor

    def update_user_by_id(self,id, professor):
        get_professor = Professor.query.get(id)

        get_professor.username = professor.username
        get_professor.fullname = professor.fullname
        get_professor.password = professor.password
        get_professor.salary = professor.salary
        get_professor.hiredate = professor.hiredate
        db.session.add(get_professor)

        db.session.commit()
        professor_schema = ProfessorSchema()
       # professor_schema = ProfessorSchema(only=['id', 'username', 'fullname', 'password',
       #                                          "hiredate", "salary"
       #                                                      'slug'])
        professor = professor_schema.dump(get_professor)
        return professor


    def delete_user_by_id(self,id):
        get_professor = Professor.query.get(id)
        db.session.delete(get_professor)
        db.session.commit()
        return True

    def create_user(self, professor):
        professor["slug"] = self.__authgradeService.unique_id()
        professor["password"] = self.__authgradeService.hash_password(professor["password"])
        professor_schema = ProfessorSchema()
        professor = professor_schema.load(professor)
        db.session.add(professor)
        db.session.commit()
        result = professor_schema.dump(professor)
        return result
