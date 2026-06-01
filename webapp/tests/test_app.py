import unittest

from app import app


class FlaskExerciseTest(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_home_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Flask Course Project", response.data)

    def test_url_variable_route(self):
        response = self.client.get("/user/John")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"John", response.data)

    def test_object_variables_render(self):
        response = self.client.get("/variables")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"New York", response.data)

    def test_double_form(self):
        response = self.client.post("/predict", data={"x": "8"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"16", response.data)


if __name__ == "__main__":
    unittest.main()
