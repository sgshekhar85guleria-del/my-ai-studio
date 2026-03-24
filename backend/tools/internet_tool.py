import requests


class InternetTool:

    def search(self, query):

        try:
            url = f"https://api.duckduckgo.com/?q={query}&format=json"
            res = requests.get(url).json()

            if res.get("AbstractText"):
                return res["AbstractText"]

            return "No clear result found"

        except Exception as e:
            return f"Internet error: {str(e)}"