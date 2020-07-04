from config.settings import db, fields, relationship, ModelSchema

class AuthJwt(db.Model):
    __tablename__ = 'authjwts'
    id = db.Column(db.Integer, primary_key=True)
    policy = db.Column(db.String(100))
    origin = db.Column(db.String(100))
    privateCode = db.Column(db.String(20))
    slug = db.Column(db.String(20))
    token = db.Column(db.Text())
    expiredTime = db.Column(db.Numeric)
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship("User")


    # products = db.relationship('modelsTest.product.Product', backref='users')
    #products = relationship("modelsTest.product.Product", back_populates="users", lazy='dynamic')


    def __init__(self,policy,origin,privateCode, userId,expiredTime, token= None):
        self.policy = policy
        self.origin = origin
        self.privateCode = privateCode
        self.token = token
        self.userId = userId
        self.expiredTime = expiredTime

    def __repr__(self):
        return '' % self.origin

class AuthJwtSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = AuthJwt
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    expiredTime = fields.Number(required=False)
    policy = fields.String(required=True)
    origin = fields.String(required=True)
    token = fields.String(required=False)
    privateCode = fields.String(required=True)
    slug = fields.String(required=True)
    user_id= fields.Number(required = True)