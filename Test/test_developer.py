import unittest
from Makogon_7 import Developer


class TestDeveloper(unittest.TestCase):

    def setUp(self):
        self.developer_1 = Developer("Alice", 500, ["Python", "JavaScript"])
        self.developer_2 = Developer("Bob", 600, ["JavaScript", "Java"])

    def test_work(self):
        self.assertEqual(self.developer_1.work(), "I come to the office and start to hiring")

    def test_str(self):
        self.assertEqual(str(self.developer_1), "Position: Alice")
        self.assertEqual(str(self.developer_2), "Position: Bob")

    def test_add(self):
        combined_dev = self.developer_1 + self.developer_2
        self.assertEqual(combined_dev.name, "Alice Bob")
        expected_tech_stack = ["Python", "JavaScript", "Java"]
        self.assertCountEqual(combined_dev.tech_stack, expected_tech_stack)
        self.assertEqual(combined_dev.salary_one_working_day, 600)

    def test_lt_tech_stack_length(self):
        # Создание объектов Developer
        dev1 = Developer("Alice", 500, ["Python", "JavaScript"])
        dev2 = Developer("Bob", 600, ["JavaScript", "Java", "C++"])

        # Проверка, что dev1 < dev2 по длине техстека
        self.assertTrue(dev1 < dev2)

        # Проверка, что dev2 не < dev1 по длине техстека
        self.assertFalse(dev2 < dev1)

        # Создание объектов с одинаковой длиной техстека
        dev3 = Developer("Charlie", 700, ["Go", "Rust"])
        dev4 = Developer("Dave", 800, ["Ruby", "Perl"])

        # Проверка, что dev3 не < dev4 и dev4 не < dev3
        self.assertFalse(dev3 < dev4)
        self.assertFalse(dev4 < dev3)


if __name__ == '__main__':
    unittest.main()
