import unittest

from app.services.studentService import StudentService
from tests.base_model import BaseModel
from app.models.student import Student, StudentSchema


class TestStudent(BaseModel):
    """This class represents the student test case"""
    def setUp(self):
        super().setUp()
        self.student = {"username":"stratege","password":"azerty","fullname":"Danick TAKAM", "register":"213346","slug": "123"}


    def test_student_valid_model(self):
        """Test API can create a student (POST request)"""
        student_schema = StudentSchema()
        error = student_schema.validate(self.student)
        #print("students : {0}".format(error))
        self.assertEqual(error, {})
       # self.assertGreater(res['id'], 0)

    def test_student_invalid_model(self):
        student_schema = StudentSchema()
        error = student_schema.validate({})
        # print("students : {0}".format(error))
        self.assertNotEqual(error, {})
        """Test API can get a student (GET request)."""




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()