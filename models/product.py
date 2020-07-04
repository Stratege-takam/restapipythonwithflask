from config.settings import db, fields, relationship, ModelSchema

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    productDescription = db.Column(db.String(100))
    productBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship("User")
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   # user = relationship("modelsTest.user.User", back_populates="products", lazy='dynamic')


   # def create(self):
   #   db.session.add(self)
   #   db.session.commit()
   #   return self

    def __init__(self,title,productDescription,productBrand,price, userId):
        self.title = title
        self.productDescription = productDescription
        self.productBrand = productBrand
        self.price = price
        self.userId = userId
        #self.id = 0
    def __repr__(self):
        return '' % self.id
#db.create_all()

class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Product
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    productDescription = fields.String(required=True)
    productBrand = fields.String(required=True)
    price = fields.Number(required=True)
    userId= fields.Number(required = True)