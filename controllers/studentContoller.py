from config.settings import init_app, make_response, jsonify, request, Resource, envs, app_param
from config.access import accessLevel3_required
from services.studentService import StudentService
from models.student import Student


class StudentController(Resource):
    __studentService = StudentService()

    @init_app.app.route('/students', methods = ['GET'])
    #@accessLevel3_required
    def get_all_students():
        students = StudentController.__studentService.get_all_users()
        return make_response(jsonify(students))

    @init_app.app.route('/students/<id>', methods = ['GET'])
    @accessLevel3_required
    def get_student_by_id( id):
        student = StudentController.__studentService.get_user_by_id(id)
        return make_response(jsonify(student))

    @init_app.app.route('/students/<id>', methods = ['PUT'])
    @accessLevel3_required
    def update_student_by_id(id):
        if (envs['test'] == app_param['env']):
            data = request.form.to_dict()
        else:
            data = request.get_json()
        student = None
        if data.get('username') and  data.get('password') and data.get('fullname') and data.get('register'):
            student = Student(data['username'], data['password'], data['fullname'], data['register'], None)
            #student.id = id
            #return make_response(jsonify({"student": student.username}))
        else:
            return make_response('invalid input', 500, {'input': "invalid input"})
        if  student is not None:
            student = StudentController.__studentService.update_user_by_id(id,student)
        return make_response(jsonify(student))

    @init_app.app.route('/students/<id>', methods = ['DELETE'])
    @accessLevel3_required
    def delete_student_by_id(id):
        response = StudentController.__studentService.delete_user_by_id(id)
        return make_response({'result': response}, 204)

    @init_app.app.route('/students', methods = ['POST'])
    def create_student():

        if(envs['test'] == app_param['env']):
            data = request.form.to_dict()
            #print("result = {0}".format(data))
            #print(f"{envs['test']} {app_param['env']}")
        else :
            data = request.get_json()

        data["slug"] = None


        result = StudentController.__studentService.create_user(data)
        return make_response(jsonify(result),200)



