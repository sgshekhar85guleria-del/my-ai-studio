class DecisionEngine:

    def analyze(self, prompt):

        prompt = prompt.lower()

        if "research" in prompt or "latest" in prompt or "news" in prompt:
            return "research"

        elif "code" in prompt or "build" in prompt:
            return "deep_thinking"

        else:
            return "normal"