import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from groq import Groq


# ---------------- PAGE CONFIGURATION ----------------

load_dotenv()

st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✨",
    layout="centered"
)

API_KEY = os.getenv("GROQ_API_KEY", "").strip()


# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>
    .main {
        background-color: #f8f9fc;
    }

    .hero {
        text-align: center;
        padding: 25px 10px;
    }

    .hero h1 {
        font-size: 38px;
        color: #6546c8;
        margin-bottom: 8px;
    }

    .hero p {
        color: #666666;
        font-size: 16px;
    }

    .stButton > button {
        width: 100%;
        background-color: #6546c8;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <h1>✨ AI Content Generator</h1>
    <p>Create blogs, captions, and summaries with AI.</p>
</div>
""", unsafe_allow_html=True)

st.divider()


# ---------------- INPUT SECTION ----------------

st.subheader("Create Your Content")

content_type = st.selectbox(
    "Choose content type",
    [
        "Blog Post",
        "Social Media Caption",
        "Text Summary"
    ]
)


if content_type == "Text Summary":

    user_input = st.text_area(
        "Enter the text to summarize",
        placeholder="Paste the text you want to summarize...",
        height=180
    )

else:

    user_input = st.text_area(
        "What would you like to create?",
        placeholder="Example: Write about the importance of friendship...",
        height=120
    )


# ---------------- WRITING OPTIONS ----------------

col1, col2 = st.columns(2)

with col1:

    tone = st.selectbox(
        "Writing Tone",
        [
            "Professional",
            "Friendly",
            "Creative",
            "Formal",
            "Casual"
        ]
    )

with col2:

    length = st.selectbox(
        "Content Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )


# ---------------- PROMPT CREATION ----------------

def create_prompt(content_type, user_input, tone, length):

    if content_type == "Blog Post":

        task = (
            "Write a well-structured blog post with an "
            "appropriate title, introduction, main content, "
            "and conclusion."
        )

    elif content_type == "Social Media Caption":

        task = (
            "Write three distinct, engaging social media "
            "caption options based on the user's requirements. "
            "Include relevant hashtags when appropriate."
        )

    else:

        task = (
            "Summarize the supplied text accurately. "
            "Preserve the main ideas and important facts. "
            "Do not invent information that is absent "
            "from the original text."
        )

    prompt = f"""
You are a helpful AI writing assistant.

Task:
{task}

User's topic or text:
{user_input}

Writing tone:
{tone}

Desired length:
{length}

Instructions:
- Follow the selected content type.
- Generate the content in English.
- Keep the writing clear and natural.
- Avoid unnecessary introductions.
- For a blog, provide a suitable title and paragraphs.
- For captions, provide three distinct options.
- For a summary, preserve the original meaning.
- Follow the selected writing tone and content length.
- Return only the requested content.
"""

    return prompt.strip()


# ---------------- GENERATE CONTENT ----------------

if st.button("✨ Generate Content", use_container_width=True):

    if not API_KEY:

        st.error(
            "API key not found. Add GROQ_API_KEY to your .env file."
        )

    elif not user_input.strip():

        st.warning(
            "Please enter a topic or text first."
        )

    else:

        try:

            client = Groq(api_key=API_KEY)

            prompt = create_prompt(
                content_type,
                user_input,
                tone,
                length
            )

            with st.spinner("✨ Generating your content..."):

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an expert content writer. "
                                "Follow the user's instructions carefully "
                                "and generate clear, useful content."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.7,
                    max_completion_tokens=2048
                )

                generated_text = (
                    response.choices[0].message.content or ""
                ).strip()

            if not generated_text:

                st.error(
                    "The AI returned an empty response. Please try again."
                )

            else:

                st.session_state["generated_content"] = generated_text

                st.session_state["generation_time"] = (
                    datetime.now().strftime("%d %b %Y, %I:%M %p")
                )

                st.session_state.pop("edited_content", None)

        except Exception as error:

            error_text = str(error)

            st.error("Content generation failed.")

            if (
                "401" in error_text
                or "authentication" in error_text.lower()
            ):

                st.warning(
                    "Check whether your Groq API key is correct."
                )

            elif (
                "429" in error_text
                or "rate_limit" in error_text.lower()
            ):

                st.warning(
                    "The API rate limit or usage quota has been reached. "
                    "Check your Groq Console usage limits."
                )

            elif "404" in error_text:

                st.warning(
                    "The selected model may be unavailable. "
                    "Check the currently supported models in Groq Console."
                )

            else:

                st.caption(error_text[:500])


# ---------------- OUTPUT SECTION ----------------

if st.session_state.get("generated_content"):

    st.divider()

    st.subheader("📝 Generated Content")

    edited_content = st.text_area(
        "You can edit your content below",
        value=st.session_state["generated_content"],
        height=300,
        key="edited_content"
    )

    st.download_button(
        label="📥 Download Content",
        data=edited_content,
        file_name="generated_content.txt",
        mime="text/plain",
        use_container_width=True
    )

    st.caption(
        "Generated on: "
        + st.session_state.get("generation_time", "")
    )

    if st.button("🗑️ Clear Content"):

        st.session_state.pop("generated_content", None)
        st.session_state.pop("edited_content", None)
        st.session_state.pop("generation_time", None)

        st.rerun()


# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    "<center>Built with Python, Streamlit, and AI</center>",
    unsafe_allow_html=True
)

