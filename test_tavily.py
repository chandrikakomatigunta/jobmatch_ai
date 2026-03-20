from tavily import TavilyClient

# ✅ IMPORTANT: key must be inside quotes
api_key = "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"

client = TavilyClient(api_key=api_key)

response = client.search(
    query="latest AI news",
    search_depth="basic"
)

for r in response["results"]:
    print("Title:", r["title"])
    print("URL:", r["url"])
    print("-" * 40)