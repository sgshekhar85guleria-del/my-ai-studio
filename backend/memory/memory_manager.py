class MemoryManager:

    def __init__(self):
        self.messages = []

    def add_user_message(self, message):
        self.messages.append({"role": "user", "content": message})

    def add_ai_message(self, message):
        self.messages.append({"role": "assistant", "content": message})

    def get_recent_context(self, limit=4):
        return self.messages[-limit:]

    def clear(self):
        self.messages = []