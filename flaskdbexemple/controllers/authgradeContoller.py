from config.access import  user_connected, jwt_required, create_limit_token, create_access_token
from config.settings import init_app, make_response, jsonify, request, Resource, envs, app_param

from services.authgradeService import AuthGradeService
from models.user import User
from services.userService import UserService
from models.authjwt import AuthJwt

class AuthGradeController(Resource):

    __authGradeService = AuthGradeService()

    # Protect a view with jwt_required, which requires a valid access token
    # in the request to access.
    @init_app.app.route('/applications/protected', methods=['GET'])
    @jwt_required
    def protected():
        ret = user_connected()
        return jsonify(ret), 200

    @init_app.app.route('/applications/register', methods = ['POST'])
    def auth_create_an_application():
        if (envs['test'] == app_param['env']):
            data = request.form.to_dict()
        else:
            data = request.get_json()
        #auth = request.authorization

        if not data or not data.get("policy") or not data.get("origin") \
                or not data.get("expiredTime") or not data.get("userId") :
            return make_response('could not verify', 401, {'Authentication': 'insufficient informations'})

        authjwt = AuthJwt(data["policy"], data["origin"], AuthGradeController.__authGradeService.unique_id(10),
                          data["userId"], data["expiredTime"])
        user =UserService().get_user_by_id(authjwt.userId)

        if user:
            #token = self.__authGradeService.generate_token(authjwt)
            token = create_limit_token(AuthGradeService(), authjwt)
            authjwt.token = token
            return jsonify({'token': token})
            authjwt.slug = AuthGradeController.__authGradeService.unique_id()
            #create application
            result = AuthGradeController.__authGradeService.create_an_application(authjwt)

            #return jsonify({'token': token.decode('UTF-8')})
            return  make_response(jsonify({"student": result}))
            #return jsonify({'token': token})

        return make_response('could not verify', 401, {'Authorization': 'Basic realm: "login required"'})



