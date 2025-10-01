# Deployed Resume Summarizer 📄🚀

## Objective
This project is a web-based tool that automatically generates a concise summary from a long block of resume text. It leverages a powerful pre-trained NLP model and is deployed as a live web application using Streamlit. This was completed as Task 3 of the 2nd Year Tasks.

---

## Live Demo
You can access and use the live application here:

**(INSERT YOUR STREAMLIT APP URL HERE)**

### Screenshots


---

## Tech Stack
* **Language:** Python
* **Libraries:**
    * Streamlit (for the web application)
    * Hugging Face `transformers` (for the summarization model)
    * PyTorch
    * SentencePiece
* **Model:** `facebook/bart-large-cnn`
* **Deployment:** Streamlit Community Cloud

---

## Implementation Details
1.  **Core Logic:** The summarization is powered by a pre-trained BART model from Hugging Face, accessed via the `pipeline` API. The model is cached to ensure fast performance after the initial load.
2.  **Web Interface:** The user interface is built with Streamlit. It features a title, a text area for input, and a button to trigger the summarization.
3.  **Deployment:** The application is deployed on the Streamlit Community Cloud. The `requirements.txt` file is used to specify the necessary libraries for the deployment environment.

---

## How to Run Locally
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/resume-summarizer-app.git](https://github.com/YOUR_USERNAME/resume-summarizer-app.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd resume-summarizer-app
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
