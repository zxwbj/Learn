import unittest
from employee import Employee


class TestEmployeeCase(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('test', 20000)

    def test_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(25000, self.employee.salary)

    def test_custom_raise(self):
        self.employee.give_raise(6000)
        self.assertEqual(26000, self.employee.salary)


if '__main__' == __name__:
    unittest.main()
