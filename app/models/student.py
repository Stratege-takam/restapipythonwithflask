from app.models.user import *

class Student(User):
    __tablename__ = "students"
    __mapper_args__ = {'polymorphic_identity': 'students'}
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    register = db.Column(db.String(20))


    def __init__(self,username,password,fullname, register,slug= None):
        super().__init__(username, password, fullname,slug)
        self.register = register


class StudentSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Student
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    username = fields.String(required=True)
    slug = fields.String(required=True)
    password = fields.String(required=True)
    fullname = fields.String(required=True)
    register = fields.String(required=True)