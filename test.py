from flask_testing import TestCase
from app import app
import unittest


class FlaskTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def test_index_loads(self):
        """Ensure index page loads correctly."""
        response = self.client.get('/', follow_redirects=True)
        self.assert200(response)
        self.assertTemplateUsed('index.html')
        self.assertIn(b"Past week's forecast in...", response.data)
        self.assertEqual(self.get_context_variable('session')['city'], 'Los Angeles')

    def test_change_city(self):
        """Ensure change city route works correctly."""
        response = self.client.post(
            '/change_city',
            data=dict(city='New York City'),
            follow_redirects=True
        )
        self.assert200(response)
        self.assertTemplateUsed('index.html')
        self.assertMessageFlashed('City successfully updated to <b>New York City</b>!', 'success')
        self.assertEqual(self.get_context_variable('session')['city'], 'New York City')

    def test_add_city(self):
        """Ensure add city route works correctly."""
        resp = self.client.get('/', follow_redirects=True)
        self.assert200(resp)
        response = self.client.post(
            '/add_city',
            data=dict(city='Cleveland', latitude='41.499', longitude='81.694', tz='America/New_York'),
            follow_redirects=True
        )
        self.assert200(response)
        self.assertTemplateUsed('add_city.html')
        self.assertMessageFlashed('City <b>Cleveland</b> successfully added!', 'success')
        self.assertEqual(self.get_context_variable('session')['city'], 'Los Angeles')


if __name__ == '__main__':
    unittest.main()
