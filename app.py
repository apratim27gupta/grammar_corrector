import streamlit as st
import os
import google.generativeai as genai
import json
genai.configure(api_key=os.getenv("API_KEY"))
import json
model = genai.GenerativeModel(
        "models/gemini-1.5-pro-latest",
        safety_settings =[
      {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
      },
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
      },
    ]
    )
# Mock function for model's API call (replace with actual API call)
def generate_content(prompt):
    # This is where you would call your language model's API
    # For the purpose of this example, we'll just return the prompt
    response = model.generate_content(prompt)
    return response.text

# Define the proofreading rules
rules = """
Spellings and Typos:
Ensure that all words are correctly spelled.
Correct any typographical errors.

Grammatical Inconsistencies:
Check for and correct errors in sentence structure, subject-verb agreement, and other grammatical issues.

Capitalization Issues:
Ensure that proper nouns, the beginnings of sentences, and other necessary words are correctly capitalized.
Fix any incorrect capitalization.

Avoid Repetition of Words:
Identify and reduce the repetition of words or phrases.
Use synonyms or rephrase sentences to enhance readability and avoid redundancy.

Usage of Numbers or Numerals:
Follow the rule: Write out numbers from one to one hundred in words and use numerals for numbers above one hundred.
Example: "The library has a collection of eighty-five novels and 150 reference books."

Tense Inconsistencies:
Ensure that the text maintains consistent tense usage throughout.
Correct any shifts in tense that might confuse the reader.

Character Names Inconsistencies:
Ensure that character names are consistently used throughout the text.
Example: If a character is introduced as "John Smith," do not later refer to him as "Jon Smith" or "Smith John."
"""

# Define the proofreader function
def proofread_text(input_text):
    prompt = f"""
    You are an expert proofreader at a publishing house, your job is to take the input text, and given rules/guidelines and apply them and output the changed text. 
    Only apply the guideline/rule. Only output the final text, nothing else. These are the rules: 
    {rules}
    This is the input: 
    {input_text}
    """
    response = generate_content(prompt)
    return response

# Streamlit app
st.title("Text Proofreader")

st.write("Provide your text below and click 'Proofread' to apply the proofreading rules.")

input_text = st.text_area("Input Text", height=300)

if st.button("Proofread"):
    if input_text:
        with st.spinner("Proofreading..."):
            proofread_text = proofread_text(input_text)
            st.subheader("Proofread Text")
            st.write(proofread_text)
    else:
        st.error("Please provide input text to proofread.")
