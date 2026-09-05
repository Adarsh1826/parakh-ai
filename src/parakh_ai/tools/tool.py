from langchain.tools import tool
from ddgs import DDGS

@tool
def web_search(query: str) -> str:
    """Search the web for current information on a given query and return the top results.
    Use this when you need up-to-date facts, news, or information not in your training data."""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        if not results:
            return "No results found for this query."

        formatted = []
        for i, r in enumerate(results, 1):
            formatted.append(
                f"{i}. {r['title']}\n{r['body']}\nSource: {r['href']}"
            )
        return "\n\n".join(formatted)

    except Exception as e:
        return f"Search failed: {str(e)}"