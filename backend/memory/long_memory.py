import json
import os


class LongMemory:

    FILE = "memory_store.json"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump({}, f)

    def save(self, key, value):
        with open(self.FILE, "r") as f:
            data = json.load(f)

        data[key] = value

        with open(self.FILE, "w") as f:
            json.dump(data, f)

    def get(self, key):
        with open(self.FILE, "r") as f:
            data = json.load(f)

        return data.get(key, None)