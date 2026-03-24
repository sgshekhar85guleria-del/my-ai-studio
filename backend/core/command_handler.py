class CommandHandler:

    def handle(self, prompt, memory, system):

        cmd = prompt.strip().lower()

        if cmd == "/clear":
            memory.clear()
            return "🧹 Memory cleared successfully"

        elif cmd == "/logs":
            logs = system.get_logs()
            return f"📊 Logs: {logs}"

        elif cmd == "/memory":
            return f"🧠 Memory: {memory.messages}"

        return None