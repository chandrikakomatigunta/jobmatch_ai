import streamlit as st

# -----------------------------
# Simple JD Matching Logic
# -----------------------------
def score_candidate(profile, jd):
    profile_text = str(profile).lower()
    jd = str(jd).lower()

    skills = ["python", "sql", "machine learning", "backend", "cloud", "api"]

    score = 0
    matched = []
    missing = []

    for skill in skills:
        if skill in jd:
            if skill in profile_text:
                score += 1
                matched.append(skill)
            else:
                missing.append(skill)

    total = len(skills)
    percentage = int((score / total) * 100)

    return percentage, matched, missing


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="JobMatch AI", layout="centered")

st.title("🤖 JobMatch AI")
st.subheader("Match Resume with Job Description")

st.write("Paste candidate profile and job description to see matching score.")

# Inputs
profile = st.text_area("📄 Candidate Profile")
jd = st.text_area("📌 Job Description")

# Button
if st.button("Analyze Match"):

    if not profile or not jd:
        st.warning("Please enter both profile and job description")
    else:
        score, matched, missing = score_candidate(profile, jd)

        st.success(f"Match Score: {score}%")

        st.write("### ✅ Matching Skills")
        if matched:
            st.write(", ".join(matched))
        else:
            st.write("No matching skills found")

        st.write("### ❌ Missing Skills")
        if missing:
            st.write(", ".join(missing))
        else:
            st.write("No missing skills 🎉")
