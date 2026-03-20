from openai import OpenAI
from config import get_openai_key
from web_search import web_search
from jd_scorer import score_candidate

client = OpenAI(api_key=get_openai_key())


def ai_agent(user_input):
    print("User:", user_input)

    # Step 1: AI reasoning
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI agent. Decide whether to search web or score a candidate."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    decision = response.choices[0].message.content
    print("\nAI Decision:", decision)

    # Step 2: Tool selection (simple logic)

    # 👉 WEB SEARCH
    if "latest" in user_input.lower() or "news" in user_input.lower():
        print("\n🔍 Using Tavily...\n")
        results = web_search(user_input)

        for r in results[:3]:
            print("Title:", r["title"])
            print("URL:", r["url"])
            print("Summary:", r["content"])
            print("-" * 40)

    # 👉 JD SCORING
    elif "score" in user_input.lower():
        print("\n📊 Scoring Candidate...\n")

        profile = "Python developer with SQL and backend experience"
        jd = "Looking for Python backend developer with cloud and API skills"

        result = score_candidate(profile, jd)

        print("Score:", result["score"])
        print("Strengths:", result["strengths"])
        print("Gaps:", result["gaps"])

    # 👉 NORMAL AI RESPONSE
    else:
        print("\n💬 AI Answer:")
        print(decision)


if __name__ == "__main__":
    ai_agent("score this candidate for backend role")