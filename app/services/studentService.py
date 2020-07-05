from app.services.userService import *
from app.models.student import *

class StudentService(UserService):

    def __init__(self):
        self.__authgradeService =  AuthGradeService()

    def get_all_users(self):
        get_students = Student.query.all()
        student_schema = StudentSchema(many=True)
        students = student_schema.dump(get_students)
        return students


    def get_user_by_id(self,id):
        get_student = Student.query.get(id)
        student_schema = StudentSchema()
        student = student_schema.dump(get_student)
        return student

    def update_user_by_id(self,id, student):
        get_student = Student.query.get(id)
        get_student.username = student.username
        get_student.fullname = student.fullname
        get_student.password = student.password
        get_student.register = student.register
        db.session.add(get_student)

        db.session.commit()
        student_schema = StudentSchema()
        #student_schema = StudentSchema(only=['id', 'username', 'fullname', 'password', "register", 'slug'])
        student = student_schema.dump(get_student)
        return student


    def delete_user_by_id(self,id):
        get_student = Student.query.get(id)
        db.session.delete(get_student)
        db.session.commit()
        return True

    def create_user(self, student):
        #student =
        student["slug"] = self.__authgradeService.unique_id()
        student["password"] = self.__authgradeService.hash_password(student["password"])
        student_schema = StudentSchema()
        student = student_schema.load(student)
        db.session.add(student)
        db.session.commit()
        result = student_schema.dump(student)
        return result