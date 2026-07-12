from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query, max_results=3):
    """
    Searches the web and returns a list of results with title, url, and content snippet.
    """
    response = client.search(query=query, max_results=max_results)
    return response["results"]