# 🤖 JobMatch AI

JobMatch AI is an AI-powered web application that analyzes resumes and matches them with job descriptions using intelligent scoring, web search, and AI suggestions.

---

## 🚀 Features

* 📄 **Resume Upload (PDF)**

  * Extracts text from resumes automatically

* 📊 **Smart Job Matching**

  * Calculates match percentage based on skills

* 🤖 **AI Suggestions (OpenAI)**

  * Resume improvement tips
  * Missing skills recommendation
  * Score explanation

* 🔍 **Web Search (Tavily API)**

  * Fetch latest job trends and tech insights

* 💾 **Database (SQLite)**

  * Save candidate results
  * View history

* 🎨 **Interactive UI (Streamlit)**

---

## 🛠️ Tech Stack

* Python
* Streamlit
* OpenAI API
* Tavily API
* SQLite
* PyPDF2

---

## 📁 Project Structure

```
jobmatch_ai/
│
├── app.py
├── main.py
├── config.py
├── database.py
├── resume_parser.py
├── requirements.txt
│
├── tools/
│   ├── web_search_tool.py
│   ├── jd_score_tool.py
│   └── db_tool.py
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/jobmatch-ai.git
cd jobmatch-ai
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

(Add your deployed Streamlit link here)

---

## 📸 Screenshots

(Add screenshots of your app here)

---

## 📌 Future Improvements

* Advanced NLP-based scoring
* Resume keyword highlighting
* Multi-job comparison
* User authentication

---

## 👨‍💻 Author

Chandrika komatigunta
