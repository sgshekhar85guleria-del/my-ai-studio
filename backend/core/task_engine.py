import os
import shutil


class TaskEngine:

    def handle(self, prompt):

        text = prompt.lower()

        # 🔥 ORGANIZE FILES
        if "organize files" in text:

            try:
                files = os.listdir()

                if not os.path.exists("organized"):
                    os.makedirs("organized")

                for f in files:
                    if os.path.isfile(f):
                        shutil.move(f, f"organized/{f}")

                return "📂 Files organized into 'organized' folder"

            except Exception as e:
                return f"❌ Error: {str(e)}"

        return None