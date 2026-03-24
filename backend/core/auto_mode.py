import time
import threading


class AutoMode:

    def __init__(self, core):
        self.core = core
        self.running = False

    def loop(self):

        while self.running:
            try:
                print("🤖 AUTO MODE RUNNING...")

                # 🔥 AI self task
                response = self.core.process("organize files")

                print("AUTO:", response)

                time.sleep(10)

            except Exception as e:
                print("❌ Auto error:", e)

    def start(self):
        if not self.running:
            self.running = True
            thread = threading.Thread(target=self.loop)
            thread.start()
            return "🚀 Auto Mode Started"

        return "⚠️ Already Running"

    def stop(self):
        self.running = False
        return "🛑 Auto Mode Stopped"