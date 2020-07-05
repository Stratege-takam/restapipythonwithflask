from app.models.user import *

class Professor(User):
    __tablename__ = "professors"
    __mapper_args__ = {'polymorphic_identity': 'professors'}
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    hiredate = db.Column(db.String(255))
    salary = db.Column(db.Float)


    def __init__(self,username,password,fullname, salary, hiredate,slug= None):
        super().__init__(username, password, fullname,slug)
        self.salary = salary
        self.hiredate = hiredate


class ProfessorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Professor
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    username = fields.String(required=True)
    slug = fields.String(required=True)
    password = fields.String(required=True)
    fullname = fields.String(required=True)
    hiredate = fields.String(required=True)
    salary = fields.Float(required=True)