import unittest

from country_codes import get_country_code


class TestCountryCodeCase(unittest.TestCase):
    def test_country_code(self):
        country_code = get_country_code('China')
        self.assertEqual('cn', country_code)


if '__main__' == __name__:
    unittest.main()
