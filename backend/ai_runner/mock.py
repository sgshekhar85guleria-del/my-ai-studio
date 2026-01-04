from .base import BaseAIRunner

class MockAIRunner(BaseAIRunner):

    def generate_text(self, prompt: str):
        return {
            "mode": "mock",
            "type": "text",
            "prompt": prompt,
            "result": f"Mock text generated for: {prompt}"
        }

    def generate_image(self, prompt: str):
        return {
            "mode": "mock",
            "type": "image",
            "prompt": prompt,
            "result": f"Mock image generated for: {prompt}"
        }

    def generate_video(self, prompt: str):
        return {
            "mode": "mock",
            "type": "video",
            "prompt": prompt,
            "result": f"Mock video generated for: {prompt}"
        }
