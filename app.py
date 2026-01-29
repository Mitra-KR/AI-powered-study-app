import streamlit as st
from transformers import pipeline

# -------------------------------
# Load Model (Stable)
# -------------------------------
@st.cache_resource
def load_model():
    return pipeline(
        task="text-generation",
        model="gpt2"
    )

model = load_model()

st.title("📘 AI Powered Study Buddy")

option = st.selectbox(
    "Choose an option:",
    ["Explain Topic", "Summarize Notes", "Generate Flashcards"]
)

user_input = st.text_area("Enter topic or paragraph:")

# -------------------------------
# Functions
# -------------------------------
def explain_topic(topic):
    prompt = f"Explain {topic} in 5 simple lines:\n"
    output = model(prompt, max_new_tokens=80)
    return output[0]["generated_text"]


def summarize_notes(text):
    prompt = f"Summarize this paragraph in 4 bullet points:\n{text}\n"
    output = model(prompt, max_new_tokens=100)
    return output[0]["generated_text"]


def flashcards(topic):
    prompt = f"""
Create 5 flashcards on {topic}.

Flashcard 1:
Q:
A:

Flashcard 2:
Q:
A:

Flashcard 3:
Q:
A:

Flashcard 4:
Q:
A:

Flashcard 5:
Q:
A:
"""
    output = model(prompt, max_new_tokens=180)
    return output[0]["generated_text"]

# -------------------------------
# Button
# -------------------------------
if st.button("Generate Output"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a topic or paragraph.")
    else:

        if option == "Explain Topic":
            st.subheader("📖 Explanation")
            st.success(explain_topic(user_input))

        elif option == "Summarize Notes":
            st.subheader("📌 Summary")
            st.info(summarize_notes(user_input))

        elif option == "Generate Flashcards":
            st.subheader("🧠 Flashcards")
            st.write(flashcards(user_input))
