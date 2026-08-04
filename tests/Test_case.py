import time
from unittest import TestCase
from models import Student



class StudentTestCase(TestCase):
    #Создадим метод SetUp - который будет создавать экземлпяр класса
    # def test_default_name_is_none(self):
    #     student = Student()
    #     self.assertIsNone(student.name)

    def setUp(self):
        self.student = Student()

    def test_default_name_is_none(self):
        self.assertIsNone(self.student.name)

    def test_set_invalid_age(self):
        with self.assertRaises(ValueError): #Ожидание того что будет вызвано исключение
            self.student.set_age(18)


    # def test_default_name_is_none(self):
    #     self.asserIsNone(self.student.name)#Проверка, что значение переменной равно None
    #
    # def test_set_invalid_age(self):
    #     with self.assertRaises(ValueError):#Проверка того, что исключение было вызвано в процессе создания программы
    #         self.student.set_age(-100)

"""Методы SetUpclass - позволяет задать общие настройки и открыть ресурсы, которые будут использованы всеми тестами."""

class TestHelloWorldWithDayApp(TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.base_url: str = '/hello-world/'
    def test_can_get_correct_username_with_weekdate(self):
        username: str = 'username'
        response = self.app.get(self.base_url + username)
        response_text: str = response.data.decode()
        self.assertIn(username, response_text)
