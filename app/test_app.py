import unittest
from pathlib import Path


class TestApplication(unittest.TestCase):

    def test_app_exists(self):
        self.assertTrue(Path("app/app.py").is_file())

    def test_http_server_used(self):
        code = Path("app/app.py").read_text()
        self.assertIn("HTTPServer", code)

    def test_environment_variable_used(self):
        code = Path("app/app.py").read_text()
        self.assertIn("STUDENT_NAME", code)


if __name__ == "__main__":
    unittest.main()
