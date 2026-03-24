class SecurityLayer:

    def check(self, prompt):

        blocked_keywords = [
            "hack",
            "bypass",
            "override",
            "ignore instructions",
            "system prompt",
            "jailbreak"
        ]

        for word in blocked_keywords:
            if word in prompt.lower():
                return False, "Blocked: Unsafe input detected"

        return True, "Safe"