from abc import ABC, abstractmethod

class BaseAIRunner(ABC):

    @abstractmethod
    def generate_text(self, prompt: str):
        pass

    @abstractmethod
    def generate_image(self, prompt: str):
        pass

    @abstractmethod
    def generate_video(self, prompt: str):
        pass
