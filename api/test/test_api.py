import unittest
import json
from unittest.mock import patch, mock_open
import sys
import os

# Add the parent directory to the sys.path to allow importing app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, DATA_FILE

# Mock data for testing
MOCK_CURSOS_DATA = [
    {
        "id": 1,
        "title": "Curso A",
        "category": "Cat1",
        "instructor": "Inst1",
        "duration_hours": 10,
        "level": "Beginner",
        "price": 100.00,
        "description": "Desc A"
    },
    {
        "id": 2,
        "title": "Curso B",
        "category": "Cat2",
        "instructor": "Inst2",
        "duration_hours": 20,
        "level": "Intermediate",
        "price": 200.00,
        "description": "Desc B"
    }
]


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([]))
    @patch("os.path.exists", return_value=False)
    def test_get_all_cursos_no_data(self, mock_exists, mock_file):
        """Test GET /cursos when no data file exists (should return 404)."""
        response = self.app.get("/cursos")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"message": "No courses found"})

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([]))
    @patch("os.path.exists", return_value=True)
    def test_get_all_cursos_empty_data(self, mock_exists, mock_file):
        """Test GET /cursos when data file is empty (should return 404)."""
        response = self.app.get("/cursos")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"message": "No courses found"})

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(MOCK_CURSOS_DATA))
    @patch("os.path.exists", return_value=True)
    def test_get_status(self, mock_exists, mock_file):
        """Test GET /status endpoint (HTTP 200)."""
        response = self.app.get("/status")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("api_name", data)
        self.assertIn("version", data)
        self.assertIn("status", data)
        self.assertEqual(data["status"], "running")

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(MOCK_CURSOS_DATA))
    @patch("os.path.exists", return_value=True)
    def test_get_all_cursos_success(self, mock_exists, mock_file):
        """Test GET /cursos endpoint (HTTP 200 and JSON structure validation)."""
        response = self.app.get("/cursos")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        for curso in data:
            self.assertIn("id", curso)
            self.assertIsInstance(curso["id"], int)

            self.assertIn("title", curso)
            self.assertIsInstance(curso["title"], str)

            self.assertIn("category", curso)
            self.assertIsInstance(curso["category"], str)

            self.assertIn("instructor", curso)
            self.assertIsInstance(curso["instructor"], str)

            self.assertIn("duration_hours", curso)
            self.assertIsInstance(curso["duration_hours"], int)

            self.assertIn("level", curso)
            self.assertIsInstance(curso["level"], str)

            self.assertIn("price", curso)
            self.assertIsInstance(curso["price"], float)

            self.assertIn("description", curso)
            self.assertIsInstance(curso["description"], str)

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(MOCK_CURSOS_DATA))
    @patch("os.path.exists", return_value=True)
    def test_get_curso_by_id_success(self, mock_exists, mock_file):
        """Test GET /cursos/{id} for an existing course (HTTP 200)."""
        response = self.app.get("/cursos/1")
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], "Curso A")

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(MOCK_CURSOS_DATA))
    @patch("os.path.exists", return_value=True)
    def test_get_curso_by_id_not_found(self, mock_exists, mock_file):
        """Test GET /cursos/{id} for a non-existent course (HTTP 404)."""
        response = self.app.get("/cursos/999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"message": "Course not found"})

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(MOCK_CURSOS_DATA))
    @patch("os.path.exists", return_value=True)
    def test_get_curso_by_id_invalid_type(self, mock_exists, mock_file):
        """Test GET /cursos/{id} with an invalid ID type."""
        response = self.app.get("/cursos/abc")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()