import streamlit as st

# -----------------------------
<<<<<<< HEAD
# Matching Logic
=======
# Simple JD Matching Logic
>>>>>>> 361a1ced64cdf4471905f6e3a48ae320530119da
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
<<<<<<< HEAD
# UI
# -----------------------------
st.set_page_config(page_title="JobMatch AI", layout="centered")

st.markdown("# 🚀 JobMatch AI")
st.markdown("### AI-powered Resume vs Job Matching Tool")
st.divider()

# -----------------------------
# Resume Upload
# -----------------------------
uploaded_file = st.file_uploader("📂 Upload Resume (txt file)", type=["txt"])

profile = ""

if uploaded_file:
    profile = uploaded_file.read().decode("utf-8")
    st.success("Resume uploaded successfully!")

# -----------------------------
# Inputs
# -----------------------------
profile_input = st.text_area("📄 Candidate Profile (or upload file above)")
jd = st.text_area("📌 Job Description")

# If user typed manually, use that
if profile_input:
    profile = profile_input

# -----------------------------
# Button Action
# -----------------------------
if st.button("Analyze Match"):

    if not profile or not jd:
        st.warning("Please enter or upload profile and job description")
    else:
        with st.spinner("Analyzing resume..."):

            score, matched, missing = score_candidate(profile, jd)

            st.success(f"Match Score: {score}%")

            # Progress bar
            st.progress(score / 100)

            # Matching skills
            st.write("### ✅ Matching Skills")
            if matched:
                st.write(", ".join(matched))
            else:
                st.write("No matching skills found")

            # Missing skills
            st.write("### ❌ Missing Skills")
            if missing:
                st.write(", ".join(missing))
            else:
                st.write("No missing skills 🎉")
=======
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
>>>>>>> 361a1ced64cdf4471905f6e3a48ae320530119da
