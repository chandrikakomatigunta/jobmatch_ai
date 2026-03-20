from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")


def jd_scorer(candidate_name, candidate_profile, job_description):

    profile = str(candidate_profile).lower()

    skills = ["python", "sql", "backend", "cloud"]

    score = 0
    strengths = []
    gaps = []

    for skill in skills:
        if skill in profile:
            score += 25
            strengths.append(skill)
        else:
            gaps.append(skill)

    return {
        "score": score,
        "strengths": strengths,
        "gaps": gaps
    }