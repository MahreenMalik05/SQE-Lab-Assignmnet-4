import unittest


class TestStudentSystem(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(5 + 5, 10)

    def test_uppercase(self):
        self.assertEqual("ali".upper(), "ALI")

    def test_marks(self):
        marks = 90
        self.assertTrue(marks > 50)

    def test_roll(self):
        roll = "101"
        self.assertEqual(roll, "101")


if __name__ == '__main__':
    unittest.main()