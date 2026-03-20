import streamlit as st
from web_search import web_search
from jd_scorer import score_candidate
from resume_parser import extract_text_from_pdf
from openai import OpenAI
from config import get_openai_key
from database import create_table, save_candidate, get_all_candidates

# Initialize OpenAI
client = OpenAI(api_key=get_openai_key())

# Initialize DB
create_table()

st.set_page_config(page_title="JobMatch AI", layout="wide")

st.title("🚀 JobMatch AI - Smart Resume Analyzer")
st.caption("Match resumes with jobs using AI")

# Tabs
tab1, tab2 = st.tabs(["🔍 Web Search", "📊 Resume Scorer"])

# ---------------- WEB SEARCH ----------------
with tab1:
    st.header("Search Latest Info")

    query = st.text_input("Enter search query")

    if st.button("Search"):
        if query:
            results = web_search(query)

            for r in results:
                st.subheader(r["title"])
                st.write(r["url"])
                st.write(r["content"])
                st.markdown("---")
        else:
            st.warning("Please enter a query")


# ---------------- RESUME SCORER ----------------
with tab2:
    st.header("Upload Resume & Match Job")

    col1, col2 = st.columns(2)

    with col1:
        uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    with col2:
        jd = st.text_area("Paste Job Description")

    if st.button("Analyze Resume"):
        if uploaded_file and jd:

            # ✅ STEP 1: Extract Resume
            try:
                resume_text = extract_text_from_pdf(uploaded_file)
            except Exception as e:
                st.error("❌ Error reading PDF")
                st.stop()

            # ✅ STEP 2: ADD SPINNER HERE (IMPORTANT LOCATION)
            # 🔥 This is EXACT place to add spinner
            with st.spinner("Analyzing resume..."):
                result = score_candidate(resume_text, jd)

            # ✅ STEP 3: Display Results
            st.success(f"🎯 Match Score: {result['score']}%")
            st.progress(result["score"] / 100)

            st.write(f"✅ Matched Skills ({len(result['matched_skills'])}):")
            st.write(result["matched_skills"])

            st.write(f"❌ Missing Skills ({len(result['missing_skills'])}):")
            st.write(result["missing_skills"])

            st.write(f"📊 Total Required Skills: {result['total_required']}")

            # 💾 Save to DB
            save_candidate(
                result["score"],
                result["matched_skills"],
                result["missing_skills"],
                jd
            )

            # ---------------- AI SUGGESTIONS ----------------
            st.subheader("🤖 AI Suggestions")

            prompt = f"""
            Candidate Resume:
            {resume_text[:2000]}

            Job Description:
            {jd}

            Matched Skills: {result['matched_skills']}
            Missing Skills: {result['missing_skills']}

            Give:
            1. How to improve this resume
            2. What skills to add
            3. Why the score is low or high
            """

            # ✅ OPTIONAL: Add spinner for AI also
            with st.spinner("Generating AI suggestions..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}]
                    )

                    ai_output = response.choices[0].message.content
                    st.write(ai_output)

                except Exception as e:
                    st.error("❌ Error generating AI suggestions")

            st.text_area("Extracted Resume Text", resume_text[:1000])

        else:
            st.warning("Please upload resume and enter job description")


# ---------------- HISTORY ----------------
st.markdown("---")
st.header("📊 Saved Candidates")

if st.button("Show History"):
    data = get_all_candidates()

    for row in data:
        st.write(f"ID: {row[0]}")
        st.write(f"Score: {row[1]}%")
        st.write(f"Matched Skills: {row[2]}")
        st.write(f"Missing Skills: {row[3]}")
        st.write(f"Job Description: {row[4][:100]}")
        st.markdown("---")