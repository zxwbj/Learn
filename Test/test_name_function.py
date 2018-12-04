import unittest
from name_function import get_formatted_name


class NamesTestCast(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('zxw', 'zxx')
        self.assertEqual(formatted_name, 'Zxw Zxx')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('zxw', 'zxx', 'test')
        self.assertEqual(formatted_name, 'Zxw Test Zxx')


if __name__ == '__main__':
    unittest.main()
