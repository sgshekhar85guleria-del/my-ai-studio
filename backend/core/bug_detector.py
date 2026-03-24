class BugDetector:

    def detect(self, prompt, response):

        issues = []

        # 🔍 Very basic checks (extendable)
        if not response or len(response.strip()) == 0:
            issues.append("Empty response")

        if "AI response to:" in response:
            issues.append("Mock-style response detected")

        if len(response) < 20:
            issues.append("Response too short")

        return issues