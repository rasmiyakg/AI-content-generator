# ✨ AI Content Generator

An AI-powered web application built using Python and Streamlit that helps users generate and summarize written content using an AI model through the Groq API.

## 🚀 Features

* **Blog Post Generation:** Generate blog posts based on a given topic.
* **Social Media Caption Generation:** Generate three caption options for social media.
* **Text Summarization:** Summarize long text while preserving the main ideas.
* **Customizable Writing Tone:** Choose Professional, Friendly, Creative, Formal, or Casual.
* **Content Length Selection:** Choose Short, Medium, or Long content.
* **Editable Output:** Edit the generated content directly in the application.
* **Download Content:** Download the generated text as a `.txt` file.
* **Error Handling:** Display helpful messages when content generation fails.

## 🛠️ Technologies Used

* Python
* Streamlit
* Groq API
* GPT-OSS 120B model
* Python-dotenv

## 📋 Prerequisites

Before running the project, ensure that Python and pip are installed on your computer.

You will also need a Groq API key.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rasmiy akg/AI-content-generator.git
```

Replace the repository URL with the exact URL shown on your GitHub page if necessary.

### 2. Navigate to the project folder

```bash
cd AI-content-generator
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a file named `.env` in the project folder and add your Groq API key:

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your web browser.

## 💡 How It Works

1. The user selects a content type.
2. The user enters a topic or text.
3. The user selects a writing tone and content length.
4. The application creates a prompt based on the user's selections.
5. The prompt is sent to the configured AI model through the Groq API.
6. The generated content is displayed for the user to review, edit, and download.

## 🎯 Project Objective

The objective of this project is to simplify content creation and summarization through an interactive AI-powered application.

## 🔮 Future Improvements

* Support additional content formats.
* Provide more customization options.
* Improve content quality and output controls.
* Add options to save and manage previously generated content.

## 👩‍💻 Author

Rasmiya KG

---

*Developed as a hands-on project to explore Python, Streamlit, API integration, and AI-powered content generation.*
