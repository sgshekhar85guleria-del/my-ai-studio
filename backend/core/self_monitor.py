class SelfMonitor:

    def analyze(self, prompt, response):

        score = 0
        suggestions = []

        # 🧠 relevance check
        if prompt.lower() in response.lower():
            score += 2
        else:
            suggestions.append("Response may not be fully relevant")

        # 📏 length check
        if len(response) > 50:
            score += 2
        else:
            suggestions.append("Response too short")

        # 📚 quality check
        if "." in response:
            score += 1
        else:
            suggestions.append("Response lacks structure")

        return {
            "score": score,
            "suggestions": suggestions
        }