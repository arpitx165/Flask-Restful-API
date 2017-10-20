import unittest
import json
from app import mongo
from app import app as app_client
from unittest import mock

class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app_client.test_client()

    def test_home_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_technology_endpoint(self):
        expected_result = {
            'data': {
                'Count': [
                    73, 1, 41, 23, 24,
                    1, 5, 2, 7326, 37,
                    20, 1, 62, 5, 15,
                    8, 7, 4, 2, 18, 2,
                    2, 4, 3, 4, 1, 3,
                    1, 3, 2, 1, 1],
                'language_Name': 
                    [
                        'JavaScript', 'F#', 'Java',
                        'C++', 'PHP', 'Perl6', 'Go',
                        'D', None, 'Ruby', 'CSS', 'Haskell',
                        'Python', 'DM', 'Shell', 'Scala', 'Lua',
                        'Rust', 'TeX', 'C#', 'Julia', 'Puppet',
                        'Swift', 'Emacs Lisp', 'C', 'SQF',
                        'Objective-C', 'Scheme', 'CoffeeScript',
                        'FORTRAN', 'Perl', 'Clojure'
                    ]
            },
            'status': 'ok'
        }

        with mock.patch.object(self.app, 'get') as mock_app:
            data = mock.Mock(return_value=expected_result)
            mock_app.return_value.data = expected_result
            response = self.app.get('/technology')
            self.assertEqual(expected_result, response.data)

    def test_repository_endpoint(self):
        language = 'python'
        response = self.app.get('/repo/{}'.format(language))

        self.assertIsNotNone(response)

    def test_user_endpoint(self):
        user = 'arpit'
        response = self.app.get('/user/{}'.format(user))

        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
