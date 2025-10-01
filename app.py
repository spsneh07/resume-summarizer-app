import streamlit as st
from transformers import pipeline

# Use a Streamlit decorator to cache the model and prevent reloading
@st.cache_resource
def load_summarizer():
    """
    Loads the summarization model from Hugging Face.
    This function is cached so the model is only loaded once.
    """
    model = pipeline("summarization", model="facebook/bart-large-cnn")
    return model

# --- App Layout ---

# Set the title of the web app
st.title("📄 Resume Summarizer")

# Create a text area for the user to paste their resume
resume_text = st.text_area("Paste your full resume text here:", height=300)

# Create a button to trigger the summarization
if st.button("Generate Summary"):
    if resume_text:
        # If text is provided, load the model and generate the summary
        summarizer = load_summarizer()
        summary = summarizer(resume_text, max_length=150, min_length=50, do_sample=False)
        
        # Display the summary
        st.subheader("Here is your summary:")
        st.write(summary[0]['summary_text'])
    else:
        # If no text is provided, show a warning
        st.warning("Please paste your resume text above.")