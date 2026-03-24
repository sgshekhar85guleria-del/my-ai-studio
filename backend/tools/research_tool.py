import requests


class ResearchTool:

    def research(self, query):

        try:
            url = "https://api.duckduckgo.com/"
            params = {
                "q": query,
                "format": "json"
            }

            res = requests.get(url, params=params)
            data = res.json()

            return data.get("AbstractText", "No data found")

        except Exception:
            return "Research failed"