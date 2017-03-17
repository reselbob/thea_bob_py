from unittest import TestCase
from employee import Employee


class TestEmployee(TestCase):
    def get_test_employee(self):
        fname = 'Luke'
        lname = 'Thedad'
        sal = 10000000
        employee = Employee(fname, lname, sal)
        return employee

    def test_create_employee(self):
        fname = 'Luke'
        lname = 'Thedad'
        sal = 10000000
        employee = Employee(fname, lname, sal)
        self.assertEqual(employee.first_name, fname)
        self.assertEqual(employee.last_name, lname)
        self.assertEqual(employee.salary, sal)

    def test_update_employee(self):
        employee = self.get_test_employee()
        new_sal = 20000000
        employee.salary = new_sal
        self.assertEqual(employee.salary, new_sal)

    def test_employee_talk(self):
        phrase = 'Python programming is cool'
        employee = self.get_test_employee()
        new_sal = 20000000
        result = employee.talk(phrase)
        self.assertEqual(result, 'OK')

    def test_employee_walk(self):
        phrase = 'Python programming is cool'
        employee = self.get_test_employee()
        new_sal = 20000000
        result = employee.walk()
        self.assertEqual(result, 'OK')