from core.self_monitor import SelfMonitor
from core.self_improver import SelfImprover
from core.knowledge_base import KnowledgeBase
from core.system_monitor import SystemMonitor
from core.bug_detector import BugDetector
from core.command_handler import CommandHandler
from core.automation import Automation
from core.task_engine import TaskEngine
from core.auto_mode import AutoMode
from core.agent_system import AgentSystem
from memory.long_memory import LongMemory


class SupremeCore:

    def __init__(self, runner, memory, security):
        self.runner = runner
        self.memory = memory
        self.security = security
        self.monitor = SelfMonitor()
        self.improver = SelfImprover()
        self.knowledge = KnowledgeBase()
        self.system = SystemMonitor()
        self.bug = BugDetector()
        self.command = CommandHandler()
        self.automation = Automation()
        self.task_engine = TaskEngine()
        self.auto = AutoMode(self)
        self.agent = AgentSystem()

        # 🔥 LONG MEMORY
        self.long_memory = LongMemory()

    def process(self, prompt):

        text = prompt.lower()

        # 🔥 SAVE NAME
        if "my name is" in text:
            name = text.replace("my name is", "").strip()
            self.long_memory.save("name", name)
            return f"Nice to meet you, {name}"

        # 🔥 GET NAME
        if "what is my name" in text:
            name = self.long_memory.get("name")
            if name:
                return f"Your name is {name}"
            return "I don't know your name yet"

        # 🔥 AUTO MODE
        if text == "/auto on":
            return self.auto.start()

        if text == "/auto off":
            return self.auto.stop()

        # 🔥 AGENT MODE
        if text.startswith("agent"):
            return self.agent.run(prompt)

        # 🟢 COMMAND
        cmd_response = self.command.handle(prompt, self.memory, self.system)
        if cmd_response:
            self.system.log(f"Command executed: {prompt}")
            return cmd_response

        # 🟢 TASK ENGINE
        task_response = self.task_engine.handle(prompt)
        if task_response:
            self.system.log(f"Task executed: {prompt}")
            return task_response

        # 🟢 AUTOMATION
        auto_response = self.automation.handle(prompt)
        if auto_response:
            self.system.log(f"Automation executed: {prompt}")
            return auto_response

        # 🛡 SECURITY
        safe, message = self.security.check(prompt)
        if not safe:
            self.system.log("Security blocked input")
            return message

        # 🧠 KNOWLEDGE
        saved = self.knowledge.search(prompt)
        if saved:
            self.system.log("Used saved knowledge")
            return saved

        # 🧠 MEMORY
        self.memory.add_user_message(prompt)

        context_messages = self.memory.get_recent_context()

        context_text = "You are an intelligent AI assistant.\n"
        context_text += "Remember user information when needed.\n\n"

        for msg in context_messages:
            context_text += f"{msg['role']}: {msg['content']}\n"

        context_text += "assistant:"

        response = self.runner.generate(context_text)

        issues = self.bug.detect(prompt, response)
        if issues:
            self.system.log(f"Issues detected: {issues}")

        analysis = self.monitor.analyze(prompt, response)

        improved_response, changed = self.improver.improve(
            prompt, response, analysis["score"]
        )

        if changed:
            self.system.log("Response improved")

        self.knowledge.save(prompt, improved_response)
        self.memory.add_ai_message(improved_response)

        return improved_response