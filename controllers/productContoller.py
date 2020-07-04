from config.settings import init_app, make_response, jsonify, request, Resource, envs, app_param
from config.access import accessLevel5_required
from models.product import Product

from services.productService import ProductService


class ProductController():
    __productService = ProductService()

    @init_app.app.route('/products', methods = ['GET'])
    @init_app.api.doc('Get products')
    @accessLevel5_required
    def get_all_products():
        products = ProductController.__productService.get_all_products()
        return make_response(jsonify({"product": products}))

    @init_app.app.route('/products/<id>', methods = ['GET'])
    @init_app.api.doc('Find product by id')
    @accessLevel5_required
    def get_product_by_id(id):
        product = ProductController.__productService.get_product_by_id(id)
        return make_response(jsonify({"product": product}))

    @init_app.app.route('/products/<id>', methods = ['PUT'])
    @init_app.api.doc('Update product by id')
    @accessLevel5_required
    def update_product_by_id(self, id):
        if (envs['test'] == app_param['env']):
            data = request.form.to_dict()
        else:
            data = request.get_json()
        product = None
        if data.get('title') and  data.get('productDescription') and data.get('productBrand') \
                and data.get('price') and data.get('userId'):
            product = Product(data['title'], data['productDescription'], data['productBrand'], data['price'], data['userId'])
        else:
            return make_response('invalid input', 500, {'input': "invalid input"})
        if  product is not None:
            product = self.__productService.update_product_by_id(id,product)
        return make_response(jsonify({"product": product}))

    @init_app.app.route('/products/<id>', methods = ['DELETE'])
    @init_app.api.doc('Delete product by id')
    @accessLevel5_required
    def delete_product_by_id(id):
        response = ProductController.__productService.delete_product_by_id(id)
        return make_response({'result': response}, 204)

    @init_app.app.route('/products', methods = ['POST'])
    @init_app.api.doc('Create product by id')
    #@accessLevel5_required
    def create_product():
        if (envs['test'] == app_param['env']):
            data = request.form.to_dict()
        else:
            data = request.get_json()
        result = ProductController.__productService.create_product(data)
        return make_response(jsonify({"product": result}),200)



