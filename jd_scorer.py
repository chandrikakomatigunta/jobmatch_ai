def score_candidate(profile, jd):
    # convert safely
    if isinstance(profile, dict):
        profile_text = profile.get("skills", "")
    else:
        profile_text = str(profile)

    profile_text = profile_text.lower()
    jd = str(jd).lower()

    # expanded skill list
    skills = [
        "python", "sql", "backend", "frontend",
        "react", "node", "api", "docker",
        "kubernetes", "aws", "cloud", "git"
    ]

    matched = []
    missing = []

    for skill in skills:
        if skill in jd:
            if skill in profile_text:
                matched.append(skill)
            else:
                missing.append(skill)

    total_required = len(matched) + len(missing)

    if total_required == 0:
        score_percent = 0
    else:
        score_percent = int((len(matched) / total_required) * 100)

    return {
        "score": score_percent,
        "matched_skills": matched,
        "missing_skills": missing,
        "total_required": total_required
    }