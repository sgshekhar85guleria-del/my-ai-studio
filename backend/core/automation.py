import os


class Automation:

    def handle(self, prompt):

        text = prompt.lower()

        # 🔥 CREATE FILE
        if text.startswith("create file"):
            try:
                name = text.replace("create file", "").strip()

                with open(name, "w") as f:
                    f.write("File created by AI")

                return f"✅ File '{name}' created successfully"

            except Exception as e:
                return f"❌ Error: {str(e)}"

        # 📁 CREATE FOLDER
        if text.startswith("create folder"):
            try:
                name = text.replace("create folder", "").strip()

                os.makedirs(name, exist_ok=True)

                return f"📁 Folder '{name}' created"

            except Exception as e:
                return f"❌ Error: {str(e)}"

        # 📄 READ FILE
        if text.startswith("read file"):
            try:
                name = text.replace("read file", "").strip()

                with open(name, "r") as f:
                    content = f.read()

                return f"📄 Content:\n{content}"

            except Exception as e:
                return f"❌ Error: {str(e)}"

        # ❌ DELETE FILE
        if text.startswith("delete file"):
            try:
                name = text.replace("delete file", "").strip()

                os.remove(name)

                return f"🗑 File '{name}' deleted"

            except Exception as e:
                return f"❌ Error: {str(e)}"

        # 📂 LIST FILES
        if text == "list files":
            try:
                files = os.listdir()

                return f"📂 Files:\n{files}"

            except Exception as e:
                return f"❌ Error: {str(e)}"

        return None