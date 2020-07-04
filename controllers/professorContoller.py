from config.settings import init_app, make_response, jsonify, request, Resource, envs, app_param
from config.access import accessLevel1_required
from services.professorService import ProfessorService
from models.professor import Professor

class ProfessorController(Resource):
    __professorService = ProfessorService()

    @init_app.app.route('/professors', methods = ['GET'])
    @accessLevel1_required
    def get_all_professors():
        professors = ProfessorController.__professorService.get_all_users()
        return make_response(jsonify({"professor": professors}))

    @init_app.app.route('/professors/<id>', methods = ['GET'])
    @accessLevel1_required
    def get_professor_by_id(id):
        professor = ProfessorController.__professorService.get_user_by_id(id)
        return make_response(jsonify({"professor": professor}))

    @init_app.app.route('/professors/<id>', methods = ['PUT'])
    @accessLevel1_required
    def update_professor_by_id(id):
        if (envs['test'] == app_param['env']):
            data = request.form.to_dict()
        else:
            data = request.get_json()
        professor = None
        if data.get('username') and  data.get('password') and data.get('fullname') and data.get('hiredate') and data.get('salary'):
           # data["hiredate"] = parse(str(data["hiredate"])).date()
            professor = Professor(data['username'], data['password'], data['fullname'], data['salary'], data['hiredate'], None)
        else:
            return make_response('invalid input', 500, {'input': "invalid input"})
        if  professor is not None:
            professor = ProfessorController.__professorService.update_user_by_id(id,professor)
        return make_response(jsonify({"professor": professor}))

    @init_app.app.route('/professors/<id>', methods = ['DELETE'])
    @accessLevel1_required
    def delete_professor_by_id(id):
        response = ProfessorController.__professorService.delete_user_by_id(id)
        return make_response({'result': response}, 204)

    @init_app.app.route('/professors', methods = ['POST'])
    def create_professor():
        if (envs['test'] == app_param['env']):
            data = request.form.to_dict()
        else:
            data = request.get_json()
        #data["hiredate"] = parse(str(data["hiredate"])).date()
        #return data
        result = ProfessorController.__professorService.create_user(data)
        return make_response(jsonify({"professor": result}),200)



