import unittest

from tests.base_model import *
from config.settings import  json


class TestStudentController(BaseModel):
    """This class represents the student test case"""
    def setUp(self):
        super().setUp()

        self.student = {"username":"stratege",
                        "password":"azerty",
                        "fullname":"Danick TAKAM",
                        "slug": "123",
                        "register":"213346"}
        self.header = {"Authorization": f"Bearer {self.auth}"}

    def test_student_creation(self):
        """Test API can create a student (POST request)"""
        res = init_app.app.test_client().post('/students', data=self.student, headers= self.header)
        self.assertEqual(res.status_code, 200)
        #print(res.data)
        result_in_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        self.assertEqual('stratege', result_in_json['username'])

    def test_api_can_get_all_students(self):
        """Test API can get a student (GET request)."""
        res = init_app.app.test_client().post('/students', data=self.student, headers= self.header)
        self.assertEqual(res.status_code, 200)
        res = init_app.app.test_client().get('/students', headers= self.header)
        self.assertEqual(res.status_code, 200)
        self.assertIn('Danick', str(res.data))
        result_in_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        #print(result_in_json)
        self.assertEqual(1, len(result_in_json))

    def test_api_can_get_student_by_id(self):
        """Test API can get a single student by using it's id."""
        rv = init_app.app.test_client().post('/students', data=self.student, headers= self.header)
        self.assertEqual(rv.status_code, 200)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        print(result_in_json)
        result = init_app.app.test_client().get(
            '/students/{}'.format(result_in_json['id']), headers= self.header)
        self.assertEqual(result.status_code, 200)
        self.assertIn('Danick', str(result.data))

    def test_student_can_be_edited(self):
        """Test API can edit an existing student. (PUT request)"""
        rv = init_app.app.test_client().post(
            '/students',
            data=self.student)
        self.assertEqual(rv.status_code, 200)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        self.student['fullname'] = "Otis Takam"
        self.student['register'] = 123
        rv = init_app.app.test_client().put(
            f'/students/{result_in_json["id"]}',
            data=self.student, headers= self.header)
        self.assertEqual(rv.status_code, 200)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
       # print(result_in_json)
        self.assertEqual('Otis Takam', result_in_json['fullname'])
        self.assertEqual("123", result_in_json['register'])

    def test_student_deletion(self):
        """Test API can delete an existing student. (DELETE request)."""
        rv = init_app.app.test_client().post(
            '/students',
            data=self.student, headers= self.header)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))

        self.assertEqual(rv.status_code, 200)
        res = init_app.app.test_client().delete(f'/students/{result_in_json["id"]}', headers=self.header)
        self.assertEqual(res.status_code, 204)
        # Test to see if it exists, should return a 404
        result = init_app.app.test_client().get(f'/students/{result_in_json["id"]}', headers=self.header)
        result_in_json = json.loads(result.data.decode('utf-8').replace("'", "\""))
        self.assertEqual({}, result_in_json)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()