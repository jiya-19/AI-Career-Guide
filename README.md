
# AI Career Guide

The **AI Career Guide** is an integrated web-based toolkit designed to assist users in their career development journey. It includes modules for resume analysis, job-role matching, and a chatbot for interview preparation — all powered by artificial intelligence.

---

## 🔧 Features

### 1. **Resume Analyzer**
- Parses uploaded resumes.
- Extracts skills, experience, and education details.
- Matches resumes to suitable job roles.

**Main file**: `resume_parser.py`

### 2. **Job Matcher**
- Matches user profiles/resumes with appropriate job roles.
- Uses similarity scoring between resume content and job descriptions.

**Main file**: `job_matcher.py`

### 3. **Interview Chatbot**
- Simulates mock interview sessions using pre-defined question datasets.
- Responds with feedback and tips based on AI prompts.

**Main file**: `interview_chatbot.py`

---

## 📁 Project Structure

```
AI_Career_Guide/
│
├── app.py                             # Resume analyzer backend 
├── resume_parser.py                   # Resume analyzer backend support
├── job_matcher.py                     # Job-role matching backend
├── interview_chatbot.py               # Interview chatbot backend
│
├── Career QA Dataset.csv              # Q&A dataset for the chatbot
├── customSmalltalkResponses_en.csv    # Chatbot's smalltalk responses
├── Mock-Interview-Questions.csv       # Interview questions dataset
├── job_roles.csv                      # Job roles with skill requirements
├── jobs_resume.csv                    # Sample resume-job mappings
│
├── requirements.txt                   # Python dependencies
│
├── *.html                             # Web interfaces for each module
│
└── Interview preparation chatbox_files/
    └── *                              # Assets for the chatbot web UI
```

---

## 🚀 How to Run

### 1. **Install Dependencies**
Make sure Python 3.8+ is installed, then run:
```bash
pip install -r requirements.txt
```

### 2. **Run the Application**
Assuming `app.py` is the entry point:
```bash
python app.py
```

Then, open the relevant HTML files in your browser (e.g., `Resume analyzer.html`, `Job matching.html`, etc.).

---

## 📊 Datasets

- **Career QA Dataset.csv** – Used for the interview chatbot's knowledge base.
- **Mock-Interview-Questions.csv** – Contains a variety of interview questions.
- **jobs_resume.csv** – Mapping between resumes and job titles.
- **job_roles.csv** – Job titles and their associated skills.

---

## 💡 Use Cases

- Students preparing for job interviews.
- Job seekers refining their resumes.
- Career coaches aiding clients with mock interviews and job-role targeting.

---

## 🤖 Technologies Used

- **Python**
- **Natural Language Processing (NLP)**
- **Flask** *(if `app.py` is a server launcher)*
- **HTML/CSS/JavaScript**

---

## 📬 Contributions

Contributions and feature enhancements are welcome! Please open an issue or submit a pull request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
