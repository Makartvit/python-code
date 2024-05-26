import unittest
import datetime
import calendar
from Makogon_7 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee_1 = Employee("Alice", 100)
        self.employee_2 = Employee("Bob", 200)

    def test_work(self):
        self.assertEqual(self.employee_1.work(), "I come to the office")

    def test_str(self):
        self.assertEqual(str(self.employee_1), "Position: Alice")
        self.assertEqual(str(self.employee_2), "Position: Bob")

    def test_lt(self):
        self.assertTrue(self.employee_1 < self.employee_2)

    def test_le(self):
        self.assertTrue(self.employee_1 <= self.employee_2)
        self.assertTrue(self.employee_1 <= self.employee_1)  # Testing for self comparison

    def test_eq(self):
        self.assertFalse(self.employee_1 == self.employee_2)
        self.assertTrue(self.employee_1 == self.employee_1)  # Testing for self comparison

    def test_gt(self):
        self.assertTrue(self.employee_2 > self.employee_1)

    def test_ge(self):
        self.assertTrue(self.employee_2 >= self.employee_1)
        self.assertTrue(self.employee_2 >= self.employee_2)  # Testing for self comparison

    def test_check_salary(self):
        # Предполагаем, что месяц май (5) имеет 22 рабочих дня
        self.assertEqual(self.employee_1.check_salary(15, 5), 100 * 22)
        self.assertEqual(self.employee_2.check_salary(20, 5), 200 * 22)

        # Предполагаем, что месяц июль (7) имеет 21 рабочий день
        self.assertEqual(self.employee_1.check_salary(15, 7), 100 * 21)
        self.assertEqual(self.employee_2.check_salary(20, 7), 200 * 21)

        # Предполагаем, что месяц февраль (2) имеет 19 рабочих дней
        self.assertEqual(self.employee_1.check_salary(15, 2), 100 * 19)
        self.assertEqual(self.employee_2.check_salary(20, 2), 200 * 19)


if __name__ == '__main__':
    unittest.main()