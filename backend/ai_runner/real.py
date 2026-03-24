import requests


class RealAIRunner:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "llama3.1:8b"

    def generate(self, prompt):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        if response.status_code == 200:
            return response.json()["response"]

        return "Error generating response"