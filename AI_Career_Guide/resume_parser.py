import fitz  # PyMuPDF for PDFs
import spacy
import docx  # For .docx files

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Only PDF and DOCX are supported.")

def extract_skills(text, skill_list):
    doc = nlp(text.lower())
    found_skills = set()
    for token in doc:
        if token.text in skill_list:
            found_skills.add(token.text)
    return list(found_skills)
