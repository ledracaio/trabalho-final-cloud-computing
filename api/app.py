
from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Configuration
API_VERSION = "1.0.0"
API_NAME = "Online Courses API"
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'cursos.json')

def load_cursos_data():
    """Loads course data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/status', methods=['GET'])
def get_status():
    """Returns the API status, name, and version."""
    return jsonify({
        "api_name": API_NAME,
        "version": API_VERSION,
        "status": "running"
    }), 200

@app.route('/cursos', methods=['GET'])
def get_all_cursos():
    """Returns all courses."""
    cursos = load_cursos_data()
    if not cursos:
        return jsonify({"message": "No courses found"}), 404
    return jsonify(cursos), 200

@app.route('/cursos/<int:curso_id>', methods=['GET'])
def get_curso_by_id(curso_id):
    """Returns a single course by its ID."""
    cursos = load_cursos_data()
    curso = next((c for c in cursos if c['id'] == curso_id), None)
    if curso:
        return jsonify(curso), 200
    return jsonify({"message": "Course not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
