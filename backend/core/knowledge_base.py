import json
import os
import re


class KnowledgeBase:

    def __init__(self):
        self.file_path = "knowledge.json"

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def normalize(self, text):
        # 🔥 Smart cleaning
        text = text.lower()
        text = re.sub(r'[^a-z0-9 ]', '', text)   # remove symbols
        text = re.sub(r'\s+', ' ', text).strip() # remove extra spaces
        return text

    def save(self, prompt, response):

        with open(self.file_path, "r") as f:
            data = json.load(f)

        data.append({
            "prompt": self.normalize(prompt),
            "response": response
        })

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def search(self, prompt):

        prompt = self.normalize(prompt)

        with open(self.file_path, "r") as f:
            data = json.load(f)

        for item in reversed(data):

            saved_prompt = item["prompt"]

            # 🔥 Advanced matching
            if prompt == saved_prompt:
                return item["response"]

            if prompt in saved_prompt or saved_prompt in prompt:
                return item["response"]

        return None