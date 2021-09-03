from main import app
import unittest


class flaskTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='document')
        self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()
