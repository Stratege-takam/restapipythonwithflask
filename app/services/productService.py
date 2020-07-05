from app.services.iproductService import *
from app.models.product import *

class ProductService(IProductService):

    def get_all_products(self):
        get_products = Product.query.all()
        product_schema = ProductSchema(many=True)
        products = product_schema.dump(get_products)
        return products

    def get_product_by_id(self,id):
        get_product = Product.query.get(id)
        product_schema = ProductSchema()
        product = product_schema.dump(get_product)
        return product

    def update_product_by_id(self,id, product):
        get_product = Product.query.get(id)

        get_product.title = product.title
        get_product.productBrand = product.productBrand
        get_product.productDescription = product.productDescription
        get_product.price = product.price
        db.session.add(get_product)

        db.session.commit()
        product_schema = ProductSchema(only=['id', 'title', 'productDescription', 'productBrand', 'price'])
        product = product_schema.dump(get_product)
        return product


    def delete_product_by_id(self,id):
        get_product = Product.query.get(id)
        db.session.delete(get_product)
        db.session.commit()
        return True


    def create_product(self, product):
        product_schema = ProductSchema()
        product = product_schema.load(product)
        db.session.add(product)
        db.session.commit()
        result = product_schema.dump(product)
        return result
