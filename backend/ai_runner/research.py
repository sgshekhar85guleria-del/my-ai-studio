import urllib.parse

def internet_search(query: str):

```
encoded = urllib.parse.quote_plus(query)

search_url = f"https://duckduckgo.com/?q={encoded}"

return {
    "search_url": search_url
}
```
