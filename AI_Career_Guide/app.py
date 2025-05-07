from flask import Flask, request, jsonify
import pandas as pd
import os
from resume_parser import extract_text, extract_skills
from flask_cors import CORS
import glob

UPLOAD_FOLDER = 'uploads'
RESUME_FOLDER = 'Resumes'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


# Initialize directly
job_df = pd.read_csv("AI_Career_Guide/jobs_resume.csv")
all_skills = set()
for skills in job_df['skills']:
    all_skills.update(skills.split(','))

# API endpoint
@app.route('/analyze_resume', methods=['POST', 'OPTIONS'])
def analyze_resume():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200

    if 'resume' not in request.files:
        return jsonify({'error': 'No resume uploaded'}), 400

    uploaded_file = request.files['resume']
    if uploaded_file.filename.endswith('.pdf') or uploaded_file.filename.endswith('.docx'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(filepath)
        resume_text = extract_text(filepath)
        resume_skills = extract_skills(resume_text, all_skills)

        match_scores = []
        improvement_areas = {}
        for _, row in job_df.iterrows():
            required_skills = set(row['skills'].split(','))
            match_count = len(required_skills & set(resume_skills))
            score = (match_count / len(required_skills)) * 100 if required_skills else 0
            missing_skills = list(required_skills - set(resume_skills))
            match_scores.append((row['role'], score))
            improvement_areas[row['role']] = missing_skills

        best_match = max(match_scores, key=lambda x: x[1])
        best_role = best_match[0]
        best_score = best_match[1]
        improvements = improvement_areas[best_role]

        return jsonify({
            'score': round(best_score, 2),
            'best_role': best_role,
            'improvements': improvements
        })
    else:
        return jsonify({'error': 'Only PDF or DOCX files are supported'}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10000)
