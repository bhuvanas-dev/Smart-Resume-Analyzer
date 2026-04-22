import streamlit as st
import PyPDF2

# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to analyze resume
def analyze_resume(text):
    keywords = ["python", "machine learning", "data analysis", "sql", "projects", "internship"]
    score = 0
    missing = []

    text = text.lower()

    for keyword in keywords:
        if keyword in text:
            score += 15
        else:
            missing.append(keyword)

    return score, missing

# Streamlit UI
st.title("📄 Smart Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📃 Extracted Text")
    st.write(text[:1000])  # show first 1000 characters

    score, missing = analyze_resume(text)

    st.subheader("📊 Resume Score")
    st.success(f"Your Resume Score: {score}/100")

    st.subheader("❌ Missing Keywords")
    if missing:
        for m in missing:
            st.write(f"- {m}")
    else:
        st.write("Great! No major keywords missing 🎉")