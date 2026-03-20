import streamlit as st
from web_search import web_search
from jd_scorer import score_candidate
from resume_parser import extract_text_from_pdf

st.set_page_config(page_title="JobMatch AI", layout="wide")

st.title("🤖 JobMatch AI")

tab1, tab2 = st.tabs(["🔍 Web Search", "📊 Resume Scorer"])

# ---------------- WEB SEARCH ----------------
with tab1:
    st.header("Search Latest Info")

    query = st.text_input("Enter search query")

    if st.button("Search"):
        results = web_search(query)

        for r in results:
            st.subheader(r["title"])
            st.write(r["url"])
            st.write(r["content"])
            st.markdown("---")

# ---------------- RESUME SCORER ----------------
with tab2:
    st.header("Upload Resume & Match Job")

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    jd = st.text_area("Paste Job Description")

    if st.button("Analyze Resume"):
        if uploaded_file and jd:
            resume_text = extract_text_from_pdf(uploaded_file)

            result = score_candidate(resume_text, jd)

            st.success(f"Match Score: {result['score']}")
            st.write("✅ Strengths:", result["strengths"])
            st.write("❌ Missing Skills:", result["gaps"])

            st.text_area("Extracted Resume Text", resume_text[:1000])
        else:
            st.warning("Please upload resume and enter job description")