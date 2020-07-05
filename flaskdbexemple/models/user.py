from config.settings import db, fields, relationship, ModelSchema

class User(db.Model):
    #__abstract__ = True
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    discriminator = db.Column('discriminator', db.String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}
    username = db.Column(db.String(20))
    password = db.Column(db.String(100))
    fullname = db.Column(db.String(20))
    slug = db.Column(db.String(15))
    isconnected = db.Column(db.Boolean, default=False)
    lastconnecteAt = db.Column(db.DateTime, nullable=True)
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


    # products = db.relationship('modelsTest.product.Product', backref='users')
    #products = relationship("modelsTest.product.Product", back_populates="users", lazy='dynamic')


    def __init__(self,username,password,fullname, slug = None):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.slug = slug
       # self.id = 0
    def __repr__(self):
        return self.username

class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    fullname = fields.String(required=True)
    slug = fields.String(required=True)
    #discriminator = fields.String(resquired=True)