import json
from pathlib import Path

script_path = Path(__file__)
script_dir = script_path.parent
json_file = script_dir / 'database.json'

classmates_initial_data = [
    {"name": "Leigh", "age": 13, "favorite_color": "navy blue", "favorite_subject": "bio", "favorite_song": "eight alone"},
    {"name": "bryce", "age": 14, "favorite_color": "cream", "favorite_subject": "physics", "favorite_song": "Sunday morning"},
    {"name": "melbie", "age": 14, "favorite_color": "White", "favorite_subject": "math", "favorite_song": "double take"},
    {"name": "Viel", "age": 14, "favorite_color": "Pink", "favorite_subject": "Math 2", "favorite_song": "Mundo"},
    {"name": "Dency", "age": 13, "favorite_color": "Blue", "favorite_subject": "Biology", "favorite_song": "Last Night On Earth"}
]

def load_data(filename=json_file):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data, filename=json_file):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data reflected in database.json successfully.")
    except IOError as e:
        print(f"Error writing file: {e}")

def create_students(student_list):
    save_data(student_list)

def read_students():
    data = load_data()
    if not data:
        print("Database is empty.")
    else:
        for student in data:
            print(student)

def update_students_school(campus_name):
    data = load_data()
    for student in data:
        student["school"] = campus_name
    save_data(data)

def delete_by_colors():
    data = load_data()
    forbidden_colors = ["red", "blue", "yellow"]
    filtered_data = [s for s in data if s["favorite_color"].lower() not in forbidden_colors]
    save_data(filtered_data)

if __name__== "_main_":
    create_students(classmates_initial_data)
    update_students_school("PSHS - Central Visayas Campus")
    delete_by_colors()
    print("\nFinal Database Content:")
    read_students()
