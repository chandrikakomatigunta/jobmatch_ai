from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")


def web_search(candidate_name, role=None):
    return {
        "found": True,
        "url": f"https://linkedin.com/in/{candidate_name.replace(' ', '').lower()}",
        "summary": f"{candidate_name} is a {role} skilled in Python, SQL, backend, and cloud."
    }