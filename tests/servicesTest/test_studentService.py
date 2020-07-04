import unittest

from services.studentService import StudentService
from tests.base_model import BaseModel
from models.student import Student


class TestStudentController(BaseModel):
    """This class represents the student test case"""
    def setUp(self):
        super().setUp()
        self.student = {"username":"stratege","password":"azerty","fullname":"Danick TAKAM", "register":"213346","slug": 123}
        self.studentService = StudentService()
        #print("---------------hello world ------------------")

    def test_student_creation(self):
        """Test API can create a student (POST request)"""
        #print("---------------start transaction main ------------------")
        res = self.studentService.create_user(self.student)
        self.assertEqual('stratege', res['username'])
        self.assertGreater(res['id'], 0)

    def test_api_can_get_all_students(self):
        """Test API can get a student (GET request)."""
        res = self.studentService.create_user(self.student)
        self.assertEqual('stratege', res['username'])
        res = self.studentService.get_all_users()
        self.assertGreater(len(res),0)

    def test_api_can_get_student_by_id(self):
        """Test API can get a single student by using it's id."""
        res = self.studentService.create_user(self.student)
        self.assertEqual('stratege', res['username'])
        result = self.studentService.get_user_by_id(res['id'])
        self.assertEqual('stratege', res['username'])

    def test_student_can_be_edited(self):
        """Test API can edit an existing student. (PUT request)"""
        res = self.studentService.create_user(self.student)
        self.assertEqual('stratege', res['username'])
        student = Student(self.student['username'], self.student['password'], self.student['fullname'], self.student['register'])
        student.username = "otis"
        rv = self.studentService.update_user_by_id(res['id'],student)
        self.assertIn('otis', rv['username'])

    def test_student_deletion(self):
        """Test API can delete an existing student. (DELETE request)."""
        student = self.studentService.create_user(self.student)
        self.assertEqual('stratege', student['username'])
        res = self.studentService.delete_user_by_id(student['id'])
        self.assertTrue(res)
        # Test to see if it exists, should return a 404
        result = self.studentService.get_user_by_id(student['id'])
        self.assertEqual(result, {})


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()