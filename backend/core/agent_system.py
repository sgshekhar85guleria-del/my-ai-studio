class AgentSystem:

    def run(self, prompt):

        # 🧠 PLANNER
        plan = f"Plan: Understand and execute task -> {prompt}"

        # ⚙️ EXECUTOR
        execution = f"Execution: Task '{prompt}' executed"

        # 🔍 REVIEWER
        review = f"Review: Task '{prompt}' completed successfully"

        return f"{plan}\n\n{execution}\n\n{review}"    