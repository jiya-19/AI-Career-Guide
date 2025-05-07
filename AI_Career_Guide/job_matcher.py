from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # To allow access from HTML

# Load CSV once
csv_path = os.path.join(os.path.dirname(__file__), "job_roles.csv")
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    raise FileNotFoundError(f"CSV file not found at {csv_path}. Please ensure the file exists.")

@app.route("/match_jobs", methods=["POST"])
def match_jobs():
    try:
        data = request.get_json()
        if not data or "skills" not in data:
            return jsonify({"error": "Invalid input. 'skills' field is required."}), 400

        skills = data.get("skills", "").lower().split(",")
        matches = []

        for skill in skills:
            skill = skill.strip()
            matched_rows = df[df['Skill'].str.lower() == skill]
            for _, row in matched_rows.iterrows():
                matches.append({
                    "title": row["Job Title"],
                    "description": row["Job Description"]
                })

        return jsonify(matches)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)