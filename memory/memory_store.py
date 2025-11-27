import json
import os

class MemoryStore:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        self.data = self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_memory(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=2)

    def add_course_data(self, course_name, data):
        if "courses" not in self.data:
            self.data["courses"] = {}
        self.data["courses"][course_name] = data
        self.save_memory()

    def get_course_data(self, course_name):
        return self.data.get("courses", {}).get(course_name, {})
